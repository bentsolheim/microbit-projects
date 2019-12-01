from microbit import *

tall1 = 1
tall2 = 1
modus = 1

newMessage = None
currentMessage = None
timePressed = 0

while True:

    if modus == 1:
        newMessage = str(tall1)
    if modus == 2:
        newMessage = str(tall2)
    if modus == 3:
        newMessage = str(tall1 * tall2)
    if modus == 4:
        tall1 = 1
        tall2 = 1
        modus = 1

    if newMessage != currentMessage:
        print("Write message: " + newMessage)
        currentMessage = newMessage
        if modus == 3:
            display.scroll(currentMessage, wait=False, loop=True)
        else:
            display.show(currentMessage, wait=False, loop=True)

    if button_a.is_pressed() == 1:
        if timePressed == 0:
            modus = modus + 1
        timePressed += 25
    if button_b.is_pressed() == 1:
        if timePressed == 0:
            timePressed += 25
            if modus == 1:
                tall1 = tall1 + 1
            if modus == 2:
                tall2 = tall2 + 1

    if button_a.is_pressed() == 0 and button_b.is_pressed() == 0:
        timePressed = 0
    sleep(25)
