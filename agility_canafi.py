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

	
list_sch_a =	[	{"x":473, "y":340, "clic":0, "t":3.5, "c_r": 1, "c_i":0, "i": -1}, {"x":568, "y":355, "clic":0, "t":3.5, "c_r": 1, "c_i":0, "i": 0},
					{"x":434, "y":485, "clic":0, "t":3.5, "c_r": 1, "c_i":0, "i": 1}, {"x":387, "y":615, "clic":0, "t":3, "c_r": 3, "c_i":-1, "i": 2}, 
					{"x":544, "y":702, "clic":1, "t":3, "c_r": 1, "c_i":0, "i": 3}, {"x":635, "y":564, "clic":1, "t":3, "c_r": 0, "c_i":6, "i": 4}, 
					{"x":970, "y":509, "clic":1, "t":5, "c_r": 1, "c_i":-2, "i": -1}, {"x":579, "y":341, "clic":1, "t":3, "c_r": 1, "c_i":0, "i": -1}
				]

list_mark= [
			{"i":2, "x": 577, "y":  419, "rx": 565, "ry": 417}, {"i":3, "x": 551, "y": 467, "rx": 466, "ry": 501}, {"i":4, "x": 522, "y":  565, "rx": 457, "ry": 529}, 
			{"i":5, "x": 545, "y":  564, "rx": 574, "ry": 595}, {"i":6, "x": 577, "y":  535, "rx": 636, "ry": 508}
		]

list_sch_agi_a =	[
						{"x":734, "y":650, "clic":0, "t":3, "c_r": 3, "c_i":0, "i": -1},
						{"x":970, "y":484, "clic":0, "t":3, "c_r": 3, "c_i":0, "i": -1},
						{"x":868, "y":755, "clic":0, "t":3, "c_r": 3, "c_i":0, "i": -1}
					]

list_sch_agi_b =	[
						{"x":657, "y":323, "clic":0, "t":4, "c_r": 3, "c_i":0, "i": -1}
					]

# Centro de la pantalla para mining
cen_min_x, cen_min_y = 580, 482

def rutine_a():
	calib = True
	r_sch = tools.schedule(list_sch_a, calib, list_mark)
	if(not r_sch):
		print("Schedule Fail")
		tools.exit()
	elif(r_sch == -1):
		tools.schedule(list_sch_agi_a, calib)

	elif(r_sch == -2):
		tools.schedule(list_sch_agi_b, calib)

keyborad_events.start_listener()

#tools.calibrate(2)
#tools.exit()

while(True):
	keyborad_events.main_events()
	rutine_a()

