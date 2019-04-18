# Stephen McDonnell
# 16/04/2019

from http.server import BaseHTTPRequestHandler, HTTPServer
from controller import Controller
import json
from sys import argv

# HTTP Request handler
class Server(BaseHTTPRequestHandler):

    # Used to ensure connection is stable with app on response
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    # Post request handling
    def do_POST(self):
        self._set_headers()
        # Get length of data packet
        length = int(self.headers["Content-Length"])
        # Read the amount of bytes specified in the header
        request = str(self.rfile.read(length), encoding="utf8")
        # Convert to post body data to json
        request = json.loads(request, encoding="utf8")
        print("Request: " + str(request))
        # Server control class
        response = Controller().execute_request(request)
        # Create Json response
        response = json.dumps(response)
        print("Response: " + response)
        # Send response to app
        self.wfile.write(bytes(response, encoding="utf8"))
        #self.wfile.write(bytes("\n\r", encoding="utf8"))


# Setup Server
def run(server_class=HTTPServer, handler_class=Server, port=8090):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print('Starting Http Server...')
    print("Server Address: " + str(server_address))
    httpd.serve_forever()


if __name__ == "__main__":
    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
