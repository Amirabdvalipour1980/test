import pyautogui as pg
import keyboard
import time


while True:
    if keyboard.is_pressed('0'):
        pg.press('enter')
        pg.write('09189406036')
        pg.press('enter')
    if keyboard.is_pressed('-'):
        break