import pyautogui

from time import sleep

import argparse

import keyborad_events

import starting

import tools

# Initialize counter
cent_plus = 18

# Centro de la pantalla
cent_x, cent_y = 575, 490

list_sch_a = [{"x":676, "y":751, "clic":0, "t":2, "c_r": 1, "c_i":0}]
				

list_sch_b = [{"x":513, "y":296, "clic":0, "t":2, "c_r": 1, "c_i":1}]


def bank():
	print("Bank...")
	clic_delay = 0.5
	bank_x, bank_y = 533, 476
	bank_drop_x, bank_drop_y = 1040, 620
	bank_x_x, bank_x_y = 697, 88
	clc_a_x, clc_a_y = 539, 344

	pyautogui.moveTo(bank_x, bank_y)
	sleep(clic_delay)
	pyautogui.click()
	sleep(1.8)

	pyautogui.moveTo(bank_drop_x, bank_drop_y)
	sleep(clic_delay)
	pyautogui.click()

	sleep(0.8)

	pyautogui.moveTo(clc_a_x, clc_a_y)
	sleep(clic_delay)
	pyautogui.click()

	sleep(0.8)

	pyautogui.moveTo(bank_x_x, bank_x_y)
	sleep(clic_delay)
	pyautogui.click()

	sleep(0.8)

def chop_chop():
	clic_delay = 0.5

	#Mouse x: 564, y: 416, Pixel RGB(red=124, green=84, blue=0)

	#Mouse x: 567, y: 434, Pixel RGB(red=142, green=98, blue=0)

	#Mouse x: 616, y: 486, Pixel RGB(red=100, green=47, blue=0)

	#Mouse x: 568, y: 435, Pixel RGB(red=83, green=31, blue=0)


	tree_a_x, tree_a_y = 564, 416
	tree_b_x, tree_b_y = 623, 490

	while(True):
		keyborad_events.main_events()
		px_a = pyautogui.pixel(tree_a_x, tree_a_y)
		if(px_a.red > 40 and px_a.blue ==0):
			print("Tree A Chop Chop!...")
			pyautogui.moveTo(tree_a_x, tree_a_y)
			sleep(clic_delay)
			pyautogui.click()
			sleep(1.2)
			if(is_chop(tree_a_x, tree_a_y) == 2):
				make_arr()
				is_complete()
		px_b = pyautogui.pixel(tree_b_x, tree_b_y)
		if(px_a.red > 40 and px_a.blue ==0):
			print("Tree B Chop Chop!...")
			pyautogui.moveTo(tree_b_x, tree_b_y)
			sleep(clic_delay)
			pyautogui.click()
			sleep(1.2)
			if(is_chop(tree_b_x, tree_b_y) == 2):
				make_arr()
				is_complete()

def make_arr():

	clic_delay = 0.5
	clc_a_x, clc_a_y = 995, 617
	clc_b_x, clc_b_y = 1080, 617
	clc_c_x, clc_c_y = 52, 819

	pyautogui.moveTo(clc_a_x, clc_a_y)
	sleep(clic_delay)
	pyautogui.click()
	sleep(1.2)

	pyautogui.moveTo(clc_b_x, clc_b_y)
	sleep(clic_delay)
	pyautogui.click()
	sleep(1.2)

	#px = pyautogui.pixel(clc_b_x, clc_b_y)
	#if(px.red ==62 and px.green ==53 and px.blue ==41):
	#	print("No more logs")
	#	tools.exit()

	pyautogui.moveTo(clc_c_x, clc_c_y)
	sleep(clic_delay)
	pyautogui.click()
	sleep(1.2)


def is_chop(x, y):
	clic_delay = 0.5
	sleep(2)
	full_x, full_y = 1120, 836
	count = 0
	c_max = 30
	while(True):
		keyborad_events.main_events()
		px_full = pyautogui.pixel(full_x, full_y)
		sleep(0.2)
		if(px_full.red != 62 and px_full.green != 53 and px_full.blue != 41):
			return 2
		px = pyautogui.pixel(x, y)
		sleep(0.2)
		print("Chop Chop! wait... %d, Pixel %s" % (count, px))
		if(px.green > 40 and px.blue !=0):
			return 1

		if(count > c_max):
			pyautogui.moveTo(x, y)
			sleep(clic_delay)
			px = pyautogui.pixel(x, y)
			if(px.red > 40 and px.blue ==0):
				pyautogui.click()
				sleep(1.2)
				count = 0
				c_max = c_max *2

		count = count +1

	return False

def is_complete():
	full_x, full_y = 1120, 836
	sleep(3)
	while(True):
		keyborad_events.main_events()
		px = pyautogui.pixel(full_x, full_y)
		sleep(0.8)
		print("Waiting... Count %d, Pixel %s" % (0, px))
		if(px.red == 62 and px.green == 53 and px.blue == 41):
			return True

	return False

def rutine_a():
	print("Start Chop Chop!...")
	chop_chop()

keyborad_events.start_listener()

#Satrting--------------------------
parser = argparse.ArgumentParser()
parser.add_argument("-s", "--starting", help="Starting and set config", action="store_true")
argum = parser.parse_args()

if(argum.starting):
	c_tag = {"x":370, "y":126}
	c_bank = {"x":611, "y":465}
	clic = True
	starting.starting_bank(c_tag, c_bank, clic)

	pyautogui.click(635, 198)

	num = 25
	clic = False
	starting.set_xvalue(num, c_bank, clic)

#-----------------------------------------

while(True):
	keyborad_events.main_events()
	rutine_a()



