from http.server import HTTPServer, BaseHTTPRequestHandler
import random
from io import BytesIO

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        response_codes = [200,404,500]
        response_code = response_codes[random.randint(0,2)]
        self.send_response(response_code)
        self.end_headers()
        response = BytesIO()
        if response_code == 200:
            response.write(b'200 Oki')
        elif response_code == 404:
            response.write(b'404 Cannot found')
        elif response_code == 500:
            response.write(b'500 Something went wrong')
        self.wfile.write(response.getvalue())



httpd = HTTPServer(('', 8080), SimpleHTTPRequestHandler)
httpd.serve_forever()
