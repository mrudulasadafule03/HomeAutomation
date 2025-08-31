import RPi.GPIO as gpio
from gpiozero import AngularServo
from time import sleep

gpio.setmode(gpio.BCM)
servo = AngularServo(21,min_pulse_width=0.0008,max_pulse_width=0.0023)#gpio pin no used

servo.angle=0
gpio.setup(2,gpio.IN)
gpio.setup(21,gpio.OUT)

while(True):
	val=gpio.input(2)
	if(val!=1):
		servo.angle=90
	else:
		servo.angle=-90
		