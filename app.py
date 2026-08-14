import os

from flask import Flask, render_template, request, jsonify
from google import genai


app = Flask(__name__)


# Load the API key from .env
with open(".env", "r") as file:
    for line in file:
        line = line.strip()

        if line.startswith("GEMINI_API_KEY="):
            key = line.split("=", 1)[1]
            os.environ["GEMINI_API_KEY"] = key


# Create Gemini client
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json()

    message = data.get("message")

    if not message:
        return jsonify({
            "error": "Message is required"
        }), 400

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=message
    )

    return jsonify({
        "response": response.text
    })


if __name__ == "__main__":
    app.run(debug=True)