import pyautogui

from time import sleep

def starting():
	clic_delay = 0.8

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

def starting_bank(tag, bank, clic):

	starting()

	clic_delay = 0.8
	if(clic):
		pyautogui.moveTo(bank["x"], bank["y"])
		sleep(clic_delay)
		pyautogui.click()
		sleep(clic_delay)

	c_lock_x, c_lock_y = 314, 273
	px_lock = pyautogui.pixel(c_lock_x, c_lock_y)
	sleep(clic_delay)
	while(True):
		print("Waiting for entry pin...%d px %s"% (0, px_lock))
		if (px_lock.red < 255 ):
			break
		px_lock = pyautogui.pixel(c_lock_x, c_lock_y)

	dep_x, dep_y = 656, 708
	pyautogui.moveTo(dep_x, dep_y)
	sleep(clic_delay)
	pyautogui.click(dep_x, dep_y)

	pyautogui.moveTo(tag["x"], tag["y"])
	sleep(clic_delay)
	pyautogui.click(tag["x"], tag["y"])

def set_xvalue(num, bank, clic):

	clic_delay = 0.8
	if(clic):
		pyautogui.moveTo(bank["x"], bank["y"])
		sleep(clic_delay)
		pyautogui.click()
		sleep(clic_delay)

	xvalue_x, xvalue_y = 520, 715
	pyautogui.moveTo(xvalue_x, xvalue_y)
	sleep(0.3)
	pyautogui.click()
	sleep(0.3)
	pyautogui.click(button='right')
	pyautogui.moveTo(xvalue_x, xvalue_y + 40)
	sleep(0.5)
	pyautogui.click()
	sleep(0.8)
	pyautogui.write(("%d")%num, interval=0.25)
	sleep(0.8)
	pyautogui.press('enter')



