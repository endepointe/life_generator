import sys
import http.server
import socketserver
import json
# import lab1
import connect_socket

# with assistence with python server creation (completely new to it)
# https://wiki.python.org/moin/BaseHttpServer
# https://docs.python.org/3/library/socketserver.html#socketserver-tcpserver-example

HOST = ''
PORT = int(sys.argv[1]) 

class Base_Handler(socketserver.BaseRequestHandler):

  # general request handler
  def handle(self):
    self.data = bytes(connect_socket.lab1(), encoding="utf-8")
    self.request.sendall(self.data)

  # https://docs.python.org/3/library/http.server.html?highlight=do_get#http.server.SimpleHTTPRequestHandler.do_HEAD
  def do_HEAD(self):
    self.send_response(200)
    self.send_header("Content-type", "text/html")
    self.end_headers() 

  # https://docs.python.org/3/library/http.server.html?highlight=do_get#http.server.SimpleHTTPRequestHandler.do_GET
  def do_GET(self):
    ''' not ready to handle this yet
    self.send_response(200)
    self.send_header("Content-type", "text/html")
    self.end_headers()
    self.wfile.write("<html><head><title>lab1</title></head>")
    self.wfile.write("<body>")
    self.wfile.write("<h3>")
    self.wfile.write(bytes(connect_socket.lab1(), encoding="utf-8"))
    self.wfile.write("</h3>")
    self.wfile.write("</body><html>")
    '''

if __name__ == "__main__":
  # https://docs.python.org/3/library/socketserver.html
  with socketserver.TCPServer((HOST, PORT), Base_Handler) as httpd:

    print("\n\nserving at port", PORT, "\n\n")
    # run lab1 to get the resource
    print(connect_socket.lab1())

    try:
      httpd.serve_forever()
    except KeyboardInterrupt:
      pass
    httpd.server_close()