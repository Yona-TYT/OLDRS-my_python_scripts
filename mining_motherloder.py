import pyautogui

from time import sleep

import keyborad_events

import tools

import drops

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

list_sch_d =	[	{"x":582, "y":682, "clic":0, "t":3.5, "c_r": 0, "c_i":1}, {"x":582, "y":648, "clic":0, "t":1, "c_r": 0, "c_i":2}	]

list_sch_e =	[	{"x":513, "y":283, "clic":0, "t":5.5, "c_r": 0, "c_i":1}, {"x":635, "y":485, "clic":0, "t":2, "c_r": 0, "c_i":1}	]

list_sch_bank_a =	[	{"x":793, "y":377, "clic":0, "t":3.5, "c_r": 0, "c_i":1}	]

list_sch_bank_b =	[	{"x":324, "y":619, "clic":0, "t":3.5, "c_r": 0, "c_i":1}	]


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

#Eperimento

code_list_a = [{"x":467, "y": 558}, {"x":513, "y": 602}, {"x":503, "y": 738}, {"e_x":485, "e_y":446}]
code_list_b = [{"x":316, "y": 512}, {"x":278, "y": 683}, {"x":293, "y": 458}, {"e_x":484, "e_y":425}]
code_list_c = [{"x":311, "y": 456}, {"x":422, "y": 556}, {"x":530, "y": 710}, {"e_x":510, "e_y":420}]
code_list_d = [{"x":347, "y": 471}, {"x":580, "y": 740}, {"x":463, "y": 579}, {"e_x":557, "e_y":440}]
code_list_e = [{"x":606, "y": 626}, {"x":452, "y": 490}, {"x":609, "y": 773}, {"e_x":582, "e_y":461}]
code_list_f = [{"x":341, "y": 490}, {"x":584, "y": 602}, {"x":785, "y": 348}, {"e_x":610, "e_y":480}]
code_list_g = [{"x":791, "y": 372}, {"x":509, "y": 655}, {"x":378, "y": 531}, {"e_x":610, "e_y":506}]
code_list_h = [{"x":663, "y": 478}, {"x":478, "y": 514}, {"x":655, "y": 385}, {"e_x":480, "e_y":465}]
code_list_i = [{"x":606, "y": 683}, {"x":357, "y": 534}, {"x":762, "y": 376}, {"e_x":583, "e_y":511}]
code_list_j = [{"x":750, "y": 500}, {"x":424, "y": 558}, {"x":556, "y": 537}, {"e_x":557, "e_y":484}]
code_list_k = [{"x":783, "y": 497}, {"x":608, "y": 710}, {"x":445, "y": 556}, {"e_x":581, "e_y":535}]
code_list_l = [{"x":721, "y": 501}, {"x":270, "y": 536}, {"x":508, "y": 654}, {"e_x":531, "e_y":486}]
code_list_o = [{"x":509, "y": 439}, {"x":768, "y": 422}, {"x":351, "y": 580}, {"e_x":582, "e_y":507}]
code_list_p = [{"x":609, "y": 741}, {"x":513, "y": 333}, {"x":486, "y": 575}, {"e_x":580, "e_y":437}]

code_list = [
				{"list": code_list_a}, {"list": code_list_b}, {"list": code_list_c},
				{"list": code_list_d}, {"list": code_list_e}, {"list": code_list_f},
				{"list": code_list_g}, {"list": code_list_h}, {"list": code_list_i},
				{"list": code_list_j}, {"list": code_list_k}, {"list": code_list_l},
 				{"list": code_list_o}, {"list": code_list_p}
			]


mark_list_a = [{"x":514, "y": 374}, {"x":761, "y": 355}, {"x":776, "y": 447}, {"e_x":530, "e_y":488}]
mark_list_b = [{"x":554, "y": 742}, {"x":511, "y": 554}, {"x":329, "y": 471}, {"e_x":487, "e_y":443}]
mark_list_c = [{"x":339, "y": 531}, {"x":420, "y": 580}, {"x":679, "y": 318}, {"e_x":462, "e_y":442}]
mark_list_d = [{"x":668, "y": 847}, {"x":840, "y": 470}, {"x":490, "y": 534}, {"e_x":582, "e_y":508}]

mark_list_e = [{"x":0, "y": 0}, {"x":0, "y": 0}, {"x":0, "y": 0}, {"e_x":0, "e_y":0}]
mark_list_ae = [{"x":0, "y": 0}, {"x":0, "y": 0}, {"x":0, "y": 0}, {"e_x":0, "e_y":0}]
mark_list_ab = [{"x":0, "y": 0}, {"x":0, "y": 0}, {"x":0, "y": 0}, {"e_x":0, "e_y":0}]
mark_list_ac = [{"x":0, "y": 0}, {"x":0, "y": 0}, {"x":0, "y": 0}, {"e_x":0, "e_y":0}]

