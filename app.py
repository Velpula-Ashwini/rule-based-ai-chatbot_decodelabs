from flask import Flask, request, jsonify, render_template
import threading
import subprocess
import time

app = Flask(__name__)

responses = {
    "hello": "Hey there! How can I help you?",
    "hi": "Hi! What's up?",
    "hey": "Hey! How can I assist you?",
    "how are you": "I'm doing great, thanks for asking!",
    "what is ai": "AI is the simulation of human intelligence by machines.",
    "what can you do": "I can answer your questions and chat with you!",
    "tell me a joke": "Why do programmers prefer dark mode? Because light attracts bugs!",
    "bye": "Goodbye! See you around.",
    "thanks": "You're welcome!",
    "who made you": "I was built by an AI Engineer intern at DecodeLabs!"
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "").lower().strip()
    reply = responses.get(user_input, "I don't understand that. Try something else!")
    return jsonify({"reply": reply})

def open_browser():
    time.sleep(1)
    subprocess.Popen(['start', 'msedge', 'http://127.0.0.1:5000'], shell=True)

if __name__ == "__main__":
    threading.Thread(target=open_browser).start()
    app.run(debug=False)