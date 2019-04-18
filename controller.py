# Stephen McDonnell
# 16/04/2019

from sensor_interface import Sensor_Interface
from gps_interface import GPS_Interface
from motor_interface import Motor_Interface


class Controller:

    def __init__(self):
        self.request = None
        self.command = None
        self.app_latitude = None
        self.app_longitude = None
        self.latitude = None
        self.longitude = None
        self.latitude_diff = None
        self.longitude_diff = None
        self.temperature = None
        self.humidity = None
        self.movement = None

    # Unpack all json request variables into private member variables
    def unpack_request(self, request):
        self.command = request["command"]
        self.app_latitude = request["latitude"]
        self.app_longitude = request["longitude"]
        self.movement = request["movement"]

    # Build a response Dictionary for converting to JSON and sending back to the server
    def build_response(self):
        response = {
            "robot_latitude": self.latitude,
            "robot_longitude": self.longitude,
            "latitude_diff": self.latitude_diff,
            "longitude_diff": self.longitude_diff,
            "temperature": self.temperature,
            "humidity": self.humidity
        }
        return response

    # Entry Point
    def execute_request(self, request):
        self.unpack_request(request)
        self.command_to_operation_translation()
        return self.build_response()

    # Removes the need for countless if/elif/.../elses
    # String to function dispatcher
    def command_to_operation_translation(self):
        # Get method name from command of request json packet
        method_name = self.command
        # Get the method from self. Default to lambda if command not recognised
        method = getattr(self, method_name, lambda: "Invalid Command")
        # Call the method as it is returned
        method()

    # Update information to send back to the server.
    def fetch(self):
        (self.temperature, self.humidity) = Sensor_Interface().get_sensor_readings()
        (self.latitude, self.longitude) = GPS_Interface().get_gps_reading()
        self.latitude_diff = self.latitude - float(self.app_latitude)
        self.longitude_diff = self.longitude - float(self.app_longitude)