mark_list = [
				{"list": mark_list_a}, {"list": mark_list_b}, {"list": mark_list_c}, {"list": mark_list_d}

			]

mine_list_a = [{"x":514, "y": 374}, {"x":761, "y": 355}, {"x":776, "y": 447}, {"e_x":580, "e_y":488}]
mine_list_b = [{"x":554, "y": 742}, {"x":511, "y": 554}, {"x":329, "y": 471}, {"e_x":535, "e_y":443}]
mine_list_c = [{"x":339, "y": 531}, {"x":420, "y": 580}, {"x":679, "y": 318}, {"e_x":510, "e_y":442}]
mine_list_d = [{"x":668, "y": 847}, {"x":840, "y": 470}, {"x":490, "y": 534}, {"e_x":635, "e_y":508}]

mine_list_e = [{"x":563, "y": 243}, {"x":483, "y": 440}, {"x":367, "y": 510}, {"e_x":511, "e_y":422}]
mine_list_f = [{"x":383, "y": 721}, {"x":212, "y": 415}, {"x":171, "y": 762}, {"e_x":505, "e_y":460}]
mine_list_g = [{"x":260, "y": 685}, {"x":638, "y": 505}, {"x":205, "y": 435}, {"e_x":505, "e_y":485}]
mine_list_h = [{"x":377, "y": 436}, {"x":679, "y": 683}, {"x":618, "y": 755}, {"e_x":522, "e_y":653}]
mine_list_hh = [{"x":0, "y": 0}, {"x":0, "y": 0}, {"x":0, "y": 0}, {"e_x":0, "e_y":0}]

mine_list = [
				{"list": mine_list_a}, {"list": mine_list_b}, {"list": mine_list_c}, {"list": mine_list_d}

			]


	
# Centro de la pantalla para mining
cen_min_x, cen_min_y = 580, 490
def mining(c_list, idx):
	cal_x, cal_y = 0 , 0
	idx_a = idx
	idx_b = 1
	gold_plus_x, gold_plus_y = 65 , 33
	delay = 3
	try_c = 0
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

			if(try_c > 30):

				px_cent = pyautogui.pixel(cent_x, cent_y)
				if (px_cent.red == 0 and px_cent.green == 0 and px_cent.blue == 0):
					print("-- Find Mining Fail (mine): ", try_c)
					calib = tools.start_calb_code(mine_list)
					return 0

			try_c = try_c + 1

			inven_check_x, inven_check_y = 1125, 835
			px_inv = pyautogui.pixel(inven_check_x, inven_check_y)
			if (px_inv.red !=62 and px_inv.green !=53 and px_inv.blue !=41):

				px_calib = pyautogui.pixel(cent_x, cent_y)
				if (px_calib.red !=0 or px_calib.green !=0 or px_calib.blue !=0):
					sleep(4)
					px_calib = pyautogui.pixel(cent_x, cent_y)
					if (px_calib.red !=0 or px_calib.green !=0 or px_calib.blue !=0):
						tools.start_calb_code(code_list)
						return 0

				print("-- Calib Mining (mark): ", try_c)
				calib = tools.start_calb_code_idx(mark_list, idx_a, delay)
				if(not calib):
					tools.start_calb_code(mark_list)

				print("Exit Mining x: %d , y: %d Delay: %f s  Px IV: %s" % (c_list[idx_a][0]["x"], c_list[idx_a][0]["y"], delay, px_inv))
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
						tools.start_calb_code(code_list)
						return 0

				px_esp = pyautogui.pixel(esp_x, esp_y)
				if (px_esp.red == 0 and px_esp.green == 255 and px_esp.blue == 0):
					sleep(0.5)
					pyautogui.moveTo(esp_x+22, esp_y-5)
					pyautogui.click(esp_x+22, esp_y-5)
					sleep(0.5)

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

					
					px_calib = pyautogui.pixel(cent_x, cent_y)
					if (px_calib.red !=0 or px_calib.green !=0 or px_calib.blue !=0):
						sleep(4)
						px_calib = pyautogui.pixel(cent_x, cent_y)
						if (px_calib.red !=0 or px_calib.green !=0 or px_calib.blue !=0):
							tools.start_calb_code(code_list)
							return 0

					repeat = repeat + 1

				return i
			idx_b = idx_b +1

		px_calib = pyautogui.pixel(cent_x, cent_y)
		if (px_calib.red !=0 or px_calib.green !=0 or px_calib.blue !=0):
			tools.start_calb_code(code_list)
			return 0


	return 0

