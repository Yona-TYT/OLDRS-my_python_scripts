import pyautogui

from time import sleep

import sys

import keyborad_events


def starting():
	clic_delay = 1.7

	c_look_x, c_look_y = 1000, 90
	pyautogui.moveTo(c_look_x, c_look_y)
	sleep(clic_delay)
	pyautogui.click()

	pyautogui.moveTo(575, 490)
	pyautogui.scroll(-20)
	sleep(clic_delay)

	pyautogui.keyDown('up')
	sleep(0.5)
	pyautogui.keyUp('up')

	inven_x, inven_y = 860, 870
	px_inv = pyautogui.pixel(inven_x, inven_y)
	if (px_inv.red < 100 and px_inv.green > 40 and px_inv.blue > 30):
		pyautogui.moveTo(inven_x, inven_y)
		sleep(clic_delay)
		pyautogui.click()

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
cent_x, cent_y = 585, 490

	
list_sch_a =	[
					{"x":864, "y":834, "clic":0, "t":4}, {"x":613, "y":836, "clic":0, "t":4}]

list_sch_b =	[
					{"x":581, "y":535, "clic":0, "t":1.8}, {"x":803, "y":174, "clic":0, "t":8},
					{"x":862, "y":192, "clic":0, "t":6}, {"x":737, "y":195, "clic":0, "t":6}, 
					{"x":361, "y":259, "clic":1, "t":6}, {"x":585, "y":489, "clic":2, "t":0.8},	
					{"x":759, "y":737, "clic":0, "t":3}
				]


list_sch_test =	[
					{"x":334, "y":260, "clic":1, "t":4}, {"x":576, "y":489, "clic":2, "t":0.8},
					{"x":759, "y":737, "clic":0, "t":0.5}
				]

list_sch_c =	[
					{"x":577, "y":462, "clic":2, "t":0.8}, {"x":948, "y":820, "clic":0, "t":6},
					{"x":378, "y":837, "clic":0, "t":4}, {"x":122, "y":690, "clic":0, "t":4}, 
					{"x":373, "y":801, "clic":0, "t":4}, {"x":610, "y":899, "clic":0, "t":4}
				]

list_sch_d =	[
					{"x":581, "y":453, "clic":2, "t":2}, {"x":560, "y":281, "clic":0, "t":4},
					{"x":415, "y":279, "clic":0, "t":4}
				]

ship_a_x, ship_a_y = 465, 537
ship_b_x, ship_b_y = 550, 479

ship_a = {"x":465, "y":537}
ship_b = {"x":293, "y":845}

cross_a = {"x":580, "y":545}
cross_b = {"x":582, "y":454}

def ship(ship, cross, clic = False):
	delay = 0.8
	sleep(delay)
	plus_x, plus_y = 0, 40

	pyautogui.moveTo(ship["x"], ship["y"])
	pyautogui.click(button='right')
	sleep(0.8)
	if(not clic):
		pyautogui.click(x = ship["x"] + plus_x, y = ship["y"] + plus_y)

	else:
		pyautogui.click(x = ship["x"], y = ship["y"])

	print("Waiting.. Delay")
	sleep(1)
	px_cent = pyautogui.pixel(cent_x, cent_y)
	count = 0
	count_max = 65
	black = 0
	while (True):
		keyborad_events.main_events()
		if(px_cent.red ==0 or px_cent.green ==0 or px_cent.blue ==0):
			black = black +1
			print("Black Count %d, Pixel %s" % (black, px_cent))
			if(black > 2): break
				
		px_cent = pyautogui.pixel(cent_x, cent_y)
		pyautogui.moveTo(cent_x, cent_y)
		count = count + 1
		print("Ship Travely... Count %d, Pixel %s" % (count, px_cent))
		if(count > count_max):
			print("Schedule Fail")
			sys.exit()

	p_x, p_y = 54 , 33
	pyautogui.moveTo(cross["x"], cross["y"])
	px = pyautogui.pixel(cross["x"] + p_x, cross["y"] + p_y)
	while(px.blue != 255):
		keyborad_events.main_events()
		print("Waiting Cross... Coord x: %d, y: %d,   Pixel %s" % (cross["x"],  cross["y"], px))
		pyautogui.moveTo(cross["x"], cross["y"])
		px = pyautogui.pixel(cross["x"] + p_x, cross["y"] + p_y)

	sleep(1)


