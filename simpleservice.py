from http.server import HTTPServer, BaseHTTPRequestHandler
from io import BytesIO
from datetime import datetime,timezone
# import ssl
import logging

# Simple HTTP(s) web service to host files and be able to do simple request/response changes.
# Inspired by: https://blog.anvileight.com/posts/simple-python-http-server/



class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    # supress all standard logging.
    def log_message(self, format, *args):
        return

    def do_GET(self):
        # 192.168.1.1 - - [21/Apr/2021 10:22:45] "GET /favicon.ico HTTP/1.1" 200 -
        logging.debug("%s %s", self.client_address[0], self.requestline)
        for header in self.headers:
            logging.info("HEADER %s:%s", header, self.headers[header])

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
        logging.debug("%s %s", self.client_address[0], self.requestline)
        for header in self.headers:
            logging.info("HEADER %s:%s", header, self.headers[header])


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
    logging.basicConfig(
        encoding='utf-8',
        level=logging.DEBUG,
        format='%(asctime)s.%(msecs)03d %(levelname)8s %(module)s (%(funcName)s): %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        )
    try:
        httpd = HTTPServer(('127.0.0.1', 8888), SimpleHTTPRequestHandler)
        # httpd.socket = ssl.wrap_socket(httpd.socket, keyfile="certificates/privkey2.pem", certfile="certificates/cert2.pem", server_side=True)
        logging.info("Started http-server on port 8888...")

        httpd.serve_forever()
    except KeyboardInterrupt:
        logging.info("^C received, shutting down server")
        httpd.socket.close()

if __name__ == '__main__':
    main()
