import pyautogui

from time import sleep

import os

from pynput import keyboard


def main():
	x, y = pyautogui.position() # Get the XY position of the mouse.
	px = pyautogui.pixel(x, y)

	# Initialize counter
	counter = 0
	cent_plus = 18

	p_x, p_y = 0 , 0

	cent_x, cent_y = 585, 490


	while (True):
		#os.system('unclutter -idle 1')c
		x, y = pyautogui.position() # Get the XY position of the mouse.
		px = pyautogui.pixel(x+p_x, y+p_y)
		#tx = ("%s" % cola.get())
		#if(tx == "c"):
		#print("%s" % tx)

		print("Mouse x: %d, y: %d, Pixel %s" % (x, y, px))
		#if(px.red > 130 and px.green > 110 and px.blue < 50):
			# Print values
		#	print("Mouse /x/:%d, /y/:%d, Pixel %s" % (x, y, px))
		#	sleep(5)




main()



