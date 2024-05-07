import pyautogui

from time import sleep

import sys

import keyborad_events

import drops

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

list_sch_a =	[	{"x":673, "y":463, "clic":0, "t":3.5, "c_r": 1, "c_i":-1}	]


list_sch_walk =	[	{"x":635, "y":536, "clic":2, "t":3.5, "c_r": 1, "c_i":0}	]

list_sch_b =	[	{"x":723, "y":504, "clic":0, "t":3.5, "c_r": 1, "c_i":0}	]


idx = 0

fish_list =	[
				[	#0 ------------------------------------------------------------------------------
					{"x":490, "y":520, "r":0, "i":0, "t":3, "lv": 0}, {"x":608, "y":506, "r":1, "i":1, "t":2.2, "lv": 0},
					{"x":607, "y":533, "r":1, "i":2, "t":2.2, "lv": 0}, {"x":411, "y":759, "r":1, "i":3, "t":4, "lv": 0}, 
					{"x":414, "y":794, "r":1, "i":4, "t":6, "lv": 0}
				],
				[	#1 ------------------------------------------------------------------------------
					{"x":492, "y":491, "r":0, "i":0, "t":3, "lv": 0}, {"x":605, "y":509, "r":1, "i":2, "t":2.2, "lv": 0},
					{"x":427, "y":718, "r":1, "i":3, "t":4, "lv": 1}, {"x":420, "y":758, "r":1, "i":4, "t":2.2, "lv": 1},
					{"x":610, "y":464, "r":1, "i":0, "t":2.2, "lv": 0}
				],
				[	#2 ------------------------------------------------------------------------------
					{"x":494, "y":463, "r":0, "i":0, "t":4, "lv": 0}, {"x":427, "y":681, "r":1, "i":3, "t":4, "lv": 1},
					{"x":423, "y":721, "r":1, "i":4, "t":2.2, "lv": 1}, {"x":605, "y":442, "r":1, "i":0, "t":3, "lv": 0},
					{"x":609, "y":470, "r":1, "i":1, "t":2.2, "lv": 0}
				],
				[	#3 ------------------------------------------------------------------------------
					{"x":655, "y":314, "r":0, "i":0, "t":8, "lv": 0}, {"x":609, "y":518, "r":1, "i":4, "t":2.2, "lv": 0},
					{"x":734, "y":311, "r":1, "i":0, "t":4, "lv": 0}, {"x":735, "y":334, "r":1, "i":1, "t":4, "lv": 0},
					{"x":738, "y":346, "r":1, "i":2, "t":4, "lv": 0}
				],
				[	#4 ------------------------------------------------------------------------------
					{"x":654, "y":287, "r":0, "i":0, "t":8, "lv": 0}, {"x":729, "y":295, "r":1, "i":0, "t":4, "lv": 1},
					{"x":731, "y":310, "r":1, "i":1, "t":4, "lv": 1}, {"x":732, "y":328, "r":1, "i":2, "t":4, "lv": 1},
					{"x":605, "y":465, "r":1, "i":3, "t":2.2, "lv": 0}
				]
		]

