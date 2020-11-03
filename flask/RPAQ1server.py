from flask import Flask
from pyfirmata import Arduino, util
import serial

app = Flask(__name__)
ser = serial.Serial('/dev/ttyACM1', 9600)

@app.route("/")
def hello():
    return "connecting"

@app.route("/red_on")
def on1():
    ser.write(b'1')
    return "on 접속"

@app.route("/red_off")
def off1():
    ser.write(b'2')
    return "off 접속"
##########################
@app.route("/blue_on")
def on2():
    ser.write(b'3')
    return "on 접속"

@app.route("/blue_off")
def off2():
    ser.write(b'4')
    return "off 접속"
##########################
@app.route("/green_on")
def on3():
    ser.write(b'5')
    return "on 접속"

@app.route("/green_off")
def off3():
    ser.write(b'6')
    return "off 접속"
##########################
@app.route("/all_on")
def on4():
    ser.write(b'7')
    return "on 접속"

@app.route("/all_off")
def off4():
    ser.write(b'8')
    return "off 접속"
##########################

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 8080)


