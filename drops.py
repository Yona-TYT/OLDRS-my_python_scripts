import pyautogui

from time import sleep

import keyborad_events

import tools

from termcolor import colored

screenWidth, screenHeight = pyautogui.size() # Get the size of the primary monitor.
x, y = pyautogui.position() # Get the XY position of the mouse.
px = pyautogui.pixel(x, y)

# Centro de la pantalla
cent_x, cent_y = 700, 495


def tes_plus_cursor(x,y):
	#p_x, p_y = 25 , 39
	pyautogui.moveTo(x, y)
	plus = 0
	while(True):

		px = pyautogui.pixel(x + plus, y)
		print("Plus: %d --- Mouse x:%d,y:%d , Pixel %s" % (plus, x, y, px))
		if (px.red ==221 and px.green ==217 and px.blue ==217):
			return 0

		plus = plus +1

c_list= [
			{"x":993, "y":617}, {"x":1035, "y":617}, {"x":1077, "y":617}, {"x":1119, "y":617},
			{"x":993, "y":653}, {"x":1035, "y":653}, {"x":1077, "y":653}, {"x":1119, "y":653},
			{"x":993, "y":689}, {"x":1035, "y":689}, {"x":1077, "y":689}, {"x":1119, "y":689},
			{"x":993, "y":725}, {"x":1035, "y":725}, {"x":1077, "y":725}, {"x":1119, "y":725},
			{"x":993, "y":761}, {"x":1035, "y":761}, {"x":1077, "y":761}, {"x":1119, "y":761},
			{"x":993, "y":797}, {"x":1035, "y":797}, {"x":1077, "y":797}, {"x":1119, "y":797},

			{"x":993, "y":833}, {"x":1035, "y":833}, {"x":1077, "y":833}, {"x":1119, "y":833}
		]

dr_list = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
def object_drops(c_list, index, color= False, jump = False, one = False):
	global dr_save
	indx = index
	first_x, first_y = 1253, 797
	pyautogui.keyUp('shift')

	print("Drop debug.... x: %d, y: %d -- Index %d" % (0, 0, indx))
	pyautogui.click(first_x, first_y)
	dr_count = 0
	idx_max = len(c_list)
	while (indx < idx_max):
		if (dr_list[indx] == 1):
			indx = indx + 1
			continue

		if(keyborad_events.main_events()):
			return 0
		c_x, c_y = c_list[indx]["x"], c_list[indx]["y"]



		with pyautogui.hold('shift'):
			pyautogui.moveTo(c_x+5, c_y)
			sleep(0.7)
			if(color):
				count = 0
				result = False
				while(count < len(color)):
					keyborad_events.main_events()
					print("--Count", count)
					px = pyautogui.pixel(c_x + color[count]["p_x"], c_y + color[count]["p_y"])
					print("Drop Color debug.... x: %d, y: %d -- Index %d --  Pixel %s" % (c_x, c_y, indx, px))
					sleep(0.2)
					if(px.red == color[count]["red"] and px.green == color[count]["green"] and px.blue == color[count]["blue"]):
						result = True
						print( colored( ("-- Correct Drop Color debug.... x: %d, y: %d -- Index %d --  Pixel %s" % (c_x, c_y, indx, px)), "green" ))
						break

					count = count + 1

				if(result):
					if(jump):
						dr_list[indx] = 1


					if(one and indx >= idx_max):
						print("-- Correct Result")
						return indx

					indx = indx + 1


					continue
			pyautogui.click()
			sleep(0.5)

		if(one):
			print("-- Exit end")
			return indx

		indx = indx + 1
		dr_count = dr_count + 1





	return idx_max


#keyborad_events.start_listener()

def drop_only(idx, jump = False, one = False):
	index = idx
	pyautogui.keyDown('shift')
	keyborad_events.main_events()
	object_drops(c_list, index, jump, one)

def drop_pause(idx, jump = False, one = False):
	index = idx
	pyautogui.keyDown('shift')
	keyborad_events.main_events()
	object_drops(c_list, index, jump, one)
	keyborad_events.main_pause()

