import socket

HOST = '127.0.0.1'
PORT = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.bind((HOST, PORT))
  s.listen(5)
  conn, addr = s.accept()
  with conn: 
    print('I am the life server, connected by', addr)
    client_msg = ''
    while 1:
      data = conn.recv(1024)
      client_msg += data.decode()
      print(client_msg)
      if not data:
        break
      conn.sendall(data)
    conn.close()
    print('population client disconnected')