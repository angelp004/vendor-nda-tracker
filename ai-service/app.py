from flask import Flask, request, jsonify
from services.groq_client import GroqClient
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import bleach
import re
import jwt

app = Flask(__name__)

# 🔐 JWT Secret (use env variable in real apps)
SECRET_KEY = "mysecretkey"

# Rate limit
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

# 🔐 JWT verification
def verify_token(token):
    try:
        jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return True
    except:
        return False


# 🔐 Input sanitisation + validation
@app.before_request
def sanitize_input():

    if request.method == "POST":

        # ✅ Check JSON
        if not request.is_json:
            return jsonify({"success": False, "error": "Invalid JSON"}), 400

        data = request.get_json()

        # ✅ Missing field
        if not data or "text" not in data:
            return jsonify({"success": False, "error": "Missing 'text' field"}), 400

        text = data["text"]

        # ✅ Empty input
        if not text or not text.strip():
            return jsonify({"success": False, "error": "Empty input"}), 400

        # ❌ Reject HTML
        if re.search(r"<.*?>", text):
            return jsonify({"success": False, "error": "HTML not allowed"}), 400

        # 🔐 PII check (email / phone)
        if re.search(r"\S+@\S+|\b\d{10}\b", text):
            return jsonify({"success": False, "error": "PII not allowed"}), 400

        # Clean input
        clean_text = bleach.clean(text, tags=[], strip=True)

        # 🔐 Prompt injection detection
        for pattern in BLOCK_PATTERNS:
            if re.search(pattern, clean_text, re.IGNORECASE):
                return jsonify({"success": False, "error": "Unsafe input detected"}), 400

        request.cleaned_text = clean_text


# 🚀 API endpoint (JWT protected)
@app.route("/describe", methods=["POST"])
def describe():

    # 🔐 JWT check
    # token = request.headers.get("Authorization")
    # if not token or not verify_token(token):
      #   return jsonify({"success": False, "error": "Unauthorized"}), 401

    try:
        user_input = request.cleaned_text

        prompt = f"""
You are a legal expert.

Explain the following clearly in simple terms.
Include:
- Key points
- Risks
- Penalties

Text:
{user_input}
"""

        result = client.generate_response(prompt)

        return jsonify({
            "success": True,
            "description": result["response"]
        }), 200

    except Exception:
        return jsonify({
            "success": False,
            "error": "AI service failed"
        }), 500

@app.route("/generate-report", methods=["POST"])
def generate_report():

    try:
        data = request.get_json()

        if not data or "text" not in data:
            return jsonify({"success": False, "error": "Missing 'text' field"}), 400

        user_input = data["text"]

        prompt = f"""
You are a legal analyst.

Generate a structured NDA risk report with:

- Title
- Summary (2-3 lines)
- Overview
- Key Issues
- Recommendations

Details:
{user_input}

Keep it clear and structured.
"""

        result = client.generate_response(prompt)

        return jsonify({
            "success": True,
            "report": result["response"]
        }), 200

    except Exception:
        return jsonify({
            "success": False,
            "error": "AI service failed"
        }), 500
    

    
if __name__ == "__main__":
    app.run(debug=False)


    