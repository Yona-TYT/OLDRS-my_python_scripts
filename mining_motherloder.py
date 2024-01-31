import pyautogui

from time import sleep

import keyborad_events

import tools

def get_ribi(c_x, c_y, idx):
	r_plus_x, r_plus_y = 25, 40
	ribi =	[
				{"x":c_x + r_plus_x, "y":c_y, "r": 1},		#Derecha   0
				{"x":c_x - r_plus_x, "y":c_y, "r": 0},		#Izquierda 1
				{"x":c_x, "y":c_y - r_plus_y, "r": 3},		#Ariba     2
				{"x":c_x, "y":c_y + r_plus_y, "r": 2}		#Abajo     3
			]
	return ribi[idx]

# Centro de la pantalla
cent_x, cent_y = 575, 490

	
list_sch_a =	[	{"x":581, "y":510, "clic":2, "t":2.5, "c_r": 0, "c_i":0}, {"x":425, "y":481, "clic":0, "t":2, "c_r": 0, "c_i":0}	]

list_sch_b =	[	{"x":739, "y":441, "clic":0, "t":3.5, "c_r": 0, "c_i":1}, {"x":636, "y":482, "clic":0, "t":1, "c_r": 0, "c_i":2}	]

list_sch_min =	[{"x":530, "y":463, "clic":0, "t":3.5, "c_r": 3, "c_i":0}]


idx = 0

ore_list =	[
				[	#0 ------------------------------------------------------------------------------
					{"x":533, "y":489, "r":0, "i":0, "t":4, "s":0},
					{"x":646, "y":492, "r":2, "i":1, "t":3, "s":0}, {"x":676, "y":491, "r":2, "i":2, "t":3, "s":0},
					{"x":536, "y":423, "r":2, "i":3, "t":3, "s":0}
				],

				[	#1 ------------------------------------------------------------------------------
					{"x":485, "y":442, "r":0, "i":0, "t":4, "s":0},
					{"x":616, "y":442, "r":2, "i":2, "t":3, "s":0},
					{"x":490, "y":381, "r":2, "i":3, "t":3, "s":0},
					{"x":562, "y":422, "r":0, "i":0, "t":3, "s":0}
				],

				[	#2 ------------------------------------------------------------------------------
					{"x":462, "y":443, "r":0, "i":0, "t":4, "s":0},
					{"x":465, "y":383, "r":2, "i":3, "t":3, "s":0},
					{"x":536, "y":424, "r":0, "i":0, "t":3, "s":0},
					{"x":562, "y":447, "r":2, "i":1, "t":3, "s":0}
				],

				[	#3 ------------------------------------------------------------------------------
					{"x":583, "y":513, "r":0, "i":0, "t":1, "s":0},
					{"x":674, "y":490, "r":0, "i":0, "t":5, "s":0},
					{"x":708, "y":516, "r":2, "i":1, "t":5, "s":0},
					{"x":739, "y":516, "r":2, "i":2, "t":4.5, "s":0}
				],

		]


