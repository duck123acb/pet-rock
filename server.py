import socket
import secret

'''
RUN THIS ON THE PI ZERO W

acts as a server, and receives dialogue from the client
displays the dialogue on an 16x02 character LCD screen
'''

# socket comms setup
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((secret.host, secret.port))
server_socket.listen(1)

print("Waiting for connection...")
client_socket, client_address = server_socket.accept()
print(f"Connected to {client_address}")

'socket comms testing'
# while True:
#   data = client_socket.recv(secret.msg_max_size)
#   if data == b"end":
#     break

#   print(f"recieved {data}")
#   client_socket.sendall(b"hello")

while True:
  data = client_socket.recv(secret.msg_max_size)
  if data == b"end":
    break

  print(data)
  # display data on the display
  

client_socket.close()
server_socket.close()