# Centro de la pantalla para Fishing
cen_fish_x, cen_fish_y = 580, 490
def fishing(c_list, idx):
	cal_x, cal_y = 0 , 0
	idx_a = idx
	idx_b = 1
	fish_plus_x, fish_plus_y = 56 , 33
	delay = 3
	inven_check_x, inven_check_y = 1125, 839
	while (True):
		print("Debug... Idx ab: %d, %d " % ( idx_a, idx_b))
		if(idx_b == len(c_list[0])):
			idx_b = 1
			lev_count = 0

		lev_count = 0
		while (idx_b < len(c_list[idx_a])):
			keyborad_events.main_events()
			c_x , c_y, r, i, lv = c_list[idx_a][idx_b]["x"] + cal_x, c_list[idx_a][idx_b]["y"]+ cal_y, c_list[idx_a][idx_b]["r"], c_list[idx_a][idx_b]["i"], c_list[idx_a][idx_b]["lv"]
			px = pyautogui.pixel(c_x, c_y)
			px_inv = pyautogui.pixel(inven_check_x, inven_check_y)
			sleep(0.2)
			print("Check Inv... Count %d, Pixel %s" % (idx_a, px_inv))
			if (px_inv.red !=62 and px_inv.green !=53 and px_inv.blue !=41):
				delay = 5
				exit_x, exit_y = c_list[idx_a][0]["x"], c_list[idx_a][0]["y"]
				pyautogui.moveTo(exit_x, exit_y)
				sleep(0.8)
				pyautogui.click()
				sleep(delay)

				print("Exit Fishing Delay... idx_a: %d :: x %d, y %d"% (idx_a, exit_x, exit_y))
				sleep(0.5)
				return False

			print("-- Find Fish... x: %d, y: %d, Idx ab: %d, %d --  Pixel %s" % (c_x, c_y, idx_a, idx_b, px))

			if(lv <= idx_b and px.blue < 90):
				c = get_ribi(c_x, c_y, r)
				pyautogui.moveTo(c["x"], c["y"])
				pyautogui.click(c["x"], c["y"])
				c = get_ribi(cen_fish_x, cen_fish_y, c["r"])

				dlay = c_list[idx_a][idx_b]["t"]
				#print("Waiting.. Delay : %f s  Coord: %d, %d" % (dlay, c_x, c_y))
				sleep(dlay)

				count = 0
				count_max = 30
				px_cent = pyautogui.pixel(cen_fish_x, cen_fish_y)
				while (px_cent.red !=0 or px_cent.green !=0 or px_cent.blue !=0):
					keyborad_events.main_events()
					px_cent = pyautogui.pixel(cen_fish_x, cen_fish_y)
					#sleep(0.2)
					pyautogui.moveTo(cen_fish_x, cen_fish_y)
					count = count + 1
					print("Chag Fish... Count %d, Pixel %s" % (count, px_cent))

					if(count > count_max):
						if(not tools.calibrate(1)):
							print("Schedule Fail")
							tools.exit()
						else:
							if(not tools.schedule(list_sch_b, False)):
								print("Fail find fire!!")
								tools.exit()
								return False
							return 0

				pyautogui.moveTo(c["x"], c["y"])
				pyautogui.click(c["x"], c["y"])
				p_x, p_y = 40, 33
				while(True):
					keyborad_events.main_events()
					pyautogui.moveTo(c["x"], c["y"])
					px_inv = pyautogui.pixel(inven_check_x, inven_check_y)
					if (px_inv.red !=62 and px_inv.green !=53 and px_inv.blue !=41):
						break

					px_fish = pyautogui.pixel(c["x"]+p_x, c["y"]+p_y)
					if(px_fish.red !=255 and px_fish.green !=255 and px_fish.blue !=0):
						break

					print("Fishing... Coord x: %d, y: %d, Idx ab: %d, %d --  Pixel %s" % (c["x"], c["y"], idx_a, idx_b, px_fish))

				return i

			idx_b = idx_b +1

		print("Lev Count... nr ", lev_count)
		lev_count = lev_count + 1
	return 0
	#print("Fishing... Count %d, Pixel %s" % (c_list[0][0]["x"], c_list[0][0]["y"]))

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


def get_fire():
	c_list = [{"x":577, "y":509, "opt": 0}, {"x":577, "y":503, "opt": 0}, {"x":602, "y":488, "opt": 1}]
	p_x, p_y = 40, 33
	tryy = 0
	while(True):
		for c in c_list:
			x, y, opt = c["x"], c["y"], c["opt"]
			#Debug------------------------------------
			pyautogui.moveTo(x, y)
			sleep(0.2)
			#Debug------------------------------------
			keyborad_events.main_events()
			px_fire = pyautogui.pixel(x+p_x, y+p_y)
			print("Find Fire ... Coord %d,%d try: %d :: Pixel %s" % (x, y,tryy, px_fire))
			if(px_fire.red <= 40 and px_fire.green >= 200 and px_fire.blue >= 200):
				return x, y, opt

			if(tryy>5):
				if(not tools.calibrate(1)):
					print("Schedule Fail")
					tools.exit()
				else:
					if(not tools.schedule(list_sch_walk, False)):
						print("Fail find fire!!")
						tools.exit()
						return False
					tryy = 0
					continue

		tryy = tryy +1

	print("Fail find fire!!")
	tools.exit()
	return False


