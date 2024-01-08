import pyautogui

from time import sleep

import keyborad_events

import tools

def get_ribi(c_x, c_y, idx):
	r_plus_x, r_plus_y = 25, 20
	ribi =	[
				{"x":c_x + r_plus_x, "y":c_y, "r": 1},		#Derecha   0
				{"x":c_x - r_plus_x, "y":c_y, "r": 0},		#Izquierda 1
				{"x":c_x, "y":c_y - r_plus_y, "r": 3},		#Ariba     2
				{"x":c_x, "y":c_y + r_plus_y, "r": 2}		#Abajo     3
			]
	return ribi[idx]

# Centro de la pantalla
cent_x, cent_y = 575, 490

	
list_sch_a =	[	{"x":749, "y":792, "clic":1, "t":3.5, "c_r": 0, "c_i":0}, {"x":583, "y":603, "clic":1, "t":2, "c_r": 0, "c_i":0},
					{"x":554, "y":798, "clic":0, "t":2, "c_r": 1, "c_i":3}, {"x":224, "y":803, "clic":0, "t":2, "c_r": 1, "c_i":4}, 
					{"x":320, "y":794, "clic":0, "t":2, "c_r": 0, "c_i":5}, {"x":388, "y":724, "clic":0, "t":2, "c_r": 0, "c_i":6}, 
					{"x":352, "y":827, "clic":0, "t":2, "c_r": 3, "c_i":-1}
				]

list_sch_b =	[	
					{"x":730, "y":258, "clic":0, "t":3, "c_r": 0, "c_i":1}, {"x":712, "y":321, "clic":0, "t":2, "c_r": 0, "c_i":2},
					{"x":757, "y":277, "clic":0, "t":2, "c_r": 1, "c_i":3},
					{"x":787, "y":300, "clic":0, "t":2, "c_r": 1, "c_i":4}, {"x":580, "y":260, "clic":0, "t":2, "c_r": 0, "c_i":5}, 
					{"x":448, "y":296, "clic":0, "t":2, "c_r": 0, "c_i":7}, {"x":593, "y":510, "clic":3, "t":2, "c_r": 2, "c_i":7}
				]

list_sch_min =	[{"x":530, "y":463, "clic":0, "t":3.5, "c_r": 3, "c_i":0}]


idx = 0

ore_list =	[
				[	#0 ------------------------------------------------------------------------------
					{"x":581, "y":487, "r":0, "i":0, "t":1, "s":0}, {"x":585, "y":503, "r":2, "i":1, "t":1.2, "s":1},
					{"x":575, "y":527, "r":1, "i":2, "t":3, "s":0}

				],
				[	#1 ------------------------------------------------------------------------------
					{"x":581, "y":487, "r":0, "i":0, "t":1, "s":0}, {"x":609, "y":478, "r":1, "i":0, "t":1.2, "s":1},
					{"x":575, "y":527, "r":1, "i":2, "t":3, "s":0}

				],
				[	#2 ------------------------------------------------------------------------------
					{"x":602, "y":439, "r":0, "i":0, "t":3, "s":0}, {"x":630, "y":435, "r":1, "i":0, "t":3, "s":0},
					{"x":609, "y":462, "r":2, "i":1, "t":3, "s":0}

				]
		]


