import pyautogui

from time import sleep

import keyborad_events

import tools


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


code_list_a = [{"x":443, "y": 330}, {"x":582, "y": 588}, {"x":731, "y": 590}, {"e_x":583, "e_y":507}]
code_list_b = [{"x":706, "y": 414}, {"x":582, "y": 533}, {"x":462, "y": 619}, {"e_x":610, "e_y":511}]
code_list_c = [{"x":0, "y": 0}, {"x":0, "y": 0}, {"x":0, "y": 0}, {"e_x":0, "e_y":0}]


code_list = [
				{"list": code_list_a}, {"list": code_list_b}
			]


list_sch_a =	[
					{"x":864, "y":834, "clic":0, "t":4, "c_r": 1, "c_i":1}, {"x":613, "y":836, "clic":0, "t":4, "c_r": 1, "c_i":1}]

list_sch_b =	[
					{"x":581, "y":535, "clic":0, "t":1.8, "c_r": 1, "c_i":1}, {"x":803, "y":174, "clic":0, "t":8, "c_r": 1, "c_i":1},
					{"x":862, "y":192, "clic":0, "t":6, "c_r": 1, "c_i":1}, {"x":737, "y":195, "clic":0, "t":6, "c_r": 2, "c_i":4}, 
					{"x":361, "y":259, "clic":4, "t":6, "c_r": 2, "c_i":4}, {"x":585, "y":489, "clic":0, "t":0.8, "c_r": 1, "c_i":1},	
					{"x":765, "y":715, "clic":0, "t":3, "c_r": 2, "c_i":7}
				]


list_sch_test =	[
					{"x":334, "y":260, "clic":1, "t":4}, {"x":576, "y":489, "clic":2, "t":0.8},
					{"x":759, "y":737, "clic":0, "t":0.5}
				]

list_sch_c =	[
					{"x":950, "y":785, "clic":0, "t":3, "c_r": 0, "c_i":1},
					{"x":373, "y":867, "clic":0, "t":4, "c_r": 1, "c_i":2}, {"x":122, "y":690, "clic":0, "t":4, "c_r": 0, "c_i":1}, 
					{"x":373, "y":801, "clic":0, "t":4, "c_r": 1, "c_i":1}, {"x":610, "y":899, "clic":0, "t":4, "c_r": 1, "c_i":1}
				]

