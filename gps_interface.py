# Stephen McDonnell
# 16/04/2019

# This File consists of API calls for the GPS Parsing Functionality.This section parse the GPS values from the GPS Module.
# pynmea2 is Python library for parsing the NMEA 0183 protocol (GPS)

#import random
from gps import *
import time
import threading
import pynmea2
#import os

gpsd = None

class GPSInterface():

    def __init__(self):
        self.latitude = None
        self.longitude = None
        self.msg = ''

    # Gps Receiver thread function, check gps value for infinite times
    def getgpsdata(serial, dmesg):
        print("getgpsdata")
        while True:
            data = serial.readline()
            if data.find('GGA') > 0:
                dmesg.msg = pynmea2.parse(data)

    # API to call start the GPS Receiver
    def start_gps_receiver(serial, dmesg):
        t2 = threading.Thread(target=serial.getgpsdata, args=(serial, dmesg))
        t2.start()
        print("GPS Receiver started")

    # API to fix the GPS Revceiver
    def ready_gps_receiver(msg):
        print("Please wait fixing GPS .....")
        dmesg = msg.msg
        while (dmesg.gps_qual != 1):
            pass
        print("GPS Fix available")

    # API to get latitude from the GPS Receiver
    def get_latitude(msg):
        print("Getting Latitude")
        dmesg = msg.msg
        print("Latitude:", dmesg.latitude)

    # API to get longitude from the GPS Receiver
    def get_longitude(msg):
        print("Getting Longitude")
        dmesg = msg.msg
        print("Longitude:", dmesg.longitude)

    # API to get Number of Satellites from the GPS Receiver
    def get_num_satellite(msg):
        print("Getting Number of satellite")
        dmesg = msg.msg
        print("No of satellites:", dmesg.num_sats)

    # API to get Altitude of Antenna from the GPS Receiver
    def get_altitude(msg):
        print("Getting altitude of Antenna")
        dmesg = msg.msg
        print("Altitude (M):", dmesg.altitude)

    # API to check the status of GPS Fix
    def get_gps_fix(msg):
        dmesg = msg.msg
        print("GPS Fix stats:", dmesg.gps_qual)

    # API to Exit
    def function_exit(msg):
        print("Exiting ......")
        print("stopping the thread")
        exit()
        return 1

    def get_gps_reading(self):
# Python Hardware calls here i.e. read UART and get data

        # Sudo number gen for testing
        #random.seed(time.time())
        #self.latitute = round(random.randint(-900, 900) * 0.10, 2)
        #self.longitude = round(random.randint(-1800, 1800) * 0.10)

        self.latitute = self.get_latitude()
        self.longitude = self.get_longitude()
        return self.latitute, self.longitude


##################################################################################
#########################            TEST            #############################
#    def __init__(self):
#        self.latitute = None
#        self.longitude = None
#
#    def get_gps_reading(self):
#        # Python Hardware calls here i.e. read UART and get data
#
#        # Sudo number gen for testing
#        random.seed(time.time())
#        self.latitute = round(random.randint(-900, 900) * 0.10, 2)
#        self.longitude = round(random.randint(-1800, 1800) * 0.10)
#        return self.latitute, self.longitude
##################################################################################
##################################################################################
