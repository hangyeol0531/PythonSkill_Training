from flask import Flask
from pyfirmata import Arduino, util
import serial

app = Flask(__name__)
ser = serial.serial('/dev/ttyACM0', 9600)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/on")
def on():
    ser.write(b'1')
    return "on 접속"

@app.route("/off")
def off():
    ser.write(b'0')
    return "off 접속"

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 8080)


