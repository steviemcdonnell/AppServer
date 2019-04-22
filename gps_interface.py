# Stephen McDonnell
# 16/04/2019

#import random
#import time
from gps import *
import time
import threading

#f = open("locations.csv", "w")
gpsd = None

class GPSInterface(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        global gpsd
        gpsd = gps(mode=WATCH_ENABLE)
        self.current_value = None
        self.running = True

    def run(self):
        global gpsd
        while gpsp.running:
            gpsd.next()


if __name__ == '__main__':
    gpsp = GPSInterface()
#    try:
#        gpsp.start()
#        while True:
#            f.write(str(gpsd.fix.longitude)
#                    + "," + str(gpsd.fix.latitude)
#                    + "\n")
#            time.sleep(30)
#    except(KeyboardInterrupt, SystemExit):
#        f.close()
#        gpsp.running = False
#        gpsp.join()


##################################################################################
#########################            TEST            #############################
#    def __init__(self):
#        self.latitute = None
#        self.longitude = None
#
#    def get_gps_reading(self):
#        # TO-DO
#        # Python Hardware calls here i.e. read SPI, I2C, UART, etc and get data
#
#        # Sudo number gen for testing
#        random.seed(time.time())
#        self.latitute = round(random.randint(-900, 900) * 0.10, 2)
#        self.longitude = round(random.randint(-1800, 1800) * 0.10)
#        return self.latitute, self.longitude
##################################################################################
##################################################################################
