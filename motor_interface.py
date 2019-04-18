# Stephen McDonnell
# 16/04/2019

from gpiozero import Robot

grazeBot = Robot(left=(7, 8), right=(9, 10))

class Motor_Interface:

    def __init__(self):
        pass

    def move(self):
        if self.left:
            grazeBot.forward()
            print("Moving Forward\n")
        elif self.right:
            grazeBot.backward()
            print("Reversing\n")
        elif self.top:
            grazeBot.right()
            print("Turning Right\n")
        elif self.bottom:
            grazeBot.left()
            print("Turning Left\n")

    def stop(self):
        grazeBot.stop()