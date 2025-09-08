import pyautogui as pg
import keyboard
import time
#save

while True:
    if keyboard.is_pressed('0'):

        time.sleep(5)
        pg.hotkey('ctrl', 's')
    if keyboard.is_pressed('z'):
        break