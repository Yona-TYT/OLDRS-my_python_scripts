import pyautogui

from time import sleep

import keyborad_events

import tools

def get_ribi(c_x, c_y, idx):
	r_plus_x, r_plus_y = 15, 20
	ribi =	[
				{"x":c_x + r_plus_x, "y":c_y, "r": 1},		#Derecha   0
				{"x":c_x - r_plus_x, "y":c_y, "r": 0},		#Izquierda 1
				{"x":c_x, "y":c_y - r_plus_y, "r": 3},		#Ariba     2
				{"x":c_x, "y":c_y + r_plus_y, "r": 2}		#Abajo     3
			]
	return ribi[idx]

# Centro de la pantalla
cent_x, cent_y = 575, 490

	
list_sch_a =	[	{"x":860, "y":717, "clic":0, "t":3.5, "c_r": 0, "c_i":0}, {"x":698, "y":618, "clic":0, "t":3.5, "c_r": 0, "c_i":0}]

list_sch_b =	[	{"x":382, "y":320, "clic":0, "t":3.5, "c_r": 0, "c_i":0}]

list_sch_min =	[{"x":530, "y":463, "clic":0, "t":3.5, "c_r": 3, "c_i":0}]


idx = 0

ore_list =	[
				[	#0 ------------------------------------------------------------------------------
					{"x":488, "y":377, "r":0, "i":0, "t":4, "s":0}, 
					{"x":603, "y":507, "r":1, "i":1, "t":2, "s":0}, {"x":634, "y":551, "r":1, "i":2, "t":4, "s":0}, {"x":636, "y":619, "r":1, "i":3, "t":4, "s":0}
				],
				[	#1 ------------------------------------------------------------------------------
					{"x":492, "y":358, "r":0, "i":0, "t":5, "s":0}, 
					{"x":633, "y":524, "r":1, "i":2, "t":1.2, "s":0}, {"x":631, "y":589, "r":1, "i":3, "t":3, "s":0},  {"x":604, "y":452, "r":1, "i":0, "t":2, "s":0}
				],
				[	#2 ------------------------------------------------------------------------------
					{"x":474, "y":322, "r":0, "i":0, "t":5, "s":0},
					{"x":604, "y":533, "r":1, "i":3, "t":3, "s":0}, {"x":578, "y":407, "r":1, "i":0, "t":4, "s":0},  {"x":576, "y":437, "r":1, "i":1, "t":2, "s":0}
				],
				[	#3 ------------------------------------------------------------------------------
					{"x":477, "y":288, "r":0, "i":0, "t":4, "s":0},
					{"x":579, "y":365, "r":1, "i":0, "t":4, "s":0}, {"x":579, "y":394, "r":1, "i":1, "t":3, "s":0},  {"x":604, "y":430, "r":1, "i":2, "t":3, "s":0}
				]
		]


code_list_a = [{"x":504, "y": 512}, {"x":408, "y":651}, {"x":275, "y": 560}, {"e_x":555, "e_y":593}]
code_list_b = [{"x":0, "y": 0}, {"x":0, "y": 0}, {"x":0, "y": 0}, {"e_x":0, "e_y":0}]
code_list_c = [{"x":0, "y": 0}, {"x":0, "y": 0}, {"x":0, "y": 0}, {"e_x":0, "e_y":0}]


code_list = [
				{"list": code_list_a}
			]


# Centro de la pantalla para mining
cen_min_x, cen_min_y = 586, 480
def mining(c_list, idx):
	cal_x, cal_y = 0 , 0
	idx_a = idx
	idx_b = 1
	gold_plus_x, gold_plus_y = 45, 33
	delay = 3

	esp_x, esp_y = 996, 231

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
				
				if(not tools.schedule(listt, False)):
					print("Schedule Fail")
					opt = 1
					if(tools.exit(opt, code_list)):
						bank()
						rutine_a()
						return 0

				return False
			#Debug-------------------------------
		#	pyautogui.moveTo(c_x, c_y)
			#Debug-------------------------------
			if(px.red > 125 ):
				dlay = c_list[idx_a][idx_b]["t"]

				c = get_ribi(c_x, c_y, r)
				if(c_list[idx_a][idx_b]["s"] == 0):
					pyautogui.moveTo(c["x"], c["y"])
					pyautogui.click(c["x"], c["y"])
					sleep(dlay)

				c = get_ribi(cen_min_x, cen_min_y, c["r"])
				#Debug-------------------------------
				print("Waiting.. Delay : %f s  Coord: %d, %d" % (dlay, c_x, c_y))
				#Debug-------------------------------

				count = 0
				count_max = 30
				px_cent = pyautogui.pixel(cen_min_x, cen_min_y)
				while (px_cent.red !=0 or px_cent.green !=0 or px_cent.blue !=0):
					keyborad_events.main_events()
					px_cent = pyautogui.pixel(cen_min_x, cen_min_y)
					#Debug-------------------------------
					sleep(0.2)
					#Debug-------------------------------
					pyautogui.moveTo(cen_min_x, cen_min_y)
					count = count + 1
					print("Chag Mine... Count %d, Pixel %s" % (count, px_cent))

					if(count > count_max):
						print("Schedule Fail")
						#if(tools.calibrate(3)):
						#	tools.schedule(list_sch_min, True)
						#	break
						#else:
						return tools.exit()


				px_esp = pyautogui.pixel(esp_x, esp_y)
				if (px_esp.red == 0 and px_esp.green == 255 and px_esp.blue == 0):
					sleep(0.5)
					pyautogui.moveTo(esp_x+22, esp_y-5)
					pyautogui.click(esp_x+22, esp_y-5)
					sleep(0.5)

				pyautogui.moveTo(c["x"], c["y"])
				pyautogui.click(c["x"], c["y"])
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
	bank_x, bank_y = 556, 484
	bank_drop_x, bank_drop_y = 549, 510
	#pray_x, pray_y = 990, 165

	pyautogui.moveTo(bank_x, bank_y)
	sleep(clic_delay)
	pyautogui.click()
	sleep(2)

	pyautogui.moveTo(bank_drop_x, bank_drop_y)
	sleep(clic_delay)
	pyautogui.click()

	#pyautogui.moveTo(pray_x, pray_y)
	#sleep(clic_delay)
	#pyautogui.click()

def rutine_a():
	r_sch = tools.schedule(list_sch_a, False)
	if(not r_sch):
		print("Schedule Fail")
		opt = 1
		if(tools.exit(opt, code_list)):
			bank()
			rutine_a()



def rutine_b():
	if(not tools.schedule(list_sch_b, False)):
		print("Schedule Fail")
		opt = 1
		if(tools.exit(opt, code_list)):
			return True
	
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

