from flask import Blueprint, request, jsonify
from groq import Groq
from service.cache import r, get_cache_key
import os
import json
from datetime import datetime

report_bp = Blueprint("report", __name__)

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def load_prompt():
    with open("prompts/generate_report.txt", "r") as f:
        return f.read()

@report_bp.route("/generate-report", methods=["POST"])
def generate_report():
    data = request.get_json()

    # Validate input
    if not data or "input" not in data:
        return jsonify({"error": "Missing input"}), 400

    user_input = data["input"]

    # ✅ CACHE START
    key = get_cache_key(user_input)

    cached = r.get(key)
    if cached:
        return jsonify({
            "report": json.loads(cached),
            "cached": True
        })
    # ✅ CACHE END

    # Load prompt
    prompt = load_prompt().replace("{input}", user_input)

    # Call Groq
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )

    output = response.choices[0].message.content

    output = output.replace("```json", "").replace("```", "").strip()

    # Convert to JSON
    try:
        report = json.loads(output)
    except:
        return jsonify({
            "error": "Invalid JSON from model",
            "raw_output": output
        }), 500

    # ✅ SAVE TO CACHE (15 min = 900 sec)
    r.setex(key, 900, json.dumps(report))

    return jsonify({
        "report": report,
        "generated_at": datetime.utcnow().isoformat(),
        "cached": False
    })