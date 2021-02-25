import socket

PORT = 5000
HOST = 'localhost'
test_data = ['one', 'two']

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  # the microserver location that all other services will connect to
  s.bind((HOST, PORT))
  # enable a server to accept connections
  s.listen(5)
  flag = 1
  while flag: # run the server until told to disconnect.
    (client_socket, addr) = s.accept()
    #server_data = b''
    with client_socket: 
      server_data = bytes(str(test_data), encoding="utf8")
      while flag:
        client_data = client_socket.recv(4096)
        #use the data received by the client to return some data
        print("client sent: ", client_data)
        if not client_data:
          break
        if "DONE" == client_data.decode('utf-8'):
          print('client initiated disconnect')
          flag = 0
          #client_socket.close()
          break
        client_socket.sendall(server_data)
    client_socket.close()

  print('client disconnected')