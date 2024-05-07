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
				{"x":45, "y":417, "clic":0, "t":3, "c_r": 1, "c_i":0},
				{"x":135, "y":436, "clic":0, "t":3, "c_r": 1, "c_i":0}, {"x":145, "y":415, "clic":0, "t":3, "c_r": 1, "c_i":0},
				{"x":253, "y":415, "clic":0, "t":3, "c_r": 1, "c_i":0}
			]
				

list_sch_b =  [
				{"x":1057, "y":575, "clic":0, "t":3, "c_r": 1, "c_i":0}, {"x":983, "y":552, "clic":0, "t":3, "c_r": 1, "c_i":0},
				{"x":1075, "y":535, "clic":0, "t":3, "c_r": 1, "c_i":0}, {"x":895, "y":480, "clic":0, "t":3, "c_r": 1, "c_i":0},
				{"x":860, "y":560, "clic":0, "t":3, "c_r": 1, "c_i":0}
			]
				

def get_sand():
	wait = 35
	clic_delay = 0.5
	clc_a_x, clc_a_y = 1000, 620
	clc_b_x, clc_b_y = 587, 507
	clc_c_x, clc_c_y = 260, 830

	sleep(0.3)
	pyautogui.moveTo(clc_a_x, clc_a_y)
	sleep(clic_delay)
	pyautogui.click()

	sleep(0.8)
	pyautogui.moveTo(clc_b_x, clc_b_y)
	sleep(clic_delay)
	pyautogui.click()

	#sleep(0.8)
	#pyautogui.moveTo(clc_c_x, clc_c_y)
	#sleep(clic_delay)
	#pyautogui.click()

	keyborad_events.main_events()

	print("Waiting.... ", wait)

	sleep(wait)

	run_x, run_y = 1008, 201
	clic_delay = 0.5
	sleep(clic_delay)
	px_run = pyautogui.pixel(run_x, run_y)
	sleep(clic_delay)
	if(px_run.green < 200):
		pyautogui.moveTo(run_x, run_y)
		sleep(clic_delay)
		pyautogui.click(run_x, run_y)
		sleep(clic_delay)



def bank():
	print("Bank...")
	clic_delay = 0.5
	bank_x, bank_y = 607, 472
	bank_drop_x, bank_drop_y = 1000, 620
	clic_a_x, clic_a_y = 545, 270

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

	pyautogui.moveTo(clic_a_x, clic_a_y)
	sleep(clic_delay)
	pyautogui.click()

	run_x, run_y = 1008, 201
	clic_delay = 0.5
	sleep(clic_delay)
	px_run = pyautogui.pixel(run_x, run_y)
	sleep(clic_delay)
	if(px_run.green < 200):
		pyautogui.moveTo(run_x, run_y)
		sleep(clic_delay)
		pyautogui.click(run_x, run_y)
		sleep(clic_delay)




def rutine_a():
	bank()
	if(not tools.schedule(list_sch_a, False)):
		print("Schedule Fail")
		return False

	inven_check_x, inven_check_y = 1039, 835
	px_inv = pyautogui.pixel(inven_check_x, inven_check_y)
	if (px_inv.red ==62 and px_inv.green ==53 and px_inv.blue ==41):
		print("No have more buckes!.")
		tools.exit()

	return True

def rutine_b():
	if(not tools.schedule(list_sch_b, False)):
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
	get_sand()
	rutine_b()



