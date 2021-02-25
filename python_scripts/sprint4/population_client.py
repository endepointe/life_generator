import socket
import sys

print(sys.argv)

PORT = 5000 
HOST = 'localhost'

# arguments are passed in as a space separated string:
#   input_item_type,input_item_category,input_number_to_generate
# Category list and CSV column names can be found here:
#     https://www.kaggle.com/PromptCloudHQ/toy-products-on-amazon
# For now, just use: Toys Hobbies <some integer>

req = sys.argv[1:]

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

  s.connect((HOST,PORT))
  s.sendall(bytes(str(req), encoding="utf8"))
  server_msg = s.recv(4096)

print("server sent", server_msg.decode("utf-8"))