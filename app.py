from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "status": "online",
        "project": "Jugaad Bhai Automation",
        "message": "Automation engine is running"
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "time": datetime.utcnow().isoformat()
    })

@app.route("/generate")
def generate():
    return jsonify({
        "status": "ready",
        "mission": "Mission ₹10",
        "workflow": [
            "Find product",
            "Create script",
            "Create short video",
            "Prepare post"
        ]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
