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

list_sch_a = [
				{"x":893, "y":589, "clic":0, "t":2, "c_r": 1, "c_i":0},
				{"x":649, "y":835, "clic":0, "t":2, "c_r": 1, "c_i":0},
				{"x":581, "y":769, "clic":0, "t":2, "c_r": 1, "c_i":0},
				{"x":581, "y":831, "clic":0, "t":2, "c_r": 1, "c_i":0},
				{"x":744, "y":757, "clic":0, "t":2, "c_r": 1, "c_i":0},
				{"x":780, "y":622, "clic":0, "t":2, "c_r": 1, "c_i":0},
				{"x":1119, "y":564, "clic":0, "t":2, "c_r": 1, "c_i":0},
				{"x":881, "y":519, "clic":0, "t":2, "c_r": 1, "c_i":0}
			]
				

list_sch_b = [
				{"x":257, "y":449, "clic":0, "t":2, "c_r": 1, "c_i":0},
				{"x":80, "y":410, "clic":0, "t":2, "c_r": 1, "c_i":0},
				{"x":412, "y":372, "clic":0, "t":2, "c_r": 1, "c_i":0},
				{"x":473, "y":311, "clic":0, "t":2, "c_r": 1, "c_i":0},
				{"x":581, "y":272, "clic":0, "t":2, "c_r": 1, "c_i":0},
				{"x":579, "y":221, "clic":0, "t":2, "c_r": 1, "c_i":0},
				{"x":536, "y":273, "clic":0, "t":2, "c_r": 1, "c_i":0},
				{"x":319, "y":397, "clic":0, "t":2, "c_r": 1, "c_i":0}
			]

def bank():
	print("Bank...")
	clic_delay = 0.5
	bank_x, bank_y = 578, 454
	bank_drop_x, bank_drop_y = 995, 620
	ess_x, ess_y = 492, 196

	pyautogui.moveTo(bank_x, bank_y)
	sleep(clic_delay)
	pyautogui.click()
	sleep(1.8)

	pyautogui.moveTo(bank_drop_x, bank_drop_y)
	sleep(clic_delay)
	pyautogui.click()
	sleep(1.8)

	pyautogui.moveTo(ess_x, ess_y)
	sleep(clic_delay)
	pyautogui.click()
	sleep(1.8)

def runecrafting():
	True

def rutine_a():
	bank()
	if(not tools.schedule(list_sch_a, True)):
		print("Schedule Fail")
		return False

	return True

def rutine_b():
	if(not tools.schedule(list_sch_b, True)):
		print("Schedule Fail")
		return False

	return True

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

	rutine_b()



