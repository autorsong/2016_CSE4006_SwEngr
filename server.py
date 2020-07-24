# -*- coding: utf-8 -*-

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import json
import main

PORT_NUMBER = 8080


class myHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        if self.path == "/send":
            length = int(self.headers['Content-length'])
            plan_data = self.rfile.read(length)

            recommend_data = main.calculate_eurailpass(json.loads(plan_data))

            self.send_response(200)
            self.send_header('Access-Control-Allow-Origin', "*")
            self.end_headers()
            self.wfile.write(json.dumps(recommend_data))
            return

try:
    server = HTTPServer(('', PORT_NUMBER), myHandler)
    print 'Started httpserver on port ', PORT_NUMBER

    server.serve_forever()

except KeyboardInterrupt:
    print ' received, shutting down the web server'
    server.socket.close()
