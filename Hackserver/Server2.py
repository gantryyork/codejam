# from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer # python2
from http.server import BaseHTTPRequestHandler, HTTPServer # python3
class HandleRequests(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        print( "Say something" )
        #self.wfile.write("received get request")
        
    def do_POST(self):
        '''Reads post request body'''
        #self._set_headers()
        #content_len = int(self.headers.getheader('content-length', 0))
        #post_body = self.rfile.read(content_len)
        self.wfile.write("received post request:<br>{}".format('Gantry'))

    def do_PUT(self):
        print("boogers")
        #self.do_POST()

host = ''
port = 8080
HTTPServer((host, port), HandleRequests).serve_forever()
