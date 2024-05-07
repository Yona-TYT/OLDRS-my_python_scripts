import pyautogui

from time import sleep

import argparse

import os

from pynput import keyboard

import keyborad_events

from termcolor import colored


def main(argum):
	x, y = pyautogui.position() # Get the XY position of the mouse.
	px = pyautogui.pixel(x, y)

	# Initialize counter
	counter = 0
	cent_plus = 18

	p_x, p_y = 95, 35

	cent_x, cent_y = 585, 490

	color = {"red":161, "green":184, "blue":13}


	while (True):
		keyborad_events.main_events()
		#os.system('unclutter -idle 1')c
		x, y = pyautogui.position() # Get the XY position of the mouse.
		if(argum.plus):
			px = pyautogui.pixel(x+p_x, y+p_y)
			print("Plus Mouse x: %d, y: %d, Pixel %s" % (x+p_x, y+p_y, px))

		else:
			px = pyautogui.pixel(x, y)

			if(argum.color):
				print("Color Mouse x: %d, y: %d, Pixel %s" % (x, y, px))
				sleep(0.1)
				if(px.red == color["red"] and px.green == color["green"] and px.blue == color["blue"]):
					print(colored(("-- Exit Color.... x: %d, y: %d -- Pixel %s" % (x, y, px)), "green" ))
					break
#<Mouse x: 707, y: 483, Pixel RGB(red=0, green=0, blue=1)
#Mouse x: 740, y: 511, Pixel RGB(red=0, green=0, blue=1)
#<Plus Mouse x: 685, y: 485, Pixel RGB(red=73, green=60, blue=45)


			else:
				print("Mouse x: %d, y: %d, Pixel %s" % (x, y, px))
		#tx = ("%s" % cola.get())
		#if(tx == "c"):
		#print("%s" % tx)


		#if(px.red > 130 and px.green > 110 and px.blue < 50):
			# Print values
		#	print("Mouse /x/:%d, /y/:%d, Pixel %s" % (x, y, px))
		#	sleep(5)



keyborad_events.start_listener()

#--------------------------
parser = argparse.ArgumentParser()
parser.add_argument("-p", "--plus", help="Plus mode", action="store_true")
parser.add_argument("-col", "--color", help="Detect color code", action="store_true")
argum = parser.parse_args()

main(argum)



