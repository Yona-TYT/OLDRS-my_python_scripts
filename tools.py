import pyautogui

from time import sleep

import argparse

import sys

from datetime import datetime

import keyborad_events

import subprocess

from termcolor import colored

# Centro de la pantalla
cent_x, cent_y = 575, 490

def schedule(list_sch, cali = False, idx = 0):
	parser = argparse.ArgumentParser()
	parser.add_argument("-c", "--count", help="MAx count in schedule", type=int)
	parser.add_argument("-a", "--agility", help="Agility Mode", action="store_true")
	argum = parser.parse_args()
	mark_list = False
	if(argum.agility):
		counter = 0
		mark_list = idx
	
	else:
		counter = idx

	walk_plus_x, walk_plus_y = 0 , 40
	clic_plus_x, clic_plus_y = 80 , 33

	while (counter < len(list_sch)):
		keyborad_events.main_events()
		if(argum.agility ):
			keyborad_events.main_events()
			m_idx = list_sch[counter]["i"]
			if(m_idx > -1):
				sleep(0.2)
				i, m_x, m_y, r_x, r_y = mark_list[m_idx]["i"], mark_list[m_idx]["x"], mark_list[m_idx]["y"], mark_list[m_idx]["rx"], mark_list[m_idx]["ry"]
				px_mark = pyautogui.pixel(m_x, m_y)
				sleep(0.5)
				print("Find Mark... Indx: %d , XY: %d,%d -- Pixel %s" % ( m_idx, m_x, m_y, px_mark))
				if(px_mark.red > 130 and px_mark.green > 110 and px_mark.blue < 15):
					print("Aqui hay , Aqui hay, Aqui hay...  Mark... index: %d  null %d" % (counter, 0))
					pyautogui.moveTo(m_x, m_y)
					sleep(0.8)
					pyautogui.click(m_x, m_y)
					sleep(3)
					pyautogui.moveTo(r_x, r_y)
					sleep(0.8)
					pyautogui.click(r_x, r_y)
					if(wait_in_tile( cent_x, cent_y)):
						counter = i
					sleep(0.8)
					
		c_x, c_y = list_sch[counter]["x"], list_sch[counter]["y"]
		delay = list_sch[counter]["t"]
		opt = list_sch[counter]["clic"]
		pyautogui.moveTo(c_x, c_y)

		if(opt==3):
			sleep(1.2)
			pyautogui.click(c_x, c_y)

		else:
			pyautogui.click(c_x, c_y)

		print("Waiting.. Delay : %f s  Coord: %d, %d --- index: %d" % (delay, c_x, c_y, counter))
		sleep(delay)

		x, y = pyautogui.position() # Get the XY position of the mouse.
		px_cent = pyautogui.pixel(cent_x, cent_y)
		# Print values
		#print("Mouse = %d,%d , Pixel %s, Pixel Center %s" % (x, y, px_cent, px_cent))

		if(opt==2):
			print("Schedule Skip... Indx: %d , XY: %d,%d -- Pixel %s" % ( counter, c_x, c_y, px_cent))
			counter = counter + 1
			continue
			
		counter = black_waiting(list_sch, counter, px_cent, cali, opt, delay, argum)
		if(counter < 0):
			if(argum.agility):
				return counter
			else:
				return 2
						
	return True

def black_waiting(list_sch, counter, px_cent, cali, opt, delay, argum):

	count = 0
	if(argum.count):
		count_max = argum.count

	else:
		count_max = 80

	while (px_cent.red !=0 or px_cent.green !=0 or px_cent.blue !=0):
		keyborad_events.main_events()
		px_cent = pyautogui.pixel(cent_x, cent_y)
		c_i = list_sch[counter]["c_i"]
		#Debug-------------------------------------------------------------------------
		#pyautogui.moveTo(cent_x, cent_y)
		#------------------------------------------------------------------------------

		count = count + 1
		print("Schedule... Count %d, Indx: %d -- Pixel %s" % (count, counter, px_cent))
		if(count > count_max):
			if(cali == False):
				return False

			else:
				if(argum.agility and c_i < 0):
					return c_i

				if(calibrate(list_sch[counter]["c_r"])):
					counter = c_i
					print("Calibrate index.. ", counter)
					return counter
	if(opt == 1):
		print("Schedule delay 1... Indx: %d , -- Pixel %s" % ( counter, px_cent))
		sleep(1)
	counter = counter + 1
	return counter

