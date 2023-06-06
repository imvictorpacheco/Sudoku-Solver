import webbrowser as web
import pyautogui as mouse
import keyboard
from time import *

def open_sudoku():
    web.open_new("https://sudoku.com/")
    sleep(1)
    mouse.moveTo(200, 200)
    for i in range(16):
        keyboard.press_and_release("ctrl+-")
    for i in range(10):
        keyboard.press_and_release("ctrl+plus")
    sleep(0.5)
    mouse.scroll(5000)
    mouse.scroll(-200)

open_sudoku()