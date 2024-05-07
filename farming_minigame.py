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


list_farm = [
				{"x":505, "y":455}, {"x":530, "y":570}, {"x":530, "y":570}, {"x":530, "y":570}, 
				{"x":660, "y":490}, {"x":630, "y":415}, {"x":630, "y":415}, {"x":630, "y":415}
			]


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



def make_arr():

	bank()

	clic_delay = 0.5
	clc_a_x, clc_a_y = 995, 617
	clc_b_x, clc_b_y = 1040, 617
	clc_c_x, clc_c_y = 52, 819

	pyautogui.moveTo(clc_a_x, clc_a_y)
	sleep(clic_delay)
	pyautogui.click()
	sleep(1.2)

	pyautogui.moveTo(clc_b_x, clc_b_y)
	sleep(clic_delay)
	pyautogui.click()
	sleep(1.2)

	px = pyautogui.pixel(clc_b_x, clc_b_y)
	if(px.red ==62 and px.green ==53 and px.blue ==41):
		print("No more logs")
		tools.exit()

	pyautogui.moveTo(clc_c_x, clc_c_y)
	sleep(clic_delay)
	pyautogui.click()
	sleep(1.2)


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


def farm_rutine_a():
	print("Start Sembrado...")
	idx = 0
	delay_a = 0.3
	delay_b = 1
	delay_c = 3.3
	clc_a_x, clc_a_y = 1000, 615
	while (idx < len(list_farm)):
		keyborad_events.main_events()
		x, y =  list_farm[idx]["x"], list_farm[idx]["y"]
		print("Farming... idx %d, x,y: %d,%d " % (idx, x, y))
		sleep(delay_a)
		pyautogui.moveTo(clc_a_x, clc_a_y)
		pyautogui.click(clc_a_x, clc_a_y)
		sleep(delay_b)
		pyautogui.moveTo(x, y)
		pyautogui.click(x, y)
		sleep(delay_c)
		idx = idx + 1

def farm_rutine_b(count):
	print("Start Riego...")
	idx = 0
	delay_a = 0.3
	delay_b = 1
	delay_c = 3.5
	#clc_a_x, clc_a_y = 1000, 615
	while (idx < len(list_farm)):
		keyborad_events.main_events()
		x, y =  list_farm[idx]["x"], list_farm[idx]["y"]
		print("Farming... count: %d --- idx %d, x,y: %d,%d " % (count, idx, x, y))
		sleep(delay_b)
		pyautogui.moveTo(x, y)
		sleep(delay_a)
		pyautogui.click(x, y)
		sleep(delay_c)
		idx = idx + 1

def rutine_a():
	farm_rutine_a()
	loop = 4
	count = 0
	delay_a = 8.5
	delay_b = 18
	while (count < loop):
		if(count == 2):
			print("Delay Riego... ", delay_a)
			sleep(delay_a)
		if(count == 3):
			print("Delay Cosecha... ", delay_b)
			sleep(delay_b)

		farm_rutine_b(count)
		count = count + 1
		

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
lmax = 37
count = 0 
while(count < lmax):
	keyborad_events.main_events()
	rutine_a()
	count = count + 1

tools.exit()



