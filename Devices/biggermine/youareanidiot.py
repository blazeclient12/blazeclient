import webbrowser
import time
import pyautogui

URL = "https://web.archive.org/web/20250214221147/https://www.youareanidiot.cc/"

def open_and_fullscreen(url, initial_wait=1, pre_press_wait=0.5):
    webbrowser.open(url, new=2)
    time.sleep(initial_wait)
    time.sleep(pre_press_wait)
    pyautogui.press('f11')
open_and_fullscreen(URL)
