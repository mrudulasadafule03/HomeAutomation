import RPi.GPIO as gpio
from time import sleep

gpio.setmode(gpio.BCM)
gpio.setup(18,gpio.IN)
gpio.setup(12,gpio.OUT)

try:
	while True:
		if gpio.input(18)!=1:
			print("detected")
			gpio.output(12,gpio.HIGH)
		else:
			print("not detected")
			gpio.output(12,gpio.LOW)
		sleep(1)
finally:
	
	print("hello there")
	gpio.cleanup()