def calibrate(ribi):
	x, y = 575, 490
	incr_x = 24.5
	incr_y = 22
	fact_y = 0

	incr_z =  0.4

	clic_delay = 0.8

	x_plus = 0
	y_plus = 0

	x_star = 0
	y_star = 0

	t = 0
	tt = 0
	count = 0
	
	mx_count = 40
	if(ribi>1):
		mx_count = 44

	clc_try = 0
	while(True):
		keyborad_events.main_events()
		if(ribi == 0):						#Derecha   0
			x = x + incr_x
			x_plus = incr_x+5
			y_star = 825
			incr_z = incr_z * 1
		elif(ribi == 1):					#Izquierda 1
			x = x -incr_x
			x_plus = -incr_x-5
			y_star = 825
			if(incr_z>0):
				incr_z = (incr_z * (-1))
		elif(ribi == 2):					#Ariba     2
			y = y - incr_y + fact_y
			y_plus = -incr_y
			x_star = 1132
			incr_z = incr_z * 1
			fact_y = fact_y + 0.5
		elif(ribi == 3):					#Abajo     3
			y = y + incr_y
			y_plus =  incr_y+10
			x_star = 1132
			fact_y = fact_y + 0.5
			if(incr_z>0):
				incr_z = (incr_z * (-1))

		px = get_pixel(x, y)

		print("Calibrate... Z: %d Coord: %d, %d, Count %d, Pixel %s" % (incr_z, x, y, count, px))
		#Debug-------------------------------------------------------------------------
		#pyautogui.moveTo(x, y)
		#sleep(0.8)
		#------------------------------------------------------------------------------
		if(count > mx_count):
			exit()

		if (px.red ==0 and px.green ==0 and px.blue ==0):

			if(clc_try > 1):
				print("Click Skip... ")
				clc_try = 0
				continue

			pyautogui.moveTo(x, y)
			pyautogui.click()

			print("Click Delay... ", 2+tt)
			sleep(2+tt)
			tt = 0

			if(not wait_in_tile( x, y)):
				print("Click Try... ", clc_try)
				x = cent_x
				y = cent_y
				clc_try = clc_try + 1
				continue
			x = x+x_plus
			y = y+y_plus

			if(x_star == 0):
				y = y_star
				x = cent_x + x_plus

			elif(y_star == 0):
				x = x_star
				y = cent_y + y_plus

			find_count = 0
			try_con = 0 
			fact_y = 0
			calc_t = 0
			tile_incr = 6
			while(True):
				keyborad_events.main_events()
				px = pyautogui.pixel(x, y)
				t = t + 0.2

				#Debug-------------------------------------------------------------------------
				#pyautogui.moveTo(x, y)
				#------------------------------------------------------------------------------

				print("Calibrate_Find_bord... Coord: %d, %d, Count %d, Pixel %s" % (x, y, find_count, px))
				if (px.red ==0 and px.green ==0 and px.blue ==0):
					pyautogui.moveTo(x, y)
					pyautogui.click()
					
					calc_t = (calc_t/28)+3
					print("Click Delay Calc... ", calc_t)
					sleep(calc_t)

					if(not wait_in_tile( cent_x, cent_y)):
						t = 0
						t_x , t_y = 8.5, 8.5
						if(try_con == 1):
							t_x , t_y = 11.8, 11.8
						if(try_con == 2):
							t_x , t_y = 5.8, 5.8
						if(try_con == 3):
							t_x , t_y = 15, 1			
						elif(try_con == 4):				
							break


						if(ribi == 0):			#Derecha   0
							y = y_star - t_y
							x = x - (tile_incr*t_x)

						elif(ribi == 1):		#Izquierda 1
							y = y_star - t_y
							x = x + (tile_incr*t_x)

						elif(ribi == 2):		#Ariba     2
							x = x_star - t_x
							y = y + t_y + (tile_incr*incr_y)

						elif(ribi == 3):		#Abajo     3
							x = x_star - t_x
							y = y - t_y - (tile_incr*incr_y)

						try_con = try_con + 1
						find_count = 0
						continue

					if(ribi == 0):			#Derecha   0
						get_pos(1, cent_x + (incr_x*-2), cent_y)

					elif(ribi == 1):		#Izquierda 1
						get_pos(0, cent_x + (incr_x*2), cent_y)

					elif(ribi == 2):		#Ariba     2
						get_pos(3, cent_x, cent_y + (incr_y*2))

					elif(ribi == 3):		#Abajo     3
						get_pos(2, cent_x, cent_y - (incr_y*2))

					
					return True

				if(x_star == 0):
					print("Increment in Y... ")
					x = (x + incr_z)
					y = y - incr_y + fact_y
					fact_y = fact_y + 0.2
					if(y > cent_y):
						calc_t = y - cent_y
					else:
						calc_t = cent_y - y

					if(find_count > mx_count):
						x = cent_x + x_plus
						pyautogui.click(x,cent_y)
						print("Click Calibrate Center... ")
						x = cent_x
						y = cent_y
						break

				elif(y_star == 0):
					print("Increment in X... ")
					y = y - incr_z
					x = x - incr_x
					if(x > cent_y):
						calc_t = x - cent_x
					else:
						calc_t = cent_x - x
					if(find_count > mx_count):
						y = cent_y + y_plus
						pyautogui.click(cent_x,y)
						print("Click Calibrate Center... ")
						x = cent_x
						y = cent_y
						break



				find_count = find_count + 1

		tt = tt + 0.6
		count = count + 1

	return True

