from http.server import HTTPServer, BaseHTTPRequestHandler
from io import BytesIO
from datetime import datetime,timezone
import ssl

# Simple HTTP(s) web service to host files and be able to do simple request/response changes.
# Inspired by: https://blog.anvileight.com/posts/simple-python-http-server/



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
        response.write(body)
        self.wfile.write(response.getvalue())
        # TODO: add name of tile to dump file.
        # TODO: Dump file to console in well formatted JSON ?
        print(body)
        f = open('dumps/%s.raw' % datetime.now(timezone.utc).isoformat(), "wb")
        f.write(body)
        f.close()


def main():
    try:
        httpd = HTTPServer(('', 8888), SimpleHTTPRequestHandler)
        httpd.socket = ssl.wrap_socket(httpd.socket, keyfile="certificates/privkey1.pem", certfile="certificates/cert1.pem", server_side=True)
        print ("started https-server on port 8888...")

        httpd.serve_forever()
    except KeyboardInterrupt:
        print ("^C received, shutting down server")
        httpd.socket.close()

if __name__ == '__main__':
    main()