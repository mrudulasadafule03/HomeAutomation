from flask import Flask
from flask import Flask,render_template
import RPi.GPIO as gpio
import time

app=Flask(__name__)
light1=17
fan=24
in2=23
en=25

gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
gpio.setup(light1,gpio.OUT)
gpio.setup(in2,gpio.OUT)
gpio.setup(en,gpio.OUT)
gpio.setup(fan,gpio.OUT)
gpio.output(light1,0)
gpio.output(fan,0)
gpio.output(in2,0)
p=gpio.PWM(en,1000)

p.start(25)
print ("Done")


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/BON')
def light1_on():
    gpio.output(light1,1)
    return render_template('index.html')


@app.route('/BOFF')
def light1_off():
    gpio.output(light1,0)
    return render_template('index.html')


@app.route('/FON')
def fan_on():
    print("P")
    while(True):
        gpio.output(fan,1)
        gpio.output(in2,gpio.LOW)
        return render_template('index.html')

@app.route('/FOFF')
def fan_off():
    gpio.output(fan,0)
    return render_template('index.html')


if __name__ == "__main__":
    print("Start")
    app.run(host="192.168.123.132",port='5010')
