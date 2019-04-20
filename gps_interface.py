# Stephen McDonnell
# 16/04/2019

import random
import time


class GPSInterface:

    def __init__(self):
        self.latitute = None
        self.longitude = None

    def get_gps_reading(self):
        # TO-DO
        # Python Hardware calls here i.e. read SPI, I2C, UART, etc and get data

        # Sudo number gen for testing
        random.seed(time.time())
        self.latitute = round(random.randint(-900, 900) * 0.10, 2)
        self.longitude = round(random.randint(-1800, 1800) * 0.10)
        return self.latitute, self.longitude