def wait_cook():
	sleep(2)
	is_cook_a_x, is_cook_a_y = 89, 103
	is_cook_b_x, is_cook_b_y = 89, 162

	px_is_cook_a = pyautogui.pixel(is_cook_a_x, is_cook_a_y)
	px_is_cook_b = pyautogui.pixel(is_cook_b_x, is_cook_b_y)

	tryy = 0
	while(True):	
		keyborad_events.main_events()
		print("It's Cooking... try: ", tryy)
		px_is_cook_a = pyautogui.pixel(is_cook_a_x, is_cook_a_y)
		px_is_cook_b = pyautogui.pixel(is_cook_b_x, is_cook_b_y)

		if(px_is_cook_a.green != 255 and px_is_cook_b.green != 255):
			break

		if(tryy>500):
			if(not tools.calibrate(1)):
				print("Schedule Fail")
				tools.exit()
			else:
				if(not tools.schedule(list_sch_walk, False)):
					print("Fail Cooking!!")
					tools.exit()
				tryy = 0
				continue
			
		tryy = tryy +1 

	return True

def cooking():
	fire_x, fire_y, opt = get_fire()
	clic_delay = 0.5
	clic_a_x, clic_a_y = 503, 858

	tryy = 0
	try2 = 0
	while(True):
		keyborad_events.main_events()
		print("Setting Cooking... try: ", tryy)

		px_check = pyautogui.pixel(clic_a_x, clic_a_y)
		sleep(0.2)
		if(px_check.red <= 160 or px_check.green <= 140 or px_check.blue >= 140):
			print("A try: ", try2)
			if(try2 > 30):
				tools.exit()

			pyautogui.moveTo(fire_x, fire_y)
			sleep(clic_delay)
			pyautogui.click(fire_x, fire_y)
			sleep(0.8)
			try2 = try2 + 1
			continue
		elif(px_check.red >= 160 and px_check.green >= 145 and px_check.blue <= 145):
			print("B")
			cook_x, cook_y = 194, 825
			px = pyautogui.pixel(cook_x, cook_y)
			sleep(0.2)
			if(px.red <= 120 and px.green <= 90 and px.blue <= 70):
				pyautogui.moveTo(cook_x, cook_y)
				sleep(clic_delay)
				pyautogui.click(cook_x, cook_y)
				wait_cook()
				continue

			cook_x, cook_y = 194, 825
			px = pyautogui.pixel(cook_x, cook_y)
			sleep(0.2)
			if(px.red >= 160 and px.green <= 50 and px.blue <= 15):
				print("C")
				pyautogui.moveTo(cook_x, cook_y)
				sleep(clic_delay)
				pyautogui.click(cook_x, cook_y)
				wait_cook()
				continue

			cook_x, cook_y = 253, 825
			px = pyautogui.pixel(cook_x, cook_y)
			sleep(0.2)
			if(px.red <= 175 and px.green <= 150):
				print("D")
				pyautogui.moveTo(cook_x, cook_y)
				sleep(clic_delay)
				pyautogui.click(cook_x, cook_y)
				wait_cook()
				continue

			cook_x, cook_y = 314, 825
			px = pyautogui.pixel(cook_x, cook_y)
			sleep(0.2)
			if(px.red >= 70 and px.green <= 100 and px.blue >= 50):
				print("E")
				pyautogui.moveTo(cook_x, cook_y)
				sleep(clic_delay)
				pyautogui.click(cook_x, cook_y)
				wait_cook()
				continue

		if(tryy>0):
			if(not tools.calibrate(1)):
				print("Schedule Fail")
				tools.exit()
			else:
				if(not tools.schedule(list_sch_walk, False)):
					print("Schedule Fail")
					tools.exit()
				tryy = 0
				continue

		tryy = tryy +1

		break
	
def rutine_a():
	cooking()
	index = 2
	drops.drop_only(index)

	r_sch = tools.schedule(list_sch_a, True)
	if(not r_sch):
		print("Schedule Fail")
		tools.exit()
	elif(r_sch == 2):
		tools.schedule(list_sch_b, True)


keyborad_events.start_listener()
#starting()

while(True):
	keyborad_events.main_events()


	while(True):
		idx = fishing(fish_list, idx)
		if(idx is False):
			break

	rutine_a()

	#rutine_b()



