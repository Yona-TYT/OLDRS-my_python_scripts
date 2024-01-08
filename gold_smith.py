import pyautogui

import sys

from time import sleep

import keyborad_events

import starting

screenWidth, screenHeight = pyautogui.size() # Get the size of the primary monitor.
x, y = pyautogui.position() # Get the XY position of the mouse.
px = pyautogui.pixel(x, y)


# Limites del inventario
inv_lim_a, inv_lim_b = 404, 326

# Initialize counter
cent_plus = 18

# Centro de la pantalla
cent_x, cent_y = 575, 490

ribi_plus = 50
ribi = [{"x":700+ribi_plus, "y":480}, {"x":700, "y":480+ribi_plus}, {"x":700-ribi_plus, "y":480}, {"x":700, "y":480-ribi_plus}]
	
list_sch_a = [{"x":882, "y":380, "r":0}]
				

list_sch_b = [{"x":206, "y":617, "r":0}]

def schedule(list_sch):
	counter = 0
	delay = 3

	while (counter < len(list_sch)):
		keyborad_events.main_events()
		pyautogui.moveTo(list_sch[counter]["x"], list_sch[counter]["y"])
		pyautogui.click()

		print("Waiting.. Delay")
		sleep(delay)

		x, y = pyautogui.position() # Get the XY position of the mouse.
		px_cent = pyautogui.pixel(cent_x, cent_y)
		# Print values
		#print("Mouse = %d,%d , Pixel %s, Pixel Center %s" % (x, y, px_cent, px_cent))

		count = 0
		count_max = 40
		while (px_cent.red !=0 or px_cent.green !=0 or px_cent.blue !=0):
			keyborad_events.main_events()
			px_cent = pyautogui.pixel(cent_x, cent_y)
			#pyautogui.moveTo(cent_x, cent_y)
			count = count + 1
			print("Schedule... Count %d, Pixel %s" % (count, px_cent))

			if(count > count_max):
				return False
		
		counter = counter + 1
	return True

def is_working(c, pixel):
	px = pyautogui.pixel(c["x"], c["y"])
	if (px.red !=pixel["r"] and px.green !=pixel["g"] and px.blue !=pixel["b"]):
		return False
	else:
		return True
	
def smithing():
	clic_delay = 1.7
	furnace_x, furnace_y = 615, 476
	bar_x, bar_y = 290, 817		#gold bars

	pyautogui.moveTo(furnace_x, furnace_y)
	sleep(clic_delay)
	pyautogui.click()

	pyautogui.moveTo(bar_x, bar_y)
	sleep(clic_delay)
	pyautogui.click()

	inven_check_x, inven_check_y = 1132, 842

	count = 0
	count_max = 450

	pixel = {"r":117, "g":123, "b":124}
	w_c = {"x":840, "y":80}
	c_try = 0
	while (True):
		keyborad_events.main_events()
		if(not is_working(w_c, pixel) and count > 20):
			if(c_try>3):
				return 0
			pyautogui.moveTo(furnace_x, furnace_y)
			sleep(clic_delay)
			pyautogui.click()

			pyautogui.moveTo(bar_x, bar_y)
			sleep(clic_delay)
			pyautogui.click()
			c_try = c_try +1
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
				pyautogui.click()
	
			return 0

def crafting():
	clic_delay = 1.7
	furnace_x, furnace_y = 615, 476
	amulet_x, amulet_y = 273, 453		#amulet

	pyautogui.moveTo(furnace_x, furnace_y)
	sleep(clic_delay)
	pyautogui.click()

	pyautogui.moveTo(amulet_x, amulet_y)
	sleep(clic_delay)
	pyautogui.click()

	inven_check_x, inven_check_y = 1133, 832

	count = 0
	count_max = 250

	pixel = {"r":88, "g":58, "b":12}
	w_c = {"x":838, "y":83}
	c_try = 0
	while (True):
		keyborad_events.main_events()
		if(not is_working(w_c, pixel) and count > 20):
			if(c_try>3):
				sys.exit()
			pyautogui.moveTo(furnace_x, furnace_y)
			sleep(clic_delay)
			pyautogui.click()

			pyautogui.moveTo(amulet_x, amulet_y)
			sleep(clic_delay)
			pyautogui.click()
			c_try = c_try +1
			count = 0

		px_inv = pyautogui.pixel(inven_check_x, inven_check_y)
		count = count + 1
		print("Crafting... Count %d, Pixel %s" % (count, px_inv))
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
	gold_x, gold_y = 395, 197

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

	pyautogui.moveTo(gold_x, gold_y)
	sleep(clic_delay)
	pyautogui.click()


keyborad_events.start_listener()

c_tag = {"x":370, "y":126}
c_bank = {"x":576, "y":513}
starting.starting_bank(c_tag, c_bank)
pyautogui.click(300, 272)

while(True):
	bank()
	if(not schedule(list_sch_a)):
		print("Schedule Fail")
		break
	smithing()
	crafting()
	if(not schedule(list_sch_b)):
		print("Schedule Fail")
		break


