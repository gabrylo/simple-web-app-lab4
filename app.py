from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    
    # Prosta logika zależna od godziny
    hour = now.hour
    if 5 <= hour < 12:
        greeting = "Dzień dobry! Poranna sesja DevOps."
    elif 12 <= hour < 18:
        greeting = "Witaj po południu!"
    else:
        greeting = "Dobry wieczór! Praca trwa nawet w nocy."

    return jsonify({
        "message": greeting,
        "server_time": current_time,
        "status": "Aplikacja działa poprawnie"
    })

@app.route("/health")
def health():
    return jsonify({"status": "UP"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)