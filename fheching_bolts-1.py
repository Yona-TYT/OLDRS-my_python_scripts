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
	bank_x, bank_y = 611, 465
	bank_drop_x, bank_drop_y = 1040, 620
	bar_x, bar_y = 590, 237

	pyautogui.moveTo(bank_x, bank_y)
	sleep(clic_delay)
	pyautogui.click()
	sleep(1.8)

	pyautogui.moveTo(bank_drop_x, bank_drop_y)
	sleep(clic_delay)
	pyautogui.click()

	pyautogui.moveTo(bank_drop_x, bank_drop_y)
	sleep(clic_delay)
	pyautogui.click()

	pyautogui.moveTo(bar_x, bar_y)
	sleep(clic_delay)
	pyautogui.click()


def make_arr():
	clic_delay = 0.5
	clc_a_x, clc_a_y = 995, 617
	clc_b_x, clc_b_y = 1040, 617
	clc_c_x, clc_c_y = 257, 825

	print("Clic A...")
	pyautogui.moveTo(clc_a_x, clc_a_y)
	sleep(clic_delay)
	pyautogui.click()
	sleep(0.5)

	print("Clic B...")
	pyautogui.moveTo(clc_b_x, clc_b_y)
	sleep(clic_delay)
	pyautogui.click()
	sleep(0.5)

	px = pyautogui.pixel(clc_a_x, clc_a_y)
	if(px.red ==62 and px.green ==53 and px.blue ==41):
		print("No more")
		tools.exit()

	px = pyautogui.pixel(clc_b_x, clc_b_y)
	if(px.red ==62 and px.green ==53 and px.blue ==41):
		print("No more")
		tools.exit()

	sleep(0.5)


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
	print("Start Make..")
	make_arr()
	print("Delay ...")
	sleep(0.4)
	#is_complete()

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



