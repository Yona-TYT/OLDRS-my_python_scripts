import pyautogui

from time import sleep

import argparse

import keyborad_events

import starting

import tools

import drops

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



def thieving():

	clic_delay = 0.3
	clc_a_x, clc_a_y = 610, 485
	p_x, p_y = 95, 35


	index = 0
	#col_list = [{"red":64, "green":82, "blue":40, "p_x":0, "p_y":0}, {"red":161, "green":184, "blue":13, "p_x":5, "p_y":5}]
	col_list = [{"red":64, "green":82, "blue":40, "p_x":0, "p_y":0}]
	jump = True
	one = True
	c_try = 0
	nr = 0
	while(True):
		keyborad_events.main_events()
		pyautogui.moveTo(clc_a_x, clc_a_y)
		sleep(clic_delay)
		px = pyautogui.pixel(clc_a_x+p_x , clc_a_y+p_y)
		print("Waiting... index %d, Pixel %s" % (index, px))
		sleep(clic_delay)
		if(px.blue == 255):
			c_try = 0
			pyautogui.click()
			sleep(0.8)

		nr = drops.drop_rgb(index, col_list, jump, one)
		print("Result nr:", nr)
		if(nr > 27):
			print("No more espace!!!")
			tools.exit()

		c_try = c_try + 1
		if(c_try > 5):
			tools.exit()	
	

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

col_list = [{"red":64, "green":82, "blue":40, "p_x":0, "p_y":0}, {"red":161, "green":184, "blue":13, "p_x":5, "p_y":5}]
db_x, db_y = 998, 830
opt = 1
while(True):
	keyborad_events.main_events()
	thieving()
	#drops.drop_debug_list(24, col_list)

	#drops.drop_coord_move(db_x, db_y, col_list, opt)



