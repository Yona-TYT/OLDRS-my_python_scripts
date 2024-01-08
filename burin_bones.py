import pyautogui

from time import sleep

import keyborad_events

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


def bury_bones_normal():
	# Limites del inventario
	inv_lim_x_a, inv_lim_y_a = 993, 617
	inv_lim_x_b, inv_lim_y_b = 1150, 857
	p_x, p_y = 25 , 39
	x, y = pyautogui.position() # Get the XY position of the mouse.
	is_bury = False
	while (inv_lim_y_a < inv_lim_y_b):
		print("Check for bones...")
		keyborad_events.main_events()
		count_x = inv_lim_x_a
		count = 1
		#pyautogui.moveTo(count_x, inv_lim_y_a)
		#tes_plus_cursor(count_x,inv_lim_y_a)
		while (count_x < inv_lim_x_b):
			keyborad_events.main_events()
			plus = 0
			if(count == 2):
				plus = 2
			if(count == 3):
				plus = 2
			if(count == 4):
				plus = 0
			px = pyautogui.pixel(count_x, inv_lim_y_a)
			if (px.red ==221 and px.green ==217 and px.blue ==217):
				is_bury = True
				print("Bury bones...Count: %d --- Mouse x:%d,y:%d , Pixel %s" % (count, count_x, inv_lim_y_a, px))
				pyautogui.click(x = count_x, y = inv_lim_y_a)
				sleep(1)

			count_x = count_x + 42
			count = count + 1

		inv_lim_y_a = inv_lim_y_a + 36

	if(not is_bury):
		print("Waiting for bones...")


c_list= [
			{"x":993, "y":617}, {"x":1035, "y":617}, {"x":1077, "y":617}, {"x":1119, "y":617},
			{"x":993, "y":653}, {"x":1035, "y":653}, {"x":1077, "y":653}, {"x":1119, "y":653},
			{"x":993, "y":689}, {"x":1035, "y":689}, {"x":1077, "y":689}, {"x":1119, "y":689},
			{"x":993, "y":725}, {"x":1035, "y":725}, {"x":1077, "y":725}, {"x":1119, "y":725},
			{"x":993, "y":761}, {"x":1035, "y":761}, {"x":1077, "y":761}, {"x":1119, "y":761},
			{"x":993, "y":797}, {"x":1035, "y":797}, {"x":1077, "y":797}, {"x":1119, "y":797},
			{"x":993, "y":833}, {"x":1035, "y":833}, {"x":1077, "y":833}, {"x":1119, "y":833}
		]
def bury_bones_combat(inv_lim_x_a, inv_lim_y_a, inv_lim_x_b, inv_lim_y_b, index):

	p_x, p_y = 25 , 39
	x, y = pyautogui.position() # Get the XY position of the mouse.
	is_bury = False
	count_all = index
	while (inv_lim_y_a < inv_lim_y_b):
		print("Check for bones...")
		keyborad_events.main_events()
		count_x = inv_lim_x_a
		count = 1
		#pyautogui.moveTo(count_x, inv_lim_y_a)
		#tes_plus_cursor(count_x,inv_lim_y_a)
		while (count_x < inv_lim_x_b):
			keyborad_events.main_events()
			plus = 0
			if(count == 2):
				plus = 2
			if(count == 3):
				plus = 2
			if(count == 4):
				plus = 0
			px = pyautogui.pixel(count_x, inv_lim_y_a)
			if (px.red ==221 and px.green ==217 and px.blue ==217):
				is_bury = True
				print("Bury bones... Number: %d --- Coord x:%d,y:%d , Pixel %s" % (count_all+1, count_x, inv_lim_y_a, px))
				pyautogui.click(x = count_x, y = inv_lim_y_a)
				pyautogui.moveTo(x, y)
				sleep(1)
				return count_all

			if ((px.red ==62 and px.green ==53 and px.blue ==41) or (px.red ==64 and px.green ==54 and px.blue ==44) or (px.red ==59 and px.green ==50 and px.blue ==38)):
				print("'Free Space... Number: %d --- Coord x:%d,y:%d , Pixel %s" % (count_all+1, count_x, inv_lim_y_a, px))
				return count_all


		
			count_x = count_x + 42
			count = count + 1
			count_all = count_all + 1

		inv_lim_y_a = inv_lim_y_a + 36

	if(not is_bury):
		print("Waiting for bones...")

	return count_all

keyborad_events.start_listener()

# Limites del inventario
inv_lim_x_a, inv_lim_y_a = 993, 617
inv_lim_x_b, inv_lim_y_b = 1150, 857
index = 0
while(True):
	keyborad_events.main_events()
	bury_bones_normal()
	#if(index == 28):
	#	index = 0
	#index = bury_bones_combat(c_list[index]["x"], c_list[index]["y"], inv_lim_x_b, inv_lim_y_b, index)

ribi_plus = 50
ribi = [{"x":700+ribi_plus, "y":480}, {"x":700, "y":480+ribi_plus}, {"x":700-ribi_plus, "y":480}, {"x":700, "y":480-ribi_plus}]

def code(list_sch):	
	# Initialize counter
	counter = 0
	cent_plus = 18
	while (counter < len(lis_test)):
		keyborad_events.main_events()
		x, y = pyautogui.position() # Get the XY position of the mouse.
		px_cent = pyautogui.pixel(cent_x, cent_y+cent_plus)
		# Print values
		print("Mouse = %d,%d , Pixel %s, Pixel Center %s" % (x, y, px, px_cent))


		#continue

		pyautogui.moveTo(lis_test[counter]["x"], lis_test[counter]["y"])
		pyautogui.click()

		sw = 1

		while (px_cent.green < 250 and sw == 1):
			keyborad_events.main_events()
			x, y = pyautogui.position() # Get the XY position of the mouse.
			px_cent = pyautogui.pixel(cent_x, cent_y+cent_plus)
			px = pyautogui.pixel(x+50, y+30)
			pyautogui.moveTo(ribi[lis_test[counter]["r"]]["x"], ribi[lis_test[counter]["r"]]["y"])
			print("- Mouse = %d,%d , Pixel %s , sw %d" % (x, y, px_cent, sw))
			while (px.blue > 250):
				keyborad_events.main_events()
				print("-- Mouse = %d,%d , Pixel %s" % (x, y, px_cent))
				#Sacan Values
				x, y = pyautogui.position() # Get the XY position of the mouse.
				px = pyautogui.pixel(x+50, y+30)
				px_cent = pyautogui.pixel(cent_x, cent_y+cent_plus)
				if(px.blue < 250 and px_cent.green > 250):
					sw = 0
					counter = counter + 1
					break


