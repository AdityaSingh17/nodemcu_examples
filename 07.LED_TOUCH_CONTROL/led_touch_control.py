import machine
from machine import TouchPad,Pin

red = machine.Pin(15, machine.Pin.OUT)
blue = machine.Pin(4, machine.Pin.OUT)
green = machine.Pin(2, machine.Pin.OUT)

on_pad = TouchPad(Pin(14))
off_pad = TouchPad(Pin(12))

while True:
	x = on_pad.read()
	y = off_pad.read()
	if (x<100):
		green.on()
	if (y<100):
		green.off()

