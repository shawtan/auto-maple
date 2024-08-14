import pydirectinput
import time

def mystic_cube():
    count = 0
    pydirectinput.keyDown("enter")

    while True:
        # print("click")
        pydirectinput.click(button="left")
        pydirectinput.click(button="left")
        # time.sleep(0.1)
        pydirectinput.keyDown("enter")
        # time.sleep(0.1)
        pydirectinput.keyDown("enter")
        # time.sleep(0.1)
        pydirectinput.keyDown("enter")

        time.sleep(1.5)
        count += 1
        if count == 100:
            break

time.sleep(1)
mystic_cube()
print("done")