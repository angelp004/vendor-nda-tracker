from flask import Flask, request, jsonify
from services.groq_client import GroqClient
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import bleach
import re

app = Flask(__name__)

# Rate limit (30 requests per minute)
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["30 per minute"]
)

client = GroqClient()

# Prompt injection patterns
BLOCK_PATTERNS = [
    r"ignore previous instructions",
    r"system prompt",
    r"act as",
    r"bypass",
    r"jailbreak"
]

# Input sanitisation middleware
@app.before_request
def sanitize_input():

    if request.method == "POST" and request.is_json:
        data = request.get_json()

        # Missing input
        if not data or "text" not in data:
            return jsonify({
                "success": False,
                "error": "Missing 'text' field"
            }), 400

        text = data["text"]

        # Remove HTML
        clean_text = bleach.clean(text, tags=[], strip=True)

        # Detect prompt injection
        for pattern in BLOCK_PATTERNS:
            if re.search(pattern, clean_text, re.IGNORECASE):
                return jsonify({
                    "success": False,
                    "error": "Unsafe input detected"
                }), 400

        request.cleaned_text = clean_text


# API endpoint
@app.route("/describe", methods=["POST"])
def describe():
    try:
        user_input = request.cleaned_text

        prompt = f"Explain the following in simple terms:\n{user_input}"

        result = client.generate_response(prompt)

        return jsonify({
            "success": True,
            "description": result["response"]
        })

    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(debug=True)