import pyautogui

from time import sleep

import sys

import keyborad_events

import drops

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
					{"x":53, "y":542, "clic":0, "t":4}, {"x":61, "y":619, "clic":0, "t":4},
					{"x":71, "y":571, "clic":0, "t":4}, {"x":51, "y":458, "clic":0, "t":4},
					{"x":323, "y":248, "clic":0, "t":4}, {"x":541, "y":275, "clic":0, "t":4}, 
					{"x":411, "y":296, "clic":0, "t":4}, {"x":320, "y":377, "clic":0, "t":4}
				]




list_sch_b =	[
					{"x":921, "y":478, "clic":0, "t":4}, {"x":707, "y":687, "clic":0, "t":4},
					{"x":860, "y":804, "clic":0, "t":4}, {"x":646, "y":840, "clic":0, "t":4},
					{"x":901, "y":780, "clic":0, "t":4}, {"x":1094, "y":513, "clic":0, "t":4}, 
					{"x":1063, "y":404, "clic":0, "t":4}, {"x":929, "y":395, "clic":0, "t":4},
					{"x":754, "y":464, "clic":0, "t":2}, {"x":924, "y":455, "clic":0, "t":4}
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

		else:
			pyautogui.click()

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

panel_siz = 120

rut_a = 1




iterate_list = [{"siz":6, "r":2, "nr":0}, {"siz":2, "r":0, "nr":3}, {"siz":6, "r":3, "nr":2}]

fish_list =	[	#0 ------------------------------------------------------------------------------
					{"x":580, "y":510, "i":0}, 
					{"x":605, "y":510, "i":1}, 
					{"x":631, "y":510, "i":2}, 
					{"x":655, "y":510, "i":3}, 
					{"x":680, "y":510, "i":4}, 
					{"x":705, "y":510, "i":5}, 
					{"x":705, "y":510, "i":6}, 
					{"x":710, "y":530, "i":7},
					{"x":710, "y":530, "i":8},
					{"x":690, "y":530, "i":9}, 
					{"x":662, "y":530, "i":10}, 
					{"x":634, "y":530, "i":11}, 
					{"x":610, "y":530, "i":12},
					{"x":583, "y":530, "i":13}
			]


idx = 0
point = 0
all_res = {"i":0, "p":0 }

def experimento2(c_list, ite_list, idx, point):


	all_res = {"i":idx, "p":point }
	print("-- Debug.. x: %d, y: %d, Idx: %d--  Pixel %s" % (0, 0, idx, 0))

	# Inventary list
	count_idx = 0

	flag_fish = 0

	while(True):

		if(flag_fish == 0):
			sea_a_x, sea_a_y = 591, 510
			fa_cent_x, fa_cent_y = 578, 518
			px_const = pyautogui.pixel(sea_a_x, sea_a_y)
			if(px_const.blue < 90 and px_const.blue !=0):
				flag_fish = 1
				print("-- NOT Sea...  count %d --  Pixel %s flag %d" % ( 0, px_const, flag_fish))
				continue

			print("-- Is Sea...  count %d --  Pixel %s" % ( 0, px_const))
			res = is_fishing(c_list, idx, point, fa_cent_x, fa_cent_y, sea_a_x, sea_a_y, px_const, count_idx)
			if(res and res["i"] is False):
				drops.clear_save_dr()
				return res

			if(res == 0):
				flag_fish = 1
				print("-- NOT Fish...  count %d --  Pixel %s flag %d" % ( 0, px_const, flag_fish))
				continue

		if(flag_fish == 1):
			sea_b_x, sea_b_y = 590, 462
			fb_cent_x, fb_cent_y = 578, 463
			px_const = pyautogui.pixel(sea_b_x, sea_b_y)
			if(px_const.blue < 90 and px_const.blue !=0):
				flag_fish = 2
				print("-- NOT Sea...  count %d --  Pixel %s flag %d" % ( 0, px_const, flag_fish))
				continue

			print("-- Is Sea...  count %d --  Pixel %s" % ( 0, px_const))
			res = is_fishing(c_list, idx, point, fb_cent_x, fb_cent_y, sea_b_x, sea_b_y, px_const, count_idx)
			if(res and res["i"] is False):
				drops.clear_save_dr()
				pyautogui.moveTo(581, 510)
				sleep(0.5)
				pyautogui.click(581, 510)
				sleep(3)
				flag_fish = 0
				return res

			if(res == 0):
				flag_fish = 2
				print("-- NOT Fish...  count %d --  Pixel %s flag %d" % ( 0, px_const, flag_fish))
				continue

		if(flag_fish == 2):
			pyautogui.moveTo(581, 510)
			sleep(0.5)
			pyautogui.click(581, 510)
			flag_fish = 0
			continue

	print("-- Debug...  count_idx %d --  flag %d" % ( count_idx, flag_fish))
	return res

	

def is_fishing(c_list, idx, point, fish_cent_x, fish_cent_y, sea_x, sea_y, px_const, count_idx):
	count = 0
	exit_count = 0
	siz = 7

	incr_x = 26
	incr_y = 21

	fish_plus_x, fish_plus_y = 56, 33

	fish_inc = 0
	fish_dir = (-1)

	t = 1
	clic_delay = 0.8
	if(px_const.blue > 90 ):
			while (count <= siz):
				px_const = pyautogui.pixel(sea_x, sea_y)
				if(px_const.blue < 90 and px_const.blue !=0):
					print("-- NOT Sea...  count %d --  Pixel %s" % ( count, px_const))
					return all_res
					break
					
				keyborad_events.main_events()
				if (invent_full(c_list[idx]["x"], c_list[idx]["y"]) == 1):
					all_res["i"] = False
					return all_res
					break
				x, y, = fish_cent_x + fish_inc, fish_cent_y
				#pyautogui.moveTo(x, y)
				sleep(0.2)

				px_fish = pyautogui.pixel(x, y)
				print("-- Find Fish... x: %d, y: %d, count %d --  Pixel %s" % (x, y, count, px_fish))

				if(px_fish.blue < 105 and px_fish.blue !=0):
					if(fish_dir):
						t = count 
					else:
						t = (count) * (-1)

					pyautogui.moveTo(x, y)
					sleep(0.2)
					pyautogui.click(button='right')
					sleep(0.5)
					pyautogui.click(x, y+45)

					print("Delay long...: %d, y: %d, count %d  time: %d" % (x, y, count, t))
					sleep(clic_delay+t)

					pyautogui.moveTo(fish_cent_x, fish_cent_y)
					sleep(0.5)
					px_fish = pyautogui.pixel(fish_cent_x+fish_plus_x, fish_cent_y+fish_plus_y)
					print("Fishing... plus_x: %d, plus_y: %d,  count %d --  Pixel %s" % (x, y, count, px_fish))
					t_fish = 2
					while(px_fish.red == 255 and px_fish.green == 255 and px_fish.blue == 0):
						keyborad_events.main_events()
						print("Fishing... plus_x: %d, plus_y: %d,  count %d --  Pixel %s" % (x, y, count, px_fish))


						res = invent_full(c_list[count_idx]["x"], c_list[count_idx]["y"])
						if ( res == 1):
							all_res["i"] = False
							return all_res
							break


						pyautogui.moveTo(fish_cent_x, fish_cent_y)
						sleep(0.2)
						px_fish = pyautogui.pixel(fish_cent_x+fish_plus_x, fish_cent_y+fish_plus_y)
						sleep(0.2)
						px_is_fish = pyautogui.pixel(63, 101)
						sleep(0.2)
						if (px_is_fish.red != 0 or px_is_fish.green != 255 or px_is_fish.blue != 0):
							if (px_fish.red == 255 and px_fish.green == 255 and px_fish.blue == 0):
							#	c = get_ribi(x, y, r)
							#	pyautogui.moveTo(x, y)
							#	sleep(0.2)
								pyautogui.click(button='right')
								sleep(0.5)
								pyautogui.click(fish_cent_x, fish_cent_y+45)

								sleep(0.5)
								pyautogui.moveTo(fish_cent_x, fish_cent_y)
								sleep(t_fish)
								t_fish = t_fish + t_fish

						else:
							t_fish = 2


				fish_inc = fish_inc + incr_x*(fish_dir)
				count = count + 1
				exit_count = exit_count + 1
				if(exit_count >= 8):
					return 0
				if (px_fish.red == 0 and px_fish.green == 0 and px_fish.blue == 0):
					if(count < 7):
						print("-- Find Fish.")
						count = siz - (siz - count)
						fish_dir = 1
						fish_inc = 0

						continue

					break
	
	return all_res

def invent_full(x, y):

	inven_check_x, inven_check_y = 256, 817
	full_r, full_g, full_b = 210, 193, 156
	px_inv = pyautogui.pixel(inven_check_x, inven_check_y)
	if (px_inv.red ==full_r and px_inv.green ==full_g and px_inv.blue ==full_b):
		index = 1
		color = {"red":155, "green":98, "blue":166}
		nr = drops.drop_rgb(index, color, True)

		#Fishing Exit
		if(nr<1):
			incr_x = 26
			incr_y = 21
			# Centro de la pantalla
			cent_x, cent_y = 585, 490

			count = 0
			siz = 7
			walk_incr = -26
			while (count <= siz):
				x, y, = cent_x + walk_incr, cent_y
				#pyautogui.moveTo(x, y)
				sleep(0.2)

				px_walk = pyautogui.pixel(x, y)
				sleep(0.2)
				if(px_walk.red ==0 and px_walk.green ==0 and px_walk.blue ==0):
					pyautogui.moveTo(x, y)
					sleep(0.8)
					pyautogui.click()
					print("Exit Fishing Delay... x %d , y %d" % (x,  y))
					sleep(0.5)

					count = 0
					count_max = 90
					px_cent = pyautogui.pixel(cent_x, cent_y)
					sleep(0.2)
					while (px_cent.red !=0 or px_cent.green !=0 or px_cent.blue !=0):
						keyborad_events.main_events()
						px_cent = pyautogui.pixel(cent_x, cent_y)
						#pyautogui.moveTo(cent_x, cent_y)

						count = count + 1
						print("Schedule... Count %d , XY: %d,%d -- Pixel %s" % (count, x, y, px_cent))
						if(count > count_max):
							return False

					return 1
					break

				walk_incr = walk_incr - incr_x * (-1)


			return 1
		return 2

	return 0



def bank():
	clic_delay = 0.5
	bank_x, bank_y = 578, 453
	bank_drop_x, bank_drop_y = 353, 323
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

	while(True):
		for c in c_list:
			x, y, opt = c["x"], c["y"], c["opt"]
			keyborad_events.main_events()
			px_fire = pyautogui.pixel(x, y)
			print("Find Fire Abajo... Coord %d,%d :: Pixel %s" % (x, y, px_fire))
			if(px_fire.red >= 180 and px_fire.green >= 128 and px_fire.blue <= 60):
				return x, y, opt

	print("Fail find fire!!")
	sys.exit()
	return False


def wait_cook():
	sleep(2)
	is_cook_a_x, is_cook_a_y = 89, 103
	is_cook_b_x, is_cook_b_y = 89, 162

	px_is_cook_a = pyautogui.pixel(is_cook_a_x, is_cook_a_y)
	px_is_cook_b = pyautogui.pixel(is_cook_b_x, is_cook_b_y)

	while(px_is_cook_a.green == 255 or px_is_cook_b.green == 255):
		keyborad_events.main_events()
		print("It's Cooking...")
		px_is_cook_a = pyautogui.pixel(is_cook_a_x, is_cook_a_y)
		px_is_cook_b = pyautogui.pixel(is_cook_b_x, is_cook_b_y)

	return True

def cooking():
	fire_x, fire_y, opt = get_fire()
	clic_delay = 0.5

	while(True):
		keyborad_events.main_events()
		pyautogui.moveTo(fire_x, fire_y)
		sleep(clic_delay)
		pyautogui.click(fire_x, fire_y)
		sleep(1)
		
		cook_x, cook_y = 194, 825
		px = pyautogui.pixel(cook_x, cook_y)
		if(px.red <= 120 and px.green <= 90 and px.blue <= 70):
			pyautogui.moveTo(cook_x, cook_y)
			sleep(clic_delay)
			pyautogui.click(cook_x, cook_y)
			wait_cook()
			continue

		cook_x, cook_y = 194, 825
		px = pyautogui.pixel(cook_x, cook_y)
		if(px.red >= 160 and px.green <= 50 and px.blue <= 15):
			pyautogui.moveTo(cook_x, cook_y)
			sleep(clic_delay)
			pyautogui.click(cook_x, cook_y)
			wait_cook()
			continue

		cook_x, cook_y = 253, 825
		px = pyautogui.pixel(cook_x, cook_y)
		if(px.red <= 175 and px.green <= 150):
			pyautogui.moveTo(cook_x, cook_y)
			sleep(clic_delay)
			pyautogui.click(cook_x, cook_y)
			wait_cook()
			continue

		cook_x, cook_y = 314, 825
		px = pyautogui.pixel(cook_x, cook_y)
		if(px.red >= 70 and px.green <= 100 and px.blue >= 50):
			pyautogui.moveTo(cook_x, cook_y)
			sleep(clic_delay)
			pyautogui.click(cook_x, cook_y)
			wait_cook()
			continue


		break
	
def rutine_a():
	bank()
	if(not schedule(list_sch_a)):
		print("Schedule Fail")
		sys.exit()
	##index = 2
	##drops.drop_only(index)
	##if(not schedule(list_sch_a)):


def rutine_b():
	if(not schedule(list_sch_b)):
		print("Schedule Fail")
		sys.exit()



keyborad_events.start_listener()
#starting()

while(True):


	index = 4
	color = {"red":166, "green":105, "blue":177}
	#nr = drops.drop_rgb(index, color)
	#print("Drop Number.... x: %d, y: %d -- Index %d --  Drop %d" % (0, 0, 0, nr))
	#drops.drop_debug(index)

	#rutine_a()
	while(True):
		all_res = experimento2(fish_list, iterate_list, all_res["i"], all_res["p"])
		if(all_res["i"] is False):
			break

	rutine_b()

	#keyborad_events.main_events()
	#schedule(list_sch_test)
	#if(rut_a): rutine_a()
	#rutine_a()
	#while(True):
		#idx = fishing(fish_list, idx)
		#if(idx is False):
			#break

	#rutine_b()