def schedule(list_sch):
	counter = 0

	walk_plus_x, walk_plus_y = (-5) , 40

	while (counter < len(list_sch)):
		keyborad_events.main_events()
		c_x, c_y = list_sch[counter]["x"], list_sch[counter]["y"]
		delay = list_sch[counter]["t"]
		pyautogui.moveTo(c_x, c_y)
		if(list_sch[counter]["clic"]==1):
			pyautogui.click(button='right')
			sleep(0.5)
			pyautogui.moveTo(c_x, c_y+walk_plus_y)
			sleep(0.5)
			pyautogui.click(x = c_x + walk_plus_x, y = c_y + walk_plus_y)

		elif(list_sch[counter]["clic"]==3):
			sleep(1.2)
			pyautogui.click(c_x, c_y)

		else:
			pyautogui.click(c_x, c_y)

		print("Waiting.. Delay : %f s  index: %d" % (delay, counter))
		sleep(delay)

		x, y = pyautogui.position() # Get the XY position of the mouse.
		px_cent = pyautogui.pixel(cent_x, cent_y)
		# Print values
		#print("Mouse = %d,%d , Pixel %s, Pixel Center %s" % (x, y, px_cent, px_cent))

		if(list_sch[counter]["clic"]==2):
			print("Schedule Skip... Indx: %d , XY: %d,%d -- Pixel %s" % ( counter, c_x, c_y, px_cent))
			counter = counter + 1
			continue
			
		count = 0
		count_max = 90
		while (px_cent.red !=0 or px_cent.green !=0 or px_cent.blue !=0):
			keyborad_events.main_events()
			px_cent = pyautogui.pixel(cent_x, cent_y)
			#pyautogui.moveTo(cent_x, cent_y)

			count = count + 1
			print("Schedule... Count %d, Indx: %d , XY: %d,%d -- Pixel %s" % (count, counter, c_x, c_y, px_cent))
			if(count > count_max):
				return False
		
		counter = counter + 1
	return True


rut_a = 1

idx = 0

