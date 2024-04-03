import time

import pyautogui

screenWidth, screenHeight = pyautogui.size()  # Get the size of the primary monitor.
currentMouseX, currentMouseY = pyautogui.position()  # Get the XY position of the mouse.

print(f"screenWidth: {screenWidth} | screenHeight: {screenHeight} | "
      f"currentMouseX: {currentMouseX} | currentMouseY: {currentMouseY}")

time.sleep(3)

try:
    green = pyautogui.locateCenterOnScreen('../data/green.png', grayscale=False)  # find image
    pyautogui.click(green)
except pyautogui.ImageNotFoundException:
    pass

pyautogui.click(screenWidth // 2, screenHeight // 2)
distance = 200
while distance > 0:
    pyautogui.drag(distance, 0, duration=0.5)   # move right
    distance -= 5
    pyautogui.drag(0, distance, duration=0.5)   # move down
    pyautogui.drag(-distance, 0, duration=0.5)  # move left
    distance -= 5
    pyautogui.drag(0, -distance, duration=0.5)  # move up