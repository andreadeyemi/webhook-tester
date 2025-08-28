# webhook_tester.py

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    print("\n📬 Webhook received!")
    print("🔐 Headers:", dict(request.headers))
    print("📦 Payload:", request.json)
    return jsonify({"status": "received"}), 200

if __name__ == "__main__":
    print("🚀 Running Webhook Tester on http://localhost:5000/webhook")
    app.run(debug=True, port=5000)
