from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/on")
def on():
    return "on 접속"

@app.route("/off")
def off():
    return "off 접속"

if __name__ == "__main__":
    app.run()