# Centro de la pantalla para mining
cen_min_x, cen_min_y = 580, 490
def mining(c_list, idx):
	cal_x, cal_y = 0 , 0
	idx_a = idx
	idx_b = 1
	gold_plus_x, gold_plus_y = 65 , 33
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

			#Debug ----------------------------------------
			#pyautogui.moveTo(c_x, c_y)
			#Debug ----------------------------------------

			#117, green=123, blue=124
			if(px.red > 110 and px.green > 120 and px.blue > 120):
				dlay = c_list[idx_a][idx_b]["t"]

				c = get_ribi(c_x, c_y, r)


				pyautogui.moveTo(c_x, c_y)
				pyautogui.click(c_x, c_y)
				print("Waiting.. Delay : %f s  Coord: %d, %d --- index: %d" % (dlay, c_x, c_y, idx_b))
				sleep(dlay)

				c = get_ribi(cen_min_x, cen_min_y, r)
				#pyautogui.moveTo(c["x"], c["y"])
			#	if(c_list[idx_a][idx_b]["s"] == 0):
			#		pyautogui.moveTo(c["x"], c["y"])
			#		pyautogui.click(c["x"], c["y"])
			#		sleep(dlay)

			#	c = get_ribi(cen_min_x, cen_min_y, c["r"])

				#Debug ----------------------------------------
				#print("Waiting.. Delay : %f s  Coord: %d, %d" % (dlay, c_x, c_y))
				#Debug ----------------------------------------

				count = 0
				count_max = 50
				px_cent = pyautogui.pixel(cen_min_x, cen_min_y)
				while (px_cent.red !=0 or px_cent.green !=0 or px_cent.blue !=0):
					keyborad_events.main_events()
					px_cent = pyautogui.pixel(cen_min_x, cen_min_y)

					#Debug ----------------------------------------
					sleep(0.2)
					#Debug ----------------------------------------

					pyautogui.moveTo(cen_min_x, cen_min_y)
					count = count + 1
					print("Chag Mine... Count %d, Pixel %s" % (count, px_cent))

					if(count > count_max):
						print("Schedule Fail")
						#if(tools.calibrate(3)):
						#	tools.schedule(list_sch_min, False)
						#	break
						#else:
						return tools.exit()

				pyautogui.moveTo(c["x"], c["y"])
				sleep(0.8)
				#pyautogui.click(c["x"], c["y"])
				px_gold = pyautogui.pixel(c["x"]+gold_plus_x, c["y"]+gold_plus_y)
				print("Mining... Coord x: %d, y: %d, Idx ab: %d, %d --  Pixel %s" % (c["x"], c["y"], idx_a, idx_b, px_gold))
				repeat = 0
				r_max = 50
				while(px_gold.blue == 255):
					keyborad_events.main_events()
					print("Mining... Coord x: %d, y: %d, Idx ab: %d, %d --  Pixel %s" % (c["x"], c["y"], idx_a, idx_b, px_gold))
					pyautogui.moveTo(c["x"], c["y"])
					if(repeat > r_max):
						r_max = r_max *2
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

def rutine_b():
	print("Hoper...")
	clic_delay = 0.5
	clc_a_x, clc_a_y = 556, 477
	inven_check_x, inven_check_y = 1125, 835

	count = 0
	c_max = 100
	tryy = 0
	print("Drop in tolve...")
	pyautogui.moveTo(clc_a_x, clc_a_y)
	sleep(clic_delay)
	pyautogui.click()
	sleep(0.5)
	while(True):
		keyborad_events.main_events()
		px_inv = pyautogui.pixel(inven_check_x, inven_check_y)
		sleep(0.3)
		if (px_inv.red ==62 and px_inv.green ==53 and px_inv.blue ==41):
			break

		if(count > c_max):
			pyautogui.moveTo(clc_a_x, clc_a_y)
			sleep(clic_delay)
			pyautogui.click()
			sleep(1)
			px_inv = pyautogui.pixel(inven_check_x, inven_check_y)
			sleep(0.3)
			if (px_inv.red ==62 and px_inv.green ==53 and px_inv.blue ==41):
				break
			print("Wait... 30")
			sleep(30)
			count = 0
			if(tryy > 4):
				tools.exit()

			tryy = tryy + 1
		count = count+ 1

def rutine_c():

	r_sch = tools.schedule(list_sch_b, True)
	if(not r_sch):
		print("Schedule Fail")
		tools.exit()
	
keyborad_events.start_listener()

#tools.calibrate(2)
#tools.exit()
count = 0
while(True):
	keyborad_events.main_events()
	#rutine_a()

	while(True):
		idx = mining(ore_list, idx)
		if(idx is False):
			break

	rutine_a()
	rutine_b()
	if(count >= 5):
		tools.exit()	

	rutine_c()
	count = count + 1