# Centro de la pantalla para mining
cen_min_x, cen_min_y = 580, 482
def mining(c_list, idx):
	cal_x, cal_y = 0 , 0
	idx_a = idx
	idx_b = 1
	gold_plus_x, gold_plus_y = 77 , 33
	delay = 3
	while (True):
		print("Debug... Idx ab: %d, %d " % ( idx_a, idx_b))
		if(idx_b == len(c_list[0])):
			idx_b = 1
		while (idx_b < len(c_list[idx_a])):
			keyborad_events.main_events()
			c_x , c_y, r, i = c_list[idx_a][idx_b]["x"] + cal_x, c_list[idx_a][idx_b]["y"]+ cal_y, c_list[idx_a][idx_b]["r"], c_list[idx_a][idx_b]["i"]
			px = pyautogui.pixel(c_x, c_y)
			print("-- Find Mine... x: %d, y: %d, Idx ab: %d, %d --  Pixel %s" % (c_x, c_y, idx_a, idx_b, px))
			inven_check_x, inven_check_y = 1125, 835
			px_inv = pyautogui.pixel(inven_check_x, inven_check_y)
			if (px_inv.red !=62 and px_inv.green !=53 and px_inv.blue !=41):

				print("Exit Mining x: %d , y: %d Delay: %f s  Px IV: %s" % (c_list[idx_a][0]["x"], c_list[idx_a][0]["y"], delay, px_inv))
				listt = [	{"x":c_list[idx_a][0]["x"], "y":c_list[idx_a][0]["y"], "clic":1, "t":2.5, "c_r": 1, "c_i":1}	]
				
				if(not tools.schedule(listt, True)):
					print("Schedule Fail")
					tools.exit()

				return False
			#pyautogui.moveTo(c_y, c_y)
			if(px.red < 60 and px.green < 60 and px.blue < 60):
				dlay = c_list[idx_a][idx_b]["t"]

				c = get_ribi(c_x, c_y, r)
				if(c_list[idx_a][idx_b]["s"] == 0):
					pyautogui.moveTo(c["x"], c["y"])
					pyautogui.click(c["x"], c["y"])
					sleep(dlay)

				c = get_ribi(cen_min_x, cen_min_y, c["r"])
				#print("Waiting.. Delay : %f s  Coord: %d, %d" % (dlay, c_x, c_y))

				count = 0
				count_max = 30
				px_cent = pyautogui.pixel(cen_min_x, cen_min_y)
				while (px_cent.red !=0 or px_cent.green !=0 or px_cent.blue !=0):
					keyborad_events.main_events()
					px_cent = pyautogui.pixel(cen_min_x, cen_min_y)
					#sleep(0.2)
					pyautogui.moveTo(cen_min_x, cen_min_y)
					count = count + 1
					print("Chag Mine... Count %d, Pixel %s" % (count, px_cent))

					if(count > count_max):
						print("Schedule Fail")
						if(tools.calibrate(3)):
							tools.schedule(list_sch_min, True)
							break
						else:
							return tools.exit()

				pyautogui.moveTo(c["x"], c["y"])
				pyautogui.click(c["x"], c["y"])
				px_gold = pyautogui.pixel(c["x"]+gold_plus_x, c["y"]+gold_plus_y)
				print("Mining... Coord x: %d, y: %d, Idx ab: %d, %d --  Pixel %s" % (c["x"], c["y"], idx_a, idx_b, px_gold))
				repeat = 0
				while(px_gold.blue == 255):
					keyborad_events.main_events()
					print("Mining... Coord x: %d, y: %d, Idx ab: %d, %d --  Pixel %s" % (c["x"], c["y"], idx_a, idx_b, px_gold))
					pyautogui.moveTo(c["x"], c["y"])
					if(repeat > 20):
						repeat = 0
						pyautogui.click(c["x"], c["y"])
						
					px_gold = pyautogui.pixel(c["x"]+gold_plus_x, c["y"]+gold_plus_y)
					px_inv = pyautogui.pixel(inven_check_x, inven_check_y)
					if (px_inv.red !=62 and px_inv.green !=53 and px_inv.blue !=41):
						break

					repeat = repeat + 1

				return i
			idx_b = idx_b +1


	return 0

def bank():
	print("Bank...")
	clic_delay = 0.5
	bank_x, bank_y = 628, 405
	bank_drop_x, bank_drop_y = 656, 708
	#pray_x, pray_y = 990, 165

	pyautogui.moveTo(bank_x, bank_y)
	sleep(clic_delay)
	pyautogui.click()
	sleep(3)

	pyautogui.moveTo(bank_drop_x, bank_drop_y)
	sleep(clic_delay)
	pyautogui.click()

	#pyautogui.moveTo(pray_x, pray_y)
	#sleep(clic_delay)
	#pyautogui.click()

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
	
keyborad_events.start_listener()

#tools.calibrate(2)
#tools.exit()

while(True):
	keyborad_events.main_events()
	rutine_a()

	while(True):
		idx = mining(ore_list, idx)
		if(idx is False):
			break

	rutine_b()

	bank()