def bank():
	print("Bag to bank...")
	clic_delay = 0.5
	bag_x, bag_y = 552, 491
	bank_x, bank_y = 608, 481
	bank_drop_x, bank_drop_y = 549, 511
	inven_check_x, inven_check_y = 1125, 835
	depx_x, depx_y = 685, 280
	result = True

	sleep(clic_delay)
	sleep(clic_delay)
	pyautogui.moveTo(bag_x, bag_y)
	sleep(clic_delay)
	pyautogui.click()

	sleep(clic_delay)
	tools.schedule(list_sch_bank_a, True)
	sleep(0.3)

	px_inv = pyautogui.pixel(inven_check_x, inven_check_y)
	sleep(0.3)
	if (px_inv.red ==62 and px_inv.green ==53 and px_inv.blue ==41):
		result = False

	pyautogui.moveTo(bank_x, bank_y)
	sleep(clic_delay)
	pyautogui.click()
	sleep(1.5)

	pyautogui.moveTo(bank_drop_x, bank_drop_y)
	sleep(clic_delay)
	pyautogui.click()

	if(result):
		sleep(0.5)
		tools.schedule(list_sch_bank_b, True)
		sleep(0.5)

	else:
		sleep(1.5)
		pyautogui.moveTo(depx_x, depx_y)
		sleep(clic_delay)
		pyautogui.click()
		sleep(clic_delay)

	return result

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
	sack_check_x, sack_check_y = 74, 119

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
			px_sack = pyautogui.pixel(sack_check_x, sack_check_y)
			if (px_sack.red ==255 and px_sack.green ==0 and px_sack.blue ==0):
				return True
			break

		if(count > c_max):
			pyautogui.moveTo(clc_a_x, clc_a_y)
			sleep(clic_delay)
			pyautogui.click()
			sleep(1)
			px_inv = pyautogui.pixel(inven_check_x, inven_check_y)
			sleep(0.3)
			if (px_inv.red ==62 and px_inv.green ==53 and px_inv.blue ==41):
				px_sack = pyautogui.pixel(sack_check_x, sack_check_y)
				if (px_sack.red ==255 and px_sack.green ==0 and px_sack.blue ==0):
					return True
				break

			print("Wait... 30")
			sleep(30)
			count = 0
			if(tryy == 3):
				idx = 27
				drops.drop_only(idx)
			if(tryy > 5):
				tools.exit()

			tryy = tryy + 1
		count = count+ 1

	return False

def rutine_c():
	print("Up Ladder")
	clic_delay = 0.5
	p_x, p_y = 45, 33
	ladd_x, ladd_y = 743, 439
	pyautogui.moveTo(ladd_x, ladd_y)
	sleep(clic_delay)
	px = pyautogui.pixel(ladd_x + p_x, ladd_y + p_y)
	if (px.green ==255 and px.blue ==255):
		r_sch = tools.schedule(list_sch_b, True)
		if(not r_sch):
			print("Schedule Fail")
			tools.exit()
	else:
		print("NoT find Ladder...")
		tools.exit()

def rutine_d():
	print("Rutine D")
	r_sch = tools.schedule(list_sch_d, True)
	if(not r_sch):
		print("Schedule Fail")
		tools.exit()

	print("...")
	sleep(0.7)
	count = 0
	while(True):
		if(not bank()):
			break

		if(count > 6):
			break

		count = count + 1

	print("Up Ladder")
	clic_delay = 0.5
	p_x, p_y = 45, 33
	ladd_x, ladd_y = 512, 275
	pyautogui.moveTo(ladd_x, ladd_y)
	sleep(clic_delay)
	px = pyautogui.pixel(ladd_x + p_x, ladd_y + p_y)
	if (px.green ==255 and px.blue ==255):
		r_sch = tools.schedule(list_sch_e, True)
		if(not r_sch):
			print("Schedule Fail")
			tools.exit()
	else:
		print("NoT find Ladder...")
		tools.exit()
	
	
keyborad_events.start_listener()


#tools.calibrate(2)

#rutine_d()

count = 0

#rutine_d()

while(True):
	keyborad_events.main_events()
	rutine_c()

	while(True):
		idx = mining(ore_list, idx)
		if(idx is False):
			break

	rutine_a()
	if(	rutine_b() or count >= 5):
		rutine_d()
		count = 0
		while(True):
			idx = mining(ore_list, idx)
			if(idx is False):
				break
		rutine_a()
		rutine_b()



	count = count + 1


