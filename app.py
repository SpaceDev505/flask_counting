from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/hello")
def say_hello():
    return f"Hello!"


if __name__ == "__main__":
    app.run()