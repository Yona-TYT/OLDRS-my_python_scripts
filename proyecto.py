import pyautogui

screenWidth, screenHeight = pyautogui.size() # Get the size of the primary monitor.
x, y = pyautogui.position() # Get the XY position of the mouse.
px = pyautogui.pixel(x, y)





# Centro de la pantalla
cent_x, cent_y = 700, 495

# Limites de la piedras a minar
min_lim_x_a, min_lim_y_a = 417, 233
min_lim_x_b, min_lim_y_b = 938, 683

#while (min_lim_y_a < min_lim_y_b):
#	count_x = min_lim_x_a
#	while (count_x < min_lim_x_b):
#		pyautogui.moveTo(count_x, min_lim_y_a)
#		count_x = count_x + 20

#	min_lim_y_a = min_lim_y_a + 25


# Limites del inventario
inv_lim_a, inv_lim_b = 404, 326


lis_test =	[	{"x":993, "y":501, "r":0}, {"x":694, "y":565, "r":1}, {"x":835, "y":632, "r":0}, {"x":922, "y":590, "r":0}, 
				{"x":835, "y":463, "r":0}, {"x":794, "y":565, "r":0}, {"x":792, "y":541, "r":0}, {"x":749, "y":575, "r":0}, 
				{"x":790, "y":457, "r":0}, {"x":917, "y":447, "r":0}, {"x":881, "y":574, "r":0}, {"x":794, "y":490, "r":0}, 
				{"x":705, "y":411, "r":0}, {"x":443, "y":391, "r":0} , {"x":433, "y":437, "r":0}, {"x":560, "y":612, "r":0}
			]

ribi_plus = 50
ribi = [{"x":700+ribi_plus, "y":480}, {"x":700, "y":480+ribi_plus}, {"x":700-ribi_plus, "y":480}, {"x":700, "y":480-ribi_plus}]
	
# Initialize counter
counter = 0
cent_plus = 18
while (counter < len(lis_test)):

	x, y = pyautogui.position() # Get the XY position of the mouse.
	px_cent = pyautogui.pixel(cent_x, cent_y+cent_plus)
	# Print values
	print("Mouse = %d,%d , Pixel %s, Pixel Center %s" % (x, y, px, px_cent))


	#continue

	pyautogui.moveTo(lis_test[counter]["x"], lis_test[counter]["y"])
	pyautogui.click()

	sw = 1

	while (px_cent.green < 250 and sw == 1):
		x, y = pyautogui.position() # Get the XY position of the mouse.
		px_cent = pyautogui.pixel(cent_x, cent_y+cent_plus)
		px = pyautogui.pixel(x+50, y+30)
		pyautogui.moveTo(ribi[lis_test[counter]["r"]]["x"], ribi[lis_test[counter]["r"]]["y"])
		print("- Mouse = %d,%d , Pixel %s , sw %d" % (x, y, px_cent, sw))
		while (px.blue > 250):
			print("-- Mouse = %d,%d , Pixel %s" % (x, y, px_cent))
			#Sacan Values
			x, y = pyautogui.position() # Get the XY position of the mouse.
			px = pyautogui.pixel(x+50, y+30)
			px_cent = pyautogui.pixel(cent_x, cent_y+cent_plus)
			if(px.blue < 250 and px_cent.green > 250):
				sw = 0
				counter = counter + 1
				break

# pyautogui.moveTo(100, 150) # Move the mouse to XY coordinates.




# Define the string
string = 'Python Bash Java Python PHP PERL'
# Define the search string
search = 'Python'
# Store the count value
count = string.count(search)
# Print the formatted output
print("Screen = %dx%d , Mouse = %d,%d , Pixel %s" % (screenWidth, screenHeight, x, y, px))
