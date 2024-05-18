import pyautogui as gui
import time

gui.moveTo(1172, 705) # checking pointer for directing mouse
gui.click() #  when the coordinates are set, the mouse will be clicked on the area

# use looping for in 80
for i in range(80):
   gui.write("Test")    #  write "Test"
   time.sleep(0.1)      #  give pause in 0.1 second
   gui.press("Enter")   #  press enter for new line