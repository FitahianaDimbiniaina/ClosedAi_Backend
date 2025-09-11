import logging
from flask import Flask, request, jsonify
from gemini_setup import get_gemini_response
from flask_cors import CORS
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

app = Flask(__name__)
CORS(app, origins=["https://closedaifita.netlify.app"]) 

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_input = data.get("message", "")

    if not user_input:
        return jsonify({"error": "No message provided"}), 400

    try:
        logging.info(f"User input: {user_input}")
        response = get_gemini_response(user_input)
        return jsonify({"response": response})
    except Exception as e:
        logging.error(f"Error getting response: {e}")
        return jsonify({"error": "Something went wrong"}), 500

@app.route("/", methods=["GET"])
def home():
    return "✅ Flask Gemini API is running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
