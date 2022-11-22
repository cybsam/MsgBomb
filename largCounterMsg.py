import pyautogui
import time

time.sleep(3)
count = 0

while count <= 10:
    pyautogui.typewrite("hey broh...")
    pyautogui.press("enter")
    time.sleep(5)
    count = count + 1




