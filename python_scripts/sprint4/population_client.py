import socket

HOST = '127.0.0.1'
PORT = 5000 

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.connect((HOST,PORT))
  s.sendall(b'I am the population client')
  server_msg = s.recv(1024)

  print(server_msg.decode())