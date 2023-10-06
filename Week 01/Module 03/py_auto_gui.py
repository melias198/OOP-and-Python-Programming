import pyautogui
from time import sleep
width,height=pyautogui.size()
print(width,height)

x,y=pyautogui.position()
print(x,y)

pyautogui.moveTo(100, 150)  #Move the mouse to XY coordinates.

pyautogui.click()    


sleep(1)
for i in range(5):
    pyautogui.write('I Love You.', interval=0.25)
    pyautogui.press('enter') 

