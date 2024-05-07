import pyautogui

from time import sleep

import os

from pynput import keyboard

from termcolor import colored

import threading

import queue
curr_key = queue.Queue()
ok_key = queue.Queue()

def on_press(key):
	if(curr_key.empty()):
		try:
			if(key.char == '<' or key.char == '>'):
				curr_key.put(key)
				#thread = threading.main_thread()
				#thread.join()
			#print('alphanumeric key {0} pressed'.format(key.char))

		except AttributeError:
			True
			#print('special key {0} pressed'.format(key))

def on_release(key):
	#print('{0} released'.format(key))

	if(not curr_key.empty()):
		ok_key.put(key)
		curr_key.queue.clear()
		
	if key == keyboard.Key.esc:
		# Stop listener
		return False

def main_events():
	if(not ok_key.empty()):
		pyautogui.keyUp('shift')
		print(colored( ("Script Pause..."), "red"))
		ok_key.queue.clear()
		while (True):
			if(not ok_key.empty()):
				ok_key.queue.clear()
				return True

	return False


def main_pause():
	pyautogui.keyUp('shift')
	print(colored( ("Script Pause..."), "red"))
	while (True):
		if(not ok_key.empty()):
			ok_key.queue.clear()
			return True

def start_listener():
	listener = keyboard.Listener(on_press=on_press, on_release=on_release)	
	listener.start()

start_listener()

main_events()