list_sch_d =	[
					{"x":581, "y":453, "clic":2, "t":2, "c_r": 1, "c_i":1}, {"x":560, "y":281, "clic":0, "t":4, "c_r": 1, "c_i":1},
					{"x":415, "y":279, "clic":0, "t":4, "c_r": 1, "c_i":1}
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
	pyautogui.click()
	sleep(0.8)
	#if(not clic):
	#	pyautogui.click(x = ship["x"] + plus_x, y = ship["y"] + plus_y)

	#else:
	#	pyautogui.click(x = ship["x"], y = ship["y"])

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
			tools.exit()

	p_x, p_y = 54 , 33
	pyautogui.moveTo(cross["x"], cross["y"])
	px = pyautogui.pixel(cross["x"] + p_x, cross["y"] + p_y)
	while(px.blue != 255):
		keyborad_events.main_events()
		print("Waiting Cross... Coord x: %d, y: %d,   Pixel %s" % (cross["x"],  cross["y"], px))
		pyautogui.moveTo(cross["x"], cross["y"])
		px = pyautogui.pixel(cross["x"] + p_x, cross["y"] + p_y)

	sleep(1)

rut_a = 1

mark_list_a = [{"x":435, "y": 587}, {"x":278, "y": 434}, {"x":725, "y": 560}, {"e_x":447, "e_y":317}]
mark_list_b = [{"x":313, "y": 419}, {"x":517, "y": 721}, {"x":643, "y": 272}, {"e_x":470, "e_y":305}]
mark_list_c = [{"x":550, "y": 790}, {"x":450, "y": 510}, {"x":675, "y": 340}, {"e_x":458, "e_y":270}]
mark_list_d = [{"x":395, "y": 505}, {"x":535, "y": 420}, {"x":235, "y": 590}, {"e_x":413, "e_y":272}]
mark_list_e = [{"x":563, "y": 243}, {"x":483, "y": 440}, {"x":367, "y": 510}, {"e_x":393, "e_y":273}]
mark_list_f = [{"x":383, "y": 721}, {"x":212, "y": 415}, {"x":171, "y": 762}, {"e_x":385, "e_y":300}]
mark_list_g = [{"x":260, "y": 685}, {"x":638, "y": 505}, {"x":205, "y": 435}, {"e_x":380, "e_y":317}]
mark_list_h = [{"x":605, "y": 585}, {"x":540, "y": 305}, {"x":470, "y": 590}, {"e_x":357, "e_y":342}]

mark_list = [
				{"list": mark_list_a}, {"list": mark_list_b}, {"list": mark_list_c}, {"list": mark_list_d},
				{"list": mark_list_e}, {"list": mark_list_f}, {"list": mark_list_g}, {"list": mark_list_h}
			]

mine_list_a = [{"x":435, "y": 587}, {"x":278, "y": 434}, {"x":725, "y": 560}, {"e_x":580, "e_y":485}]
mine_list_b = [{"x":313, "y": 419}, {"x":517, "y": 721}, {"x":643, "y": 272}, {"e_x":605, "e_y":465}]
mine_list_c = [{"x":550, "y": 790}, {"x":450, "y": 510}, {"x":675, "y": 340}, {"e_x":580, "e_y":420}]
mine_list_d = [{"x":395, "y": 505}, {"x":535, "y": 420}, {"x":235, "y": 590}, {"e_x":535, "e_y":420}]
mine_list_e = [{"x":563, "y": 243}, {"x":483, "y": 440}, {"x":367, "y": 510}, {"e_x":511, "e_y":422}]
mine_list_f = [{"x":383, "y": 721}, {"x":212, "y": 415}, {"x":171, "y": 762}, {"e_x":505, "e_y":460}]
mine_list_g = [{"x":260, "y": 685}, {"x":638, "y": 505}, {"x":205, "y": 435}, {"e_x":505, "e_y":485}]
mine_list_h = [{"x":377, "y": 436}, {"x":679, "y": 683}, {"x":618, "y": 755}, {"e_x":522, "e_y":653}]
mine_list_hh = [{"x":0, "y": 0}, {"x":0, "y": 0}, {"x":0, "y": 0}, {"e_x":0, "e_y":0}]

mine_list = [
				{"list": mine_list_a}, {"list": mine_list_b}, {"list": mine_list_c}, {"list": mine_list_d},
				{"list": mine_list_e}, {"list": mine_list_f}, {"list": mine_list_g}, {"list": mine_list_h}
			]

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
	try_c = 0
	while (True):
		print("Debug... Idx ab: %d, %d " % ( idx_a, idx_b))
		if(idx_b == 7):
			idx_b = 1
		while (idx_b < len(c_list[idx_a])):
			keyborad_events.main_events()
			c_x , c_y, r, i = c_list[idx_a][idx_b]["x"] + cal_x, c_list[idx_a][idx_b]["y"]+ cal_y, c_list[idx_a][idx_b]["r"], c_list[idx_a][idx_b]["i"]
			px = pyautogui.pixel(c_x, c_y)
			print("-- Find Mine... x: %d, y: %d, Idx ab: %d, %d --  Pixel %s" % (c_x, c_y, idx_a, idx_b, px))

			if(try_c > 3):

				px_cent = pyautogui.pixel(cent_x, cent_y)
				if (px_cent.red !=0 or px_cent.green !=0 or px_cent.blue !=0):
					print("-- Find Mining Fail: ", try_c)
					try_c = 0
					if(tools.calibrate(2)):
						return 0
					else:
						return tools.exit()

			try_c = try_c + 1

			if(try_c > 15):
				print("-- Find Mining Fail (mine): ", try_c)
				calib = tools.start_calb_code(mine_list)
				return 0

			inven_check_x, inven_check_y = 1125, 835
			px_inv = pyautogui.pixel(inven_check_x, inven_check_y)
			if (px_inv.red !=62 and px_inv.green !=53 and px_inv.blue !=41):
				delay = 1.5
				#pyautogui.moveTo(c_list[idx_a][0]["x"], c_list[idx_a][0]["y"])
				#sleep(0.8)
				#pyautogui.click()
				print("-- Calib Mining (mark): ", try_c)
				calib = tools.start_calb_code_idx(mark_list, idx_a, delay)
				if(not calib):
					tools.start_calb_code(mark_list)


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
						tools.exit()

				return False
			#pyautogui.moveTo(c_y, c_y)
			if(px.red > 100 and px.green > 80 ):
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
						print("Mining Fail")
						if(tools.calibrate(2)):
							return 0
						else:
							return tools.exit()

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
	run_x, run_y = 1008, 201

	pyautogui.moveTo(bank_x, bank_y)
	sleep(clic_delay)
	pyautogui.click(bank_x, bank_y)
	sleep(1.8)

	pyautogui.moveTo(bank_drop_x, bank_drop_y)
	sleep(clic_delay)
	pyautogui.click(bank_drop_x, bank_drop_y)
	sleep(clic_delay)
	px_run = pyautogui.pixel(run_x, run_y)
	sleep(clic_delay)
	if(px_run.green < 200):
		pyautogui.moveTo(run_x, run_y)
		sleep(clic_delay)
		pyautogui.click(run_x, run_y)

def rutine_a():
	bank()
	if(not tools.schedule(list_sch_a)):
		print("Schedule Fail")
		tools.exit()

	ship(ship_a, cross_a)

	if(not tools.schedule(list_sch_b, True)):
		print("Schedule Fail")
		tools.exit()

	run_x, run_y = 1008, 201
	clic_delay = 0.5
	sleep(clic_delay)
	px_run = pyautogui.pixel(run_x, run_y)
	sleep(clic_delay)
	if(px_run.green < 200):
		pyautogui.moveTo(run_x, run_y)
		sleep(clic_delay)
		pyautogui.click(run_x, run_y)




door_list_a = [{"x":582, "y": 335}, {"x":782, "y": 462}, {"x":747, "y": 558}, {"e_x":583, "e_y":480}]
door_list_b = [{"x":764, "y": 716}, {"x":404, "y": 648}, {"x":785, "y": 832}, {"e_x":582, "e_y":461}]
door_list_c = [{"x":396, "y": 378}, {"x":787, "y": 483}, {"x":776, "y": 788}, {"e_x":581, "e_y":510}]

door_list = [
				{"list": door_list_a}, {"list": door_list_b}, {"list": door_list_c}
			]


def rutine_b():
	run_x, run_y = 1008, 201
	clic_delay = 0.5
	sleep(clic_delay)
	px_run = pyautogui.pixel(run_x, run_y)
	sleep(clic_delay)
	if(px_run.green < 200):
		pyautogui.moveTo(run_x, run_y)
		sleep(clic_delay)
		pyautogui.click(run_x, run_y)


	door_x, door_y = 582, 460
	door_time = 0.8
	pyautogui.moveTo(door_x, door_y)
	sleep(clic_delay)
	pyautogui.click(door_x, door_y)
	sleep(door_time)
	index = 0
	click = False
	while(True):
		print("-- Try in door...")
		calib = tools.start_calb_code_idx(door_list, index, door_time, click)
		if (not calib):
			tools.start_calb_code(door_list, index, click)
		else:
			break
	

	if(not tools.schedule(list_sch_c, True)):
		print("Schedule Fail")
		tools.exit()

	ship(ship_b, cross_b, True)

	if(not tools.schedule(list_sch_d)):
		print("Schedule Fail")
		tools.exit()

keyborad_events.start_listener()
#starting()

#tools.calibrate(2)
#tools.exit()
#tools.schedule(list_sch_c, True)
while(True):
	#schedule(list_sch_test)
	if(rut_a): rutine_a()

	while(True):
		idx = mining(ore_list, idx)
		if(idx is False):
			break

	rutine_b()



