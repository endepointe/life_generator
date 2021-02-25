import socket

PORT = 5000 
HOST = 'localhost'
#list_object = ['list', 'of', 'things', 123]
list_object = 'DONE'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  '''
  connect to the microservice server
  '''
  s.connect((HOST,PORT))
  s.sendall(bytes(str(list_object), encoding="utf8"))
  #s.sendall(b'request data sent from the population generator microservice')
  server_msg = s.recv(4096)

print("server sent", server_msg.decode())