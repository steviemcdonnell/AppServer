# Stephen McDonnell
# 16/04/2019

import curses
from gpiozero import Robot

grazeBot = Robot(left = (17, 18), right = (22, 23))

actions = {
    curses.KEY_UP:       grazeBot .forward,
    curses.KEY_DOWN:     grazeBot .backward,
    curses.KEY_LEFT:     grazeBot .left,
    curses.KEY_RIGHT:    grazeBot .right,
    }

def Motor_Interface(window):
    next_key = None
    while True:
        curses.halfdelay(1)
        if next_key is None:
            key = window.getch()
        else:
            key = next_key
            next_key = None
        if key != -1:
            # Key pressed
            curses.halfdelay(3)
            action = actions.get(key)
            if action is not None:
                action()
            next_key = key
            while next_key == key:
                next_key = window.getch()
            # Key released
            grazeBot .stop()
curses.wrapper(Motor_Interface)