def drop_rgb(idx, color, jump = False, one = False):
	index = idx
	pyautogui.keyDown('shift')
	keyborad_events.main_events()
	return object_drops(c_list, index, color, jump, one)

def clear_save_dr():
	dr_list = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

def drop_debug(idx):
	global dr_save
	indx = idx
	c_x, c_y = c_list[indx]["x"], c_list[indx]["y"]
	siz = 10
	count_x = 0
	while (count_x < siz):
		count_y = 0
		while (count_y < siz):
			pyautogui.moveTo(c_x, c_y)
			px = pyautogui.pixel(c_x, c_y)
			print("Color debug.... x: %d, y: %d -- Index %d --  Pixel %s" % (c_x, c_y, indx, px))
			sleep(1)
			count_y = count_y + 1
			c_y = c_y + 1

		count_x = count_x + 1
		c_x = c_x +1

def drop_debug_list(idx, color):
	indx = idx
	first_x, first_y = 1253, 541
	pyautogui.keyUp('shift')

	print("Drop debug.... x: %d, y: %d -- Index %d" % (0, 0, indx))
	pyautogui.click(first_x, first_y)
	dr_count = 0
	while (indx < len(c_list)):
		c_x, c_y = c_list[indx]["x"], c_list[indx]["y"]


		pyautogui.moveTo(c_x+10, c_y)
		sleep(1)
		if(color):
			count = 0
			result = False
			while(count < len(color)):
				keyborad_events.main_events()
				p_x, p_y =  color[count]["p_x"], color[count]["p_y"]
				print("--Count", count)
				px = pyautogui.pixel(c_x + p_x, c_y + p_y)
				print("Drop Color debug.... x: %d, y: %d -- Index %d --  Pixel %s" % (c_x + p_x, c_y + p_y, indx, px))
				sleep(0.2)
				if(px.red == color[count]["red"] and px.green == color[count]["green"] and px.blue == color[count]["blue"]):
					result = True
					print(colored( ("-- Correct Drop Color debug.... x: %d, y: %d -- Index %d --  Pixel %s" % (c_x + p_x, c_y + p_y, indx, px)), "green" ))

					indx = indx + 1

					break
				count = count + 1

			if(result):
				continue

			else:
				print(colored( ("Drop Color debug..... x: %d, y: %d -- Index %d --  Pixel %s" % (c_x, c_y, indx, px)), "red" ))
				tools.exit()	

		sleep(0.5)



		indx = indx + 1
		dr_count = dr_count + 1

		if(one):
			return indx

	return dr_count

def drop_coord_move(x, y, color, opt = 0):
	indx = 0
	while (True):
		keyborad_events.main_events()
		pyautogui.moveTo(x, y)
		if(color):
			count = 0
			result = False
			while(count < len(color)):
				keyborad_events.main_events()
				p_x, p_y =  0, 0
				print("--Count", count)
				px = pyautogui.pixel(x,  y)
				print("Drop Color debug.... x: %d, y: %d -- Index %d --  Pixel %s" % (x, y , indx, px))
				sleep(0.2)
				if(px.red == color[count]["red"] and px.green == color[count]["green"] and px.blue == color[count]["blue"]):
					result = True
					print(colored( ("-- Correct Drop Color debug.... x: %d, y: %d -- Index %d --  Pixel %s" % (x, y, indx, px)), "green" ))

					indx = indx + 1

					break
				count = count + 1

			if(result):
				print(colored( ("-- Exit Color debug.... x: %d, y: %d -- Index %d --  Pixel %s" % (x, y, indx, px)), "green" ))
				tools.exit()

			else:
				if(opt == 0):
					x = x +1
					print(colored( ("Increment X..... x: %d, y: %d " % (x, y)), "red" ))
				elif(opt == 1):
					y = y +1
					print(colored( ("Increment Y..... x: %d, y: %d " % (x, y)), "red" ))


dr_save = 0



