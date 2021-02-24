import socket

HOST = '127.0.0.1'
PORT = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.bind((HOST, PORT))
  s.listen()
  conn, addr = s.accept()
  with conn: 
    print('I am the life server, connected by', addr)
    while 1:
      data = conn.recv(1024)
      if not data:
        break
      conn.sendall(data)