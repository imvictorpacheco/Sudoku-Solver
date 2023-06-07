import webbrowser as web
import pyautogui
import keyboard
from time import *
import numpy as np
import cv2
from PIL import Image
import pytesseract
import AppOpener

# First Part -> Get the base matrix

def open_sudoku():
	AppOpener.open("SUDOKU CLASSIC!")
	sleep(1)

def get_main_matrix():
	tile_size = 99
	margin = 15
	screenshot_matrix()
	M = matrix_generator(9, 0)
	for row in range(9):
		for col in range(9):
			x = margin + col * tile_size
			y = margin + row * tile_size
			img = cv2.imread("sudoku_matrix.jpg")
			cropped_image = img[x:x+tile_size - (2 * margin), y:y+tile_size - (2 * margin)]
			gray = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2GRAY)
			# sharpen_kernel = np.array([[-1,-1,-1], [-1,9.5,-1], [-1,-1,-1]])
			# sharpen = cv2.filter2D(gray, -1, sharpen_kernel)
			cv2.imwrite("matrix_aux_tile.jpg", gray)
			num = pytesseract.image_to_string(gray, lang='eng',config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789').replace('\n', '')
			try:
				M[col][row] = int(num)
			except:
				None
	return M

def matrix_generator(size, v):
	matrix = []
	for a in range(size):
		line = []
		for b in range(size):
			line.append(v)
		matrix.append(line)
	return matrix

def screenshot_matrix():
	tile_size = 99
	pyautogui.screenshot("sudoku_matrix.jpg", region = (400-8, 60, tile_size * 9, tile_size * 9))

def print_matrix(matrix):
	for l in matrix:
		print(l)
# Second Part -> Solve

def solve_matrix(matrix, draft):
	print("Antes do apdate", draft[8][8])
	draft = update_draft(matrix, draft)
	print("Depois do apdate", draft[8][8])
	for r in range(9):
		for c in range(9):
			if type(draft[r][c]) == int:
				matrix[r][c] = draft[r][c]
	return matrix

	# Sub-functions for solving
def update_draft(matrix, draft):
	for i in range(81):
		r, c = index_to_coord(i)
		if matrix[r][c] != 0 and type(draft[r][c]) == list:
			draft[r][c] = matrix[r][c]
		row  = get_rcq(matrix, i, 'r')
		col  = get_rcq(matrix, i, 'c')
		quad = get_rcq(matrix, i, 'q')
		n_l = merge_lists(row, col, quad)
		print(f"r, c = {r},{c}")
		print(f"row = {row}")
		print(f"col = {col}")
		print(f"quad = {quad}")
		if type(draft[r][c]) == list:
			draft[r][c] = subtract_lists(list(draft[r][c]), n_l)
		if type(draft[r][c]) == list and len(draft[r][c]) == 1:
				draft[r][c] = draft[r][c][0]
				print(draft[r][c])
	return draft


def last_free_cell(matrix):

	return matrix


def get_rcq(matrix, index, c):
	ans = []
	row, col = index_to_coord(index)
	if c == 'c':
		for r in range(9):
			ans.append(matrix[r][col])
	elif c == 'r':
		ans = matrix[row]
	elif c == 'q':
		r, c = index_to_coord(quad_to_index(index_to_quad(index)))
		for i in range(-1, 2):
			for j in range(-1, 2):
				ans.append(matrix[r + i][c + j])
	return ans

def index_to_quad(index):
	row, col = index_to_coord(index)
	quad = int(row / 3) * 3 + int(col / 3)
	return quad

def quad_to_index(quad):
	return int(quad%3)*3 + 10 + (int(quad/3))*27

def index_to_coord(index):
	col = index % 9
	row = int(index / 9)
	return row, col

def merge_lists(list1, list2, list3):
	merged_list = []
	for num in list1:
		if num not in merged_list:
			merged_list.append(num)
	for num in list2:
		if num not in merged_list:
			merged_list.append(num)
	for num in list3:
		if num not in merged_list:
			merged_list.append(num)
	return merged_list

def subtract_lists(main_list, sub_list):
	for i in sub_list:
		if i in main_list:
			main_list.remove(i)
	return main_list