ore_list =	[
				[	#0 ------------------------------------------------------------------------------
					{"x":442, "y":315, "r":0, "i":0, "t":3}, {"x":554, "y":533, "r":2, "i":1, "t":2.2},
					{"x":577, "y":579, "r":2, "i":2, "t":3}, {"x":631, "y":578, "r":2, "i":3, "t":3}, 
					{"x":669, "y":578, "r":2, "i":4, "t":3}, {"x":690, "y":505, "r":1, "i":5, "t":3},
					{"x":688, "y":482, "r":1, "i":6, "t":3}
				],
				[	#1 ------------------------------------------------------------------------------
					{"x":470, "y":308, "r":0, "i":0, "t":3}, {"x":603, "y":559, "r":2, "i":2, "t":2.2},
					{"x":660, "y":557, "r":2, "i":3, "t":3}, {"x":691, "y":558, "r":2, "i":4, "t":3},
					{"x":711, "y":479, "r":1, "i":5, "t":3}, {"x":702, "y":469, "r":1, "i":6, "t":3}, 
					{"x":572, "y":465, "r":0, "i":0, "t":3}
				],
				[	#2 ------------------------------------------------------------------------------
					{"x":455, "y":274, "r":0, "i":0, "t":3}, {"x":628, "y":506, "r":2, "i":3, "t":2.2},
					{"x":662, "y":504, "r":2, "i":4, "t":3}, {"x":682, "y":444, "r":1, "i":5, "t":3},
					{"x":681, "y":422, "r":1, "i":6, "t":3}, {"x":556, "y":423, "r":0, "i":0, "t":3},
					{"x":542, "y":466, "r":2, "i":1, "t":3}
				],
				[	#3 ------------------------------------------------------------------------------
					{"x":413, "y":272, "r":0, "i":0, "t":3}, {"x":610, "y":504, "r":2, "i":4, "t":1.5},
					{"x":622, "y":441, "r":1, "i":5, "t":3}, {"x":638, "y":422, "r":1, "i":6, "t":3},
					{"x":503, "y":421, "r":0, "i":0, "t":3}, {"x":505, "y":461, "r":2, "i":1, "t":3},
					{"x":527, "y":503, "r":2, "i":2, "t":3}
				],
				[	#4 ------------------------------------------------------------------------------
					{"x":394, "y":274, "r":0, "i":0, "t":3}, {"x":612, "y":440, "r":1, "i":5, "t":2.2},
					{"x":612, "y":422, "r":1, "i":6, "t":3}, {"x":480, "y":421, "r":0, "i":0, "t":3},
					{"x":473, "y":460, "r":2, "i":1, "t":3}, {"x":496, "y":505, "r":2, "i":2, "t":3},
					{"x":550, "y":505, "r":2, "i":3, "t":1.5}
				],
				[	#5 ------------------------------------------------------------------------------
					{"x":384, "y":299, "r":0, "i":0, "t":3}, {"x":611, "y":451, "r":1, "i":6, "t":1.7},
					{"x":471, "y":463, "r":0, "i":0, "t":3}, {"x":475, "y":505, "r":2, "i":1, "t":3},
					{"x":498, "y":557, "r":2, "i":2, "t":3}, {"x":553, "y":557, "r":2, "i":3, "t":3},
					{"x":588, "y":557, "r":2, "i":4, "t":3}
				],
				[	#6 ------------------------------------------------------------------------------
					{"x":380, "y":316, "r":0, "i":0, "t":3}, {"x":480, "y":482, "r":0, "i":0, "t":3},
					{"x":468, "y":524, "r":2, "i":1, "t":3}, {"x":498, "y":580, "r":2, "i":2, "t":3},
					{"x":553, "y":579, "r":2, "i":3, "t":3}, {"x":588, "y":576, "r":2, "i":4, "t":3},
					{"x":614, "y":505, "r":1, "i":5, "t":1.7}
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
		if(idx_b == 7):
			idx_b = 1
		while (idx_b < len(c_list[idx_a])):
			keyborad_events.main_events()
			c_x , c_y, r, i = c_list[idx_a][idx_b]["x"] + cal_x, c_list[idx_a][idx_b]["y"]+ cal_y, c_list[idx_a][idx_b]["r"], c_list[idx_a][idx_b]["i"]
			px = pyautogui.pixel(c_x, c_y)
			print("-- Find Mine... x: %d, y: %d, Idx ab: %d, %d --  Pixel %s" % (c_x, c_y, idx_a, idx_b, px))
			inven_check_x, inven_check_y = 1125, 835
			px_inv = pyautogui.pixel(inven_check_x, inven_check_y)
			if (px_inv.red !=62 and px_inv.green !=53 and px_inv.blue !=41):
				delay = 5
				pyautogui.moveTo(c_list[idx_a][0]["x"], c_list[idx_a][0]["y"])
				sleep(0.8)
				pyautogui.click()
				print("Exit Mining x: %d , y: %d Delay: %f s  Px IV: %s" % (c_list[idx_a][0]["x"], c_list[idx_a][0]["y"], delay, px_inv))
				sleep(delay)
				px_cent = pyautogui.pixel(cen_min_x, cen_min_y)
				count = 0
				count_max = 30
				while (px_cent.red !=0 or px_cent.green !=0 or px_cent.blue !=0):
					keyborad_events.main_events()
					px_cent = pyautogui.pixel(cen_min_x, cen_min_y)
					#pyautogui.moveTo(cen_min_x, cen_min_y)
					count = count + 1
					print("Exit Mining... Count %d, Pixel %s" % (count, px_cent))
					if(count > count_max):
						print("Schedule Fail")
						sys.exit()

				print("Exit Mining Delay...")
				sleep(0.5)
				return False
			#pyautogui.moveTo(c_y, c_y)
			if(px.red > 130 and px.green > 110 and px.blue < 55):
				c = get_ribi(c_x, c_y, r)
				pyautogui.moveTo(c["x"], c["y"])
				pyautogui.click(c["x"], c["y"])
				c = get_ribi(cen_min_x, cen_min_y, c["r"])

				dlay = c_list[idx_a][idx_b]["t"]
				#print("Waiting.. Delay : %f s  Coord: %d, %d" % (dlay, c_x, c_y))
				sleep(dlay)

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
						sys.exit()

				pyautogui.moveTo(c["x"], c["y"])
				pyautogui.click(c["x"], c["y"])
				px_gold = pyautogui.pixel(c["x"]+gold_plus_x, c["y"]+gold_plus_y)
				print("Mining... Coord x: %d, y: %d, Idx ab: %d, %d --  Pixel %s" % (c["x"], c["y"], idx_a, idx_b, px_gold))
				while(px_gold.blue == 255):
					keyborad_events.main_events()
					print("Mining... Coord x: %d, y: %d, Idx ab: %d, %d --  Pixel %s" % (c["x"], c["y"], idx_a, idx_b, px_gold))
					pyautogui.moveTo(c["x"], c["y"])
					px_gold = pyautogui.pixel(c["x"]+gold_plus_x, c["y"]+gold_plus_y)
					px_inv = pyautogui.pixel(inven_check_x, inven_check_y)
					if (px_inv.red !=62 and px_inv.green !=53 and px_inv.blue !=41):
						break

				return i
			idx_b = idx_b +1


	return 0
	#print("Mining... Count %d, Pixel %s" % (c_list[0][0]["x"], c_list[0][0]["y"]))

def bank():
	clic_delay = 0.5
	bank_x, bank_y = 578, 453
	bank_drop_x, bank_drop_y = 548, 512
	run_x, run_y = 1002, 201

	pyautogui.moveTo(bank_x, bank_y)
	sleep(clic_delay)
	pyautogui.click(bank_x, bank_y)
	sleep(1.8)

	pyautogui.moveTo(bank_drop_x, bank_drop_y)
	sleep(clic_delay)
	pyautogui.click(bank_drop_x, bank_drop_y)

	px_run = pyautogui.pixel(run_x, run_y)
	if(px_run.green < 200):
		pyautogui.moveTo(run_x, run_y)
		sleep(clic_delay)
		pyautogui.click(run_x, run_y)

def rutine_a():
	bank()
	if(not schedule(list_sch_a)):
		print("Schedule Fail")
		sys.exit()

	ship(ship_a, cross_a)
	if(not schedule(list_sch_b)):
		print("Schedule Fail")
		sys.exit()

def rutine_b():
	if(not schedule(list_sch_c)):
		print("Schedule Fail")
		sys.exit()

	ship(ship_b, cross_b, True)

	if(not schedule(list_sch_d)):
		print("Schedule Fail")
		sys.exit()

keyborad_events.start_listener()
starting()
while(True):
	#schedule(list_sch_test)
	if(rut_a): rutine_a()

	while(True):
		idx = mining(ore_list, idx)
		if(idx is False):
			break

	rutine_b()



