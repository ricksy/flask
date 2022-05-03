from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route("/<name>")
def hello_world(name):
    return f" Hello, {escape(name)}!"

@app.route("/")
def index():
    return "index page"

@app.route("/hello")
def hello():
    return "Hello"

@app.route("/number/<int:myNumber>")
def meow(myNumber):
    return f"Ladies and gentle men, this is Mambo number {escape(myNumber)}"
