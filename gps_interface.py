# Stephen McDonnell
# 24/04/2019

from gps import *
from time import *
import time
from multiprocessing import Process, Queue


class GPSInterface(Process):

    def __init__(self, queue):
        super().__init__()
        self.gpsd = None # bring it in scope
        self.gpsd = gps(mode=WATCH_ENABLE)  # starting the stream of info
        self.current_value = None
        self.queue = queue
        self.latitude = None
        self.longitude = None

    def run(self):
        while True:
            self.gpsd.next()  # this will continue to loop and grab EACH set of gpsd info to clear the buffer
            self.get_gps_reading()
            time.sleep(1)

    def get_gps_reading(self):
        self.latitude = self.gpsd.fix.latitude
        self.longitude = self.gpsd.fix.longitude
        self.queue.put((self.latitude, self.longitude))

if __name__ == '__main__':
    queue = Queue()
    gps_interface = GPSInterface(queue)
    gps_interface.daemon = True
    gps_interface.start()
    while True:
        try:
            print(queue.get(block=False))
        except Exception as e:
            pass
        time.sleep(0.5)