# https://docs.python.org/3/library/pdb.html
import pdb
# https://docs.python.org/3/library/socket.html
import socket

def lab1():
  port = 80 
  host = 'gaia.cs.umass.edu'
  uri1 = '/wireshark-labs/INTRO-wireshark-file1.html'
  uri2 = '/wireshark-labs/HTTP-wireshark-file1.html'
  req_string = "GET " + uri2 + " HTTP/1.1\r\nHost:" + host + "\r\n\r\n"
  address = (host, port)
  buffer_size = 4096 
  res_size = 0

  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # connect a remote socket at address
    # https://docs.python.org/3/library/socket.html?#socket.socket.connect
    s.connect(address)

    # ... could use this ...
    # send data to the socket. in this case, it is the resource uri with
    # with other resource parameters
    # https://docs.python.org/3/library/socket.html?#socket.socket.send
    # s.send(bytes(req_string, encoding="utf-8"))
    #
    # ... but used this ...
    # added benefit of using sendall instead of send is that the sendall
    # continues to send data from the parameter until all data is sent or
    # or there is an error
    # https://docs.python.org/3/library/socket.html?#socket.socket.sendall
    s.sendall(bytes(req_string, encoding="utf-8"))
    # until a system interrupt is given
    while True:
      # get the data from the remote socket
      # https://docs.python.org/3/library/socket.html?#socket.socket.connect 
      # buffer_size can be set to a power of 2 but won't produce easily
      # readable results. Using a realistic buffer size will help. Either
      # way, we will get all the data from the resource.
      data = s.recv(buffer_size)

      res_size += len(data)

      print("[RECV] - length: ", res_size)

      # if there is nothing left in the res, nothing at all, sad face
      if not data:
        print(" :-( ")

        break
      return data.decode()