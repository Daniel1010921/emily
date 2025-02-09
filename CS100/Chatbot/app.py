from flask import Flask, render_template, request

app = Flask(__name__)

# Chatbot logic
responses = {
    "hello": "Hi there! How can I help you?",
    "how are you": "I'm just a chatbot, but I'm doing great!",
    "bye": "Goodbye! Have a nice day!"
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    user_input = request.form["user_input"].lower()
    response = responses.get(user_input, "I don't understand that. Can you try again?")
    return response

if __name__ == "__main__":
    app.run(debug=True)
