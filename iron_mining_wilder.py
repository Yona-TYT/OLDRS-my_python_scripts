import pyautogui

from time import sleep

import argparse

import keyborad_events

import tools

# Centro de la pantalla
cent_x, cent_y = 575, 490

	
list_sch_a =	[	{"x":749, "y":792, "clic":0, "t":3.5, "c_r": 0, "c_i":0}, {"x":583, "y":603, "clic":0, "t":2, "c_r": 0, "c_i":0},
					{"x":554, "y":798, "clic":0, "t":2, "c_r": 1, "c_i":3}, {"x":224, "y":803, "clic":0, "t":2, "c_r": 1, "c_i":4}, 
					{"x":320, "y":794, "clic":0, "t":2, "c_r": 0, "c_i":5}, {"x":388, "y":724, "clic":0, "t":2, "c_r": 0, "c_i":6}, 
					{"x":426, "y":716, "clic":0, "t":2, "c_r": 3, "c_i":-1}
				]

list_sch_b =	[	
					{"x":690, "y":315, "clic":0, "t":3, "c_r": 0, "c_i":1}, {"x":712, "y":321, "clic":0, "t":2, "c_r": 0, "c_i":2},
					{"x":757, "y":277, "clic":0, "t":2, "c_r": 1, "c_i":3},
					{"x":787, "y":300, "clic":0, "t":2, "c_r": 1, "c_i":4}, {"x":580, "y":260, "clic":0, "t":2, "c_r": 0, "c_i":5}, 
					{"x":448, "y":296, "clic":0, "t":2, "c_r": 0, "c_i":6}, {"x":593, "y":510, "clic":3, "t":2, "c_r": 2, "c_i":7}
				]

list_sch_pvb =	[	
					{"x":690, "y":315, "clic":0, "t":3, "c_r": 0, "c_i":1}, {"x":712, "y":321, "clic":0, "t":2, "c_r": 0, "c_i":2},
					{"x":757, "y":277, "clic":0, "t":2, "c_r": 1, "c_i":3},
					{"x":787, "y":300, "clic":0, "t":2, "c_r": 1, "c_i":4}, {"x":580, "y":260, "clic":0, "t":2, "c_r": 0, "c_i":5}, 
					{"x":581, "y":231, "clic":0, "t":2, "c_r": 0, "c_i":6}, {"x":439, "y":420, "clic":1, "t":2, "c_r": 2, "c_i":7},
					{"x":610, "y":587, "clic":0, "t":3, "c_r": 2, "c_i":7}
				]

list_sch_min =	[{"x":582, "y":393, "clic":0, "t":3.5, "c_r": 3, "c_i":0}]


def mining_iron():
	# Valores para las iron ore
	list_iron = [	{"x":558, "y":491, "clic":0}, {"x":585, "y":515, "clic":0}	]
	iron_plus_x, iron_plus_y = 75 , 33
	pyautogui.moveTo(list_iron[0]["x"], list_iron[0]["y"])
	pyautogui.click()
	px_iron = pyautogui.pixel(list_iron[0]["x"]+iron_plus_x, list_iron[0]["y"]+iron_plus_y)

	index = 0
	clic_max = 27

	inven_check_x, inven_check_y = 1125, 835
	repeat = 0
	try_count = 0
	while (True):
		keyborad_events.main_events()
		print("Mining... Count %d, Pixel %s" % (clic_max, px_iron))

		px_inv = pyautogui.pixel(inven_check_x, inven_check_y)
		if (px_inv.red !=62 and px_inv.green !=53 and px_inv.blue !=41):
			print("Exit Mining.. Delay: %f s  Px IV: %s" % (0, px_inv))
			return 0

		if(repeat > clic_max):
			repeat = 0
			pyautogui.moveTo(c_x, c_y)
			sleep(0.5)
			pyautogui.click()
			try_count = try_count + 1 

		if(try_count>1):
			try_count = 0
			if(tools.calibrate(3)):
				tools.schedule(list_sch_min, True)
				continue
			else:
				return tools.exit()
			
			
		repeat = repeat + 1

		c_x, c_y = list_iron[index]["x"], list_iron[index]["y"]
		if (px_iron.blue >=250):
			pyautogui.moveTo(c_x, c_y)
			px_iron = pyautogui.pixel(c_x+iron_plus_x, c_y+iron_plus_y)
			continue

		index = not index
		c_x, c_y = list_iron[index]["x"], list_iron[index]["y"]

		min_count = 0
		min_max = 30
		while (px_iron.blue < 250):
			print("Mining--Waiting... min-Count %d, Pixel %s" % (min_count, px_iron))
			if(min_count>min_max):
				min_count = 0
				if(tools.calibrate(3)):
					tools.schedule(list_sch_min, True)
					continue
				else:
					return tools.exit()

			min_count = min_count +1
			keyborad_events.main_events()
			px_iron = pyautogui.pixel(c_x+iron_plus_x, c_y+iron_plus_y)
			pyautogui.moveTo(c_x, c_y)

			px_inv = pyautogui.pixel(inven_check_x, inven_check_y)
			if (px_inv.red !=62 and px_inv.green !=53 and px_inv.blue !=41):
				print("Exit Mining.. Delay: %f s  Px IV: %s" % (0, px_inv))
				return 0

		sleep(0.3)
		pyautogui.click()
		repeat = 0

	px_iron = pyautogui.pixel(c_x+iron_plus_x, list_iron[index]["y"]+iron_plus_y)


def bank():
	print("Bank...")
	clic_delay = 0.5
	bank_x, bank_y = 582, 460
	bank_drop_x, bank_drop_y = 656, 708

	pyautogui.moveTo(bank_x, bank_y)
	sleep(clic_delay)
	pyautogui.click()
	sleep(2.2)

	pyautogui.moveTo(bank_drop_x, bank_drop_y)
	sleep(clic_delay)
	pyautogui.click()



def rutine_a():
	r_sch = tools.schedule(list_sch_a, True)
	if(not r_sch):
		print("Schedule Fail")
		tools.exit()
	elif(r_sch == 2):
		tools.schedule(list_sch_min, True)

	clic_delay = 0.5
	pray_x, pray_y = 990, 165
	pyautogui.moveTo(pray_x, pray_y)
	sleep(clic_delay)
	pyautogui.click()

def rutine_b():
	if(not tools.schedule(list_sch_b, True)):
		print("Schedule Fail")
		tools.exit()

def rutine_pvb():
	if(not tools.schedule(list_sch_pvb, True)):
		print("Schedule Fail")
		tools.exit()

parser = argparse.ArgumentParser()
parser.add_argument("-b", "--placeb", help="Starting in place B", action="store_true")
parser.add_argument("-pvp", "--pvpworld", help="Schedule for pvp", action="store_true")
argum = parser.parse_args()

keyborad_events.start_listener()

if(argum.placeb):
	mining_iron()
	rutine_b()
	bank()

while(True):
	keyborad_events.main_events()
	rutine_a()

	mining_iron()

	if(argum.pvpworld):
		rutine_pvb()
	else:
		rutine_b()

	bank()

