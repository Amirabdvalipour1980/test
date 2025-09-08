import pyautogui as pg
import keyboard

while True:
    if keyboard.is_pressed('x'):
        pg.moveTo(600, 350, duration=1)
        pg.moveTo(600, 350, duration=1)
        # pg.moveTo(206, 789, duration=1)
        # pg.moveTo(252, 996, duration=1)
    if keyboard.is_pressed('z'):
        break