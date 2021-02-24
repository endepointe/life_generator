import socket

HOST = '127.0.0.1'
PORT = 5000


print("Opening socket...")
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((HOST,PORT))

print("Listening...")
while True:
    datagram = server.recv(1024)
    if not datagram:
        break
    else:
        print("-" * 20)
        print(datagram.decode('utf-8'))
        if "DONE" == datagram.decode('utf-8'):
            break
print("-" * 20)
print("Shutting down...")
server.close()
print("Done")