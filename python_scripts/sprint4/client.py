''' EXAMPLE ONLY
import socket
import os

HOST = '127.0.0.1'
PORT = 5000 

print("Connecting...")
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.connect((HOST,PORT))
print("Ready.")
print("Ctrl-C to quit.")
print("Sending 'DONE' shuts down the server and quits.")
while True:
  try:
    x = input("> ")
    if "" != x:
      print("SEND:", x)
      client.send(x.encode('utf-8'))
      if "DONE" == x:
        print("Shutting down.")
        break
  except KeyboardInterrupt as k:
    print("Shutting down.")
    client.close()
    break
'''