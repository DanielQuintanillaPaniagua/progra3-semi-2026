from http.server import HTTPServer, SimpleHTTPRequestHandler
from urllib import parse
from urllib.parse import urlparse, parse_qs
import json

port = 3000

class miservidor(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.path = "/index.html"
        return SimpleHTTPRequestHandler.do_GET(self)

print(f"servidor corriendo en el puerto {port}")
server = HTTPServer(("localhost", port), miservidor)
server.serve_forever()