def get_pos(ribi, x, y):
	incr_x = 26
	incr_y = 21
	count = 0
	t = 0

	def_x = x
	def_y = y

	print("Start Get_Pos...")
	while(True):
		keyborad_events.main_events()
		t = t + 0.4
		if(ribi == 0):			#Derecha   0
			x = x + incr_x

		elif(ribi == 1):		#Izquierda 1
			x = x -incr_x

		elif(ribi == 2):		#Ariba     2
			y = y - incr_y

		elif(ribi == 3):		#Abajo     3
			y = y + incr_y

		px = pyautogui.pixel(x, y)

		print("Get_Pos... Coord: %d, %d, Count %d, Pixel %s" % (x, y, count, px))

		#Debug-------------------------------------------------------------------------
		#pyautogui.moveTo(x, y)
		#------------------------------------------------------------------------------

		count = count+1
		if(count == 20):
			x =	def_x + 12
			y = def_y + 12 
			t = 0

		if(count == 40):
			x =	def_x - 12
			y = def_y - 12 
			t = 0

		if(count == 60):
			x =	def_x + 22
			y = def_y + 22 
			t = 0

		if(count == 80):
			x =	def_x - 22
			y = def_y - 22 
			t = 0
			count = 0
			
		if (px.red ==0 and px.green ==0 and px.blue ==0):
			pyautogui.moveTo(x, y)
			pyautogui.click()
			print("Click Delay... ", 2+t)
			sleep(2+t)

			if(not wait_in_tile( x, y)):
				def_x, def_y = cent_x, cent_y
				x, y = cent_x, cent_y
				#count = 0
				t = 0
				continue
			
			return True

	return False

def wait_in_tile(x, y):
	px_cent = pyautogui.pixel(cent_x, cent_y)
	wt_count = 0
	while (px_cent.red !=0 or px_cent.green !=0 or px_cent.blue !=0):
		keyborad_events.main_events()
		print("Waiting Black tile... Coord: %d, %d, WT_Count %d, Pixel %s" % (x, y, wt_count, px_cent))
		wt_count = wt_count + 1
		px_cent = pyautogui.pixel(cent_x, cent_y)
		if(wt_count > 30):
			return False

	return True

x_max, y_max = 1439, 899
def get_pixel(x, y):
	if(x > x_max or y > y_max):

		print("Out of range: x y: %d, %d --  x_max: %d y_max: %d " % (x, y, x_max, y_max))
		return exit()

	return pyautogui.pixel(x, y)


def exit():
	# datetime object containing current date and time
	now = datetime.now()
	 
	#print("now =", now)

	# dd/mm/YY H:M:S
	dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

	#Argu Poweroff--------------------------
	parser = argparse.ArgumentParser()
	parser.add_argument("-p", "--power", help="Poweroff system", action="store_true")
	argum = parser.parse_args()

	if(argum.power):
		t = 30


		count = 0
		while(count < t):
			print(colored( ("Alert, System poweroff in : " + str(t - count) +" s ... You can press < > to PAUSE."), "red"))
			keyborad_events.main_events()
			sleep(1)
			count = count +1

		subprocess.run(["shutdown", "-h", "now"])

	print(colored( ("Sys exit.. Current date: " + dt_string), "red"))
	sys.exit()

