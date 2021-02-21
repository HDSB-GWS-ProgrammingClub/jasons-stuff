from pynput import mouse, keyboard
from pynput.mouse import Button, Controller

mouse = Controller()

virusOn = True

while virusOn == True:
    mouse.position = (300, 300)