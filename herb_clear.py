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
	bank_x, bank_y = 593, 476
	bank_drop_x, bank_drop_y = 659, 709
	bank_x_x, bank_x_y = 697, 88
	clc_a_x, clc_a_y = 590, 450

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



def herb_clear():

	bank()

	clic_delay = 0.5
	clc_a_x, clc_a_y = 1000, 620
	herb_x, herb_y = 844, 80
	clc_c_x, clc_c_y = 52, 819

	pyautogui.moveTo(clc_a_x, clc_a_y)
	sleep(clic_delay)
	pyautogui.click()
	sleep(1.2)

	while(True):
		keyborad_events.main_events()
		px = pyautogui.pixel(herb_x, herb_y)
		print("Waiting... Count %d, Pixel %s" % (0, px))
		if(px.red < 10 and px.green < 100 and px.blue < 10):
			print("To babn ..")
			return True


def is_complete():
	x, y =  836, 91
	sleep(3)
	while(True):
		keyborad_events.main_events()
		px = pyautogui.pixel(x, y)
		sleep(0.8)
		print("Waiting... Count %d, Pixel %s" % (0, px))
		if (px.red !=9 or px.green !=108 or px.blue !=2):
			return True

	return False

def rutine_a():
	print("Start Herb Clear..")
	herb_clear()


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



