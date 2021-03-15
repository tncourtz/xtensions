from http.server import HTTPServer, BaseHTTPRequestHandler
from io import BytesIO
from datetime import datetime,timezone




class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        try:
            if self.path.endswith(".json"):
                f = open(self.path[1:], 'rb')
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(f.read())
                f.close()
                return
            else:
                self.send_response(200, "Thanks")
                self.end_headers()
                return

        except IOError:
            self.send_error(404,'File Not Found: %s' % self.path)


    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        self.send_response(200)
        self.end_headers()
        response = BytesIO()
        response.write(b'Received: ')
        response.write(body)
        self.wfile.write(response.getvalue())
        f = open('dumps/%s.raw' % datetime.now(timezone.utc).isoformat(), "wb")
        f.write(body)
        f.close()



# import ssl
# see https://blog.anvileight.com/posts/simple-python-http-server/#example-with-ssl-support
#httpd.socket = ssl.wrap_socket (httpd.socket, 
#        keyfile="path/to/key.pem", 
#        certfile='path/to/cert.pem', server_side=True)


def main():
    try:
        server = HTTPServer(('', 8888), SimpleHTTPRequestHandler)
        print ("started httpserver on port 8888...")
        server.serve_forever()
    except KeyboardInterrupt:
        print ("^C received, shutting down server")
        server.socket.close()

if __name__ == '__main__':
    main()