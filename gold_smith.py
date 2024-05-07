import pyautogui

from time import sleep

import keyborad_events

import starting

import tools

# Centro de la pantalla
cent_x, cent_y = 575, 490

list_sch_a = [{"x":882, "y":380, "clic":0, "t":2, "c_r": 2, "c_i":2}]

list_sch_b = [{"x":206, "y":617, "clic":0, "t":2, "c_r": 1, "c_i":1}]

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
		if(not is_working(w_c, pixel) and count > count_max):
			if(c_try>3):
				print("No more try..!!")
				tools.exit()

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
		if (px_inv.red >200 and px_inv.green >150 and px_inv.blue < 30):
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
		if(not is_working(w_c, pixel) and count > count_max):
			if(c_try>3):
				print("No more try..!!")
				tools.exit()
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
		if (px_inv.red < 150 and px_inv.green < 150 and px_inv.blue < 20):
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
#starting.starting_bank(c_tag, c_bank, False)
#pyautogui.click(300, 272)

while(True):
	bank()
	if(not tools.schedule(list_sch_a, True)):
		print("Schedule Fail")
		tools.exit()
	smithing()
	crafting()
	if(not tools.schedule(list_sch_b, True)):
		print("Schedule Fail")
		tools.exit()


