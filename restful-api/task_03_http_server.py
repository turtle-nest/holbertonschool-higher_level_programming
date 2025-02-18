#!/usr/bin/python3
"""
Simple API using Python's http.server module.

This API handles GET requests on multiple endpoints:
- "/" : Returns a simple text message.
- "/data" : Returns a JSON object with sample data.
- "/status" : Returns the API status as text.
For any other endpoint, a 404 Not Found response is returned.
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class SimpleAPIHandler(BaseHTTPRequestHandler):
    """
    HTTP request handler for the Simple API.

    This class handles GET requests and returns responses
    based on the requested URL.
    """

    def do_GET(self):
        """
        Handles GET requests.

        Implemented routes:
        / : Returns a text message.
        /data : Returns a JSON response with sample data.
        /status : Returns "OK" to indicate that the API is operational.
        Others : Returns a 404 error with the message "Endpoint not found".
        """
        if self.path == '/':
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == '/data':
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_header()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode('utf-8'))

        elif self.path == '/status':
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_header()
            self.wfile.write(b"OK")

        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_header()
            self.wfile.write(b"Endpoint not found")


def run(server_class=HTTPServer, handler_class=SimpleAPIHandler, port=8000):
    """
    Starts the HTTP server.

    Args:
        server_class (HTTPServer): HTTP server class to use.
        handler_class (BaseHTTPRequestHandler): Request handler class.
        port (int): Port on which the server will be started.
    """
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting HTTP server on port {port}...")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
