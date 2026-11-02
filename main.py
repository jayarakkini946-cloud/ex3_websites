
from flask import Flask, render_template, request

app = Flask(__name__)

# Home route: display the form
@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

# Welcome route: process submitted form
@app.route("/welcome", methods=["POST"])
def welcome():
    name = request.form.get("name", "").strip()

    if not name:
        return render_template(
            "index.html",
            error="Please enter your name."
        ), 400

    return render_template("welcome.html", name=name)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
