import pyautogui
from time import *

n = int(input())
sleep(2)
for i in range(1,n+1):
    for j in range(i):
        pyautogui.press("#")
    pyautogui.press('enter')




