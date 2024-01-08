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

def smithing():
	clic_delay = 1.5
	anvil_x, anvil_y = 584, 511
	smith_x, smith_y = 418, 461		#steel plateboody

	pyautogui.moveTo(anvil_x, anvil_y)
	sleep(clic_delay)
	pyautogui.click(anvil_x, anvil_y)
	sleep(clic_delay)
	pyautogui.moveTo(smith_x, smith_y)
	sleep(clic_delay+0.3)
	pyautogui.click(smith_x, smith_y)

	inven_check_x, inven_check_y = 1039, 835

	count = 0
	count_max = 100

	while (True):
		keyborad_events.main_events()
		if(count>count_max):

			px_cent = pyautogui.pixel(cent_x, cent_y)
			if (px_cent.red !=0 or px_cent.green !=0 or px_cent.blue !=0):
				if(tools.calibrate(1)):
					return False

				else:
					tools.exit()

			pyautogui.moveTo(anvil_x, anvil_y)
			sleep(clic_delay)
			pyautogui.click()

			pyautogui.moveTo(smith_x, smith_y)
			sleep(clic_delay)
			pyautogui.click(smith_x, smith_y)
			count = 0


		px_inv = pyautogui.pixel(inven_check_x, inven_check_y)
		count = count + 1
		print("Smithing... Count %d, Pixel %s" % (count, px_inv))
		if (px_inv.red ==62 and px_inv.green ==53 and px_inv.blue ==41):
			run_x, run_y = 1002, 201
			px_run = pyautogui.pixel(run_x, run_y)
			if(px_run.green < 200):
				pyautogui.moveTo(run_x, run_y)
				sleep(clic_delay)
				pyautogui.click(run_x, run_y)
				sleep(clic_delay)
	
			return True

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




def rutine_a():
	bank()
	if(not tools.schedule(list_sch_a, True)):
		print("Schedule Fail")
		return False

	inven_check_x, inven_check_y = 1039, 835
	px_inv = pyautogui.pixel(inven_check_x, inven_check_y)
	if (px_inv.red ==62 and px_inv.green ==53 and px_inv.blue ==41):
		print("No have more bar!.")
		tools.exit()

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
	smithing()
	rutine_b()



