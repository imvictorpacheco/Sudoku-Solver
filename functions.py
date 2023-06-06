import webbrowser as web
import pyautogui
import keyboard
from time import *
import numpy as np
import cv2
from PIL import Image
import pytesseract
import AppOpener

# def open_sudoku():
# 	web.open_new("https://sudoku.com/")
# 	sleep(1)
# 	pyautogui.moveTo(200, 200)
# 	for i in range(16):
# 		sleep(0.01)
# 		keyboard.press_and_release("ctrl+-")
# 	for i in range(10):
# 		sleep(0.01)
# 		keyboard.press_and_release("ctrl+plus")
# 	sleep(0.5)
# 	pyautogui.scroll(5000)
# 	sleep(0.05)
# 	pyautogui.scroll(-200)
# 	sleep(0.5)
# 	pyautogui.click(90,250)
# 	sleep(0.5)
# 	pyautogui.click(10,250)

def open_sudoku():
	AppOpener.open("SUDOKU CLASSIC!")
	sleep(1)

def get_matrix():
	tile_size = 99
	margin = 15
	screenshot_matrix()
	M = list(np.zeros((9, 9), dtype = int))
	for row in range(9):
		for col in range(9):
			x = margin + col * tile_size
			y = margin + row * tile_size
			img = cv2.imread("sudoku_matrix.jpg")
			cropped_image = img[x:x+tile_size - (2 * margin), y:y+tile_size - (2 * margin)]
			gray = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2GRAY)
			sharpen_kernel = np.array([[-1,-1,-1], [-1,9.5,-1], [-1,-1,-1]])
			sharpen = cv2.filter2D(gray, -1, sharpen_kernel)
			cv2.imwrite("matrix_aux_tile.jpg", sharpen)
			num = pytesseract.image_to_string(gray, lang='eng',config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789').replace('\n', '')
			try:
				M[col][row] = int(num)
			except:
				None
			print(num, "->", col+1, ",", row+1)
	return M

def screenshot_matrix():
	tile_size = 99
	pyautogui.screenshot("sudoku_matrix.jpg", region = (400-8, 60, tile_size * 9, tile_size * 9))

def print_matrix(matrix):
	for l in range(len(matrix)):
		print(matrix[l])