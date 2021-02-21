from pynput.mouse import Button, Controller

mouse = Controller()

virusOn = True

while virusOn == True:
    mouse.position = (300, 300)