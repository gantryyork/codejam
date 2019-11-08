#!/usr/bin/python3

import os

from http.server import BaseHTTPRequestHandler, HTTPServer

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):

        message = "Hello!\n"

        self.protocol_version = "HTTP/1.1"
        self.send_response(200)
        self.send_header("Content-Length", len(message))
        self.end_headers()

        self.wfile.write(bytes(message, "utf8"))
        return

    def do_POST(self):

        message = os.system('ls')

        self.protocol_version = "HTTP/1.1"
        self.send_response(200)
        self.send_header("Content-Length", len(message))
        self.end_headers()

        self.wfile.write(bytes(message, "utf8"))

def run():
    server = ('', 8080)
    httpd = HTTPServer(server, RequestHandler)
    httpd.serve_forever()
run()
