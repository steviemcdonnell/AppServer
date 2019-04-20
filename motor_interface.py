# Stephen McDonnell
# 16/04/2019

# from gpiozero import Robot
import RPi.GPIO as gpio
#from mock_robot import Robot            # COMMENT ME
from multiprocessing import Process, Queue, Pipe
import time

class MotorInterface(Process):

    def __init__(self, queue):
        super().__init__()
        self.queue = queue
        #self.graze_bot = Robot(left=(17, 18), right=(22, 23))
        self.movement = "still"
        self.ML_1 = 17
        self.ML_2 = 18
        self.MR_1 = 22
        self.MR_2 = 23
        gpio.setmode(gpio.BCM)
        gpio.setup(self.ML_1, gpio.OUT)
        gpio.setup(self.ML_2, gpio.OUT)
        gpio.setup(self.MR_1, gpio.OUT)
        gpio.setup(self.MR_2, gpio.OUT)

    def run(self):
        while True:
            try:
                self.movement = self.queue.get_nowait()
            except Exception:
                pass
            time.sleep(1/100)
            self.movement_to_operation_translation()
            gpio.output(self.ML_1, True)
            gpio.output(self.ML_2, False)
            gpio.output(self.MR_1, True)
            gpio.output(self.MR_2, False)
            time.sleep(1)


    def movement_to_operation_translation(self):
        # Get method name from command of request json packet
        method_name = self.movement
        # Get the method from self. Default to lambda if command not recognised
        method = getattr(self, method_name, lambda: "Invalid Movement")
        # Call the method as it is returned
        method()

    def left(self):
        # Move Motors left here

        return "Moving Left"

    def right(self):
        # Move Motors right here
        # self.graze_bot.right()
        return "Moving Right"

    def forward(self):
        # Move Motors forward here
        # self.graze_bot.forward()
        return "Moving Forward"

    def reverse(self):
        # Move Motors in reverse here
        # self.graze_bot.backward()
        return "Moving Reverse"

    def still(self):
        # Motors are Stationary
        # self.graze_bot.stop()
        return "Stationary"