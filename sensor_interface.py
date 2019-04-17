# Stephen McDonnell
# 16/04/2019

import random
import time


class Sensor_Interface:

    def __init__(self):
        self.temperature = 20.6
        self.humidity = 50

    def get_sensor_readings(self):
        # TO-DO
        # Python Hardware calls here i.e. read SPI, I2C, UART, etc and get data

        # Sudo number gen for testing
        random.seed(time.time())
        self.temperature = round(random.randint(-400, 1250) * 0.10, 2)
        self.humidity = round(random.randint(0, 1000) * 0.10, 2)
        return self.temperature, self.humidity


