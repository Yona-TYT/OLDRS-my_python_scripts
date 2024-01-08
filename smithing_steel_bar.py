import pyautogui

from time import sleep

import argparse

import keyborad_events

import starting

import tools

# Limites del inventario
inv_lim_a, inv_lim_b = 404, 326

# Initialize counter
cent_plus = 18

# Centro de la pantalla
cent_x, cent_y = 575, 490

	
list_sch_a = [{"x":882, "y":380, "clic":0, "t":2, "c_r": 2, "c_i":1}]
				

list_sch_b = [{"x":206, "y":617, "clic":0, "t":2, "c_r": 1, "c_i":1}]


def smithing():
	clic_delay = 1.5
	furnace_x, furnace_y = 615, 476
	bar_x, bar_y = 229, 817		#steel bars

	if(not tools.wait_in_tile(0, 0)):
		tools.calibrate(2)

	pyautogui.moveTo(furnace_x, furnace_y)
	sleep(clic_delay)
	pyautogui.click()

	pyautogui.moveTo(bar_x, bar_y)
	sleep(clic_delay)
	pyautogui.click()

	inven_check_x, inven_check_y = 1125, 835

	count = 0
	count_max = 155
	try_count = 0
	while (True):
		keyborad_events.main_events()

		if(count>count_max):
			if(try_count>1):
				print("No more Smithing!!")
				tools.exit()
			if(not tools.wait_in_tile(0, 0)):
				tools.calibrate(2)
			pyautogui.moveTo(furnace_x, furnace_y)
			sleep(clic_delay)
			pyautogui.click()

			pyautogui.moveTo(bar_x, bar_y)
			sleep(clic_delay)
			pyautogui.click()
			count = 0
			try_count = try_count + 1

		px_inv = pyautogui.pixel(inven_check_x, inven_check_y)
		count = count + 1
		print("Smithing... Count %d, Pixel %s" % (count, px_inv))
		if (px_inv.red ==62 and px_inv.green ==53 and px_inv.blue ==41):
			run_x, run_y = 1002, 201
			px_run = pyautogui.pixel(run_x, run_y)
			if(px_run.green < 200):
				pyautogui.moveTo(run_x, run_y)
				sleep(clic_delay)
				pyautogui.click()
	
			return 0

def bank():
	clic_delay = 0.5
	bank_x, bank_y = 576, 513
	bank_drop_x, bank_drop_y = 1040, 620
	coal_x, coal_y = 495, 197
	iron_x, iron_y = 445, 197

	pyautogui.moveTo(bank_x, bank_y)
	sleep(clic_delay)
	pyautogui.click()
	sleep(1.8)

	pyautogui.moveTo(bank_drop_x, bank_drop_y)
	sleep(clic_delay)
	pyautogui.click()

	pyautogui.moveTo(coal_x, coal_y)
	sleep(clic_delay)
	pyautogui.click()

	pyautogui.moveTo(iron_x, iron_y)
	sleep(clic_delay)
	pyautogui.click()


def rutine_a():
	bank()
	if(not tools.schedule(list_sch_a, True)):
		print("Schedule Fail")
		tools.exit()

	inven_check_x, inven_check_y = 1125, 835
	px_inv = pyautogui.pixel(inven_check_x, inven_check_y)
	if (px_inv.red ==62 and px_inv.green ==53 and px_inv.blue ==41):
		print("No have more ore!.")
		tools.exit()

def rutine_b():
	if(not tools.schedule(list_sch_b, True)):
		print("Schedule Fail")
		tools.exit()

keyborad_events.start_listener()

#tools.calibrate(3)
#tools.exit()

#Satrting--------------------------
parser = argparse.ArgumentParser()
parser.add_argument("-s", "--starting", help="Starting and set config", action="store_true")
argum = parser.parse_args()

if(argum.starting):
	c_tag = {"x":370, "y":126}
	c_bank = {"x":576, "y":513}
	clic = True
	starting.starting_bank(c_tag, c_bank, clic)

	pyautogui.click(587, 272)

	num = 18
	clic = False
	starting.set_xvalue(num, c_bank, clic)

#-----------------------------------------

while(True):
	rutine_a()
	smithing()
	rutine_b()


