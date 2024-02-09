
from pyautogui import *
import pyautogui
import keyboard
import time
import win32api, win32con


'''
#1  Magic Piano Tiles
>>> https://www.agame.com/game/magic-piano-tilesr


#2  Find x: y: Position via Python
>>> import pyautogui
>>> pyautogui.displayMousePosition()
X:000  y:000 |RGB: (0,0,0)

# Tile 1 Position:  x:525   y:800
# Tile 2 Position:  x:650   y:800
# Tile 3 Position:  x:770   y:800
# Tile 4 Position:  x:900   y:800

'''



def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)


run_bot = False
while True:

    if keyboard.is_pressed('r'): #Press "r" to run
        run_bot = True
        print("RUN")
    if keyboard.is_pressed('q'): #Press "q" to stop
        print("STOP")
        break

    if run_bot:
        if pyautogui.pixel(525,800)[0] == 0:
            click(525,800)
        if pyautogui.pixel(650,800)[0] == 0:
            click(650,800)
        if pyautogui.pixel(770,800)[0] == 0:
            click(770,800)
        if pyautogui.pixel(900,800)[0] == 0:
            click(900,800) 
    


