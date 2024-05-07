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

list_sch_a = [{"x":280, "y":522, "clic":0, "t":3, "c_r": 1, "c_i":0}]
				

list_sch_b = [{"x":812, "y":459, "clic":0, "t":3, "c_r": 1, "c_i":1}]


def bank():
	print("Bank...")
	clic_delay = 0.5
	bank_x, bank_y = 560, 480
	bank_drop_x, bank_drop_y = 660, 708
	bank_x_x, bank_x_y = 697, 88
	clc_a_x, clc_a_y = 640, 235

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



def cooking():
	inven_check_x, inven_check_y = 1128, 832
	nomore_x, nomore_y = 1083, 617

	clic_delay = 0.8
	cook_delay = 65
	clc_a_x, clc_a_y = 610, 470
	clc_b_x, clc_b_y = 255, 830
	clc_c_x, clc_c_y = 1125, 835

	px_inv = pyautogui.pixel(nomore_x, nomore_y)
	sleep(0.3)
	if (px_inv.red ==62 and px_inv.green ==53 and px_inv.blue ==41):
		print("No more fish ..!")
		tools.exit()

	pyautogui.moveTo(clc_a_x, clc_a_y)
	sleep(clic_delay)
	pyautogui.click()
	sleep(clic_delay)

	pyautogui.moveTo(clc_b_x, clc_b_y)
	sleep(clic_delay)
	pyautogui.click()
	sleep(clic_delay)

	print("Cooking Delay...", cook_delay)
	sleep(cook_delay)




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
	bank()

	r_sch = tools.schedule(list_sch_a, False)
	if(not r_sch):
		print("Schedule Fail")
		tools.exit()

	print("Start Cooking..")
	cooking()

def rutine_b():
	r_sch = tools.schedule(list_sch_b, False)
	if(not r_sch):
		print("Schedule Fail")
		tools.exit()


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



