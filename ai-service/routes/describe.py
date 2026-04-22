print("DESCRIBE LOADED")
from flask import Blueprint, request, jsonify
from groq import Groq
import os
from datetime import datetime


describe_bp = Blueprint("describe", __name__)

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def load_prompt():
    with open("prompts/describe.txt", "r") as f:
        return f.read()

@describe_bp.route("/describe", methods=["POST"])
def describe():
    data = request.get_json()

    # Validate input
    if not data or "input" not in data:
        return jsonify({"error": "Missing input"}), 400

    user_input = data["input"]

    # Load prompt
    prompt = load_prompt().replace("{input}", user_input)

    # Call Groq
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )

    output = response.choices[0].message.content

    # Return structured response
    return jsonify({
        "result": output,
        "generated_at": datetime.utcnow().isoformat()
    })