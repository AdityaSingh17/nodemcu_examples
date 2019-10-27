# Code to control LED by capacitive touch on the ESP32 board.

import machine
from machine import TouchPad,Pin

# The 4 pin LED pins are connected to GPIO pins numbered 15,4 and 2 in the following way:
red = machine.Pin(15, machine.Pin.OUT)		
blue = machine.Pin(4, machine.Pin.OUT)
green = machine.Pin(2, machine.Pin.OUT)

on_pad = TouchPad(Pin(14))		# This will signal the touch for turning the LED on.
off_pad = TouchPad(Pin(12))		# This will signal the touch for turning the LED off.

while True:
	x = on_pad.read()			# Read the sensor values and wait for a touch.
	y = off_pad.read()
	if (x<100):					# When the ON sensor is touched, turn on the LED.
		green.on()				# We are using the Green colored LED as an example, any of the LED colors may be used.
	if (y<100):					# When the OFF sensor is touched, turn off the LED.
		green.off()	

