from flask import Blueprint, jsonify
import time

health_bp = Blueprint("health", __name__)

start_time = time.time()

@health_bp.route("/health", methods=["GET"])
def health():
    uptime = time.time() - start_time

    return jsonify({
        "status": "healthy",
        "model": "llama-3.3-70b (Groq)",
        "avg_response_time": "1-2 sec",
        "uptime_seconds": round(uptime, 2)
    })