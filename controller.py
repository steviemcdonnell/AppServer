# Stephen McDonnell
# 24/04/2019

from sensor_interface import SensorInterface
from gps_interface import GPSInterface

class Controller:

    previous_lat = 0.00
    previous_long = 0.00

    def __init__(self):
        self.request = None
        self.motor_queue = None
        self.gps_queue = None
        self.sql_interface = None
        self.command = None
        self.app_latitude = None
        self.app_longitude = None
        self.latitude = None
        self.longitude = None
        self.latitude_diff = None
        self.longitude_diff = None
        self.sensor_array = None
        self.movement = None
        self.response = None

    # Unpack all json request variables into private member variables
    def unpack_request(self, request):
        self.command = request["command"]
        self.app_latitude = request["latitude"]
        self.app_longitude = request["longitude"]
        self.movement = request["movement"]

    # Build a response Dictionary for converting to JSON and sending back to the server
    def build_response(self):
        response = {
            "response": self.response,
            "robot_latitude": self.latitude,
            "robot_longitude": self.longitude,
            "latitude_diff": self.latitude_diff,
            "longitude_diff": self.longitude_diff,
            "sensor_array": self.sensor_array
        }
        return response

    # Entry Point
    def execute_request(self, request, motor_queue, gps_queue, sql_interface):
        self.unpack_request(request)
        self.motor_queue = motor_queue
        self.gps_queue = gps_queue
        self.sql_interface = sql_interface
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
        print(method())

    # Update information to send back to the server.
    def fetch(self):
        self.sensor_array = self.sql_interface.query_all()
        (self.latitude, self.longitude) = self.get_gps_reading()
        self.latitude_diff = self.latitude - float(self.app_latitude)
        self.longitude_diff = self.longitude - float(self.app_longitude)
        self.response = "fetch_OK"
        return "Running fetch()"

    def move(self):
        self.motor_queue.put(self.movement)
        self.fetch()
        return "Running move()"

    def test(self):
        self.fetch()
        self.response = "test_OK"
        return "Running test()"

    def get_gps_reading(self):
        (lat, long) = (Controller.previous_lat, Controller.previous_long)
        try:
            # remove items from the head of the queue
            while not self.gps_queue.empty():
                lat, long = self.gps_queue.get_nowait()
        except Exception as e:
            pass
        Controller.previous_lat = lat
        Controller.previous_long = long

        return lat, long



