import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '0.0.0.0'
port = 4200

server_socket.bind((host, port))
server_socket.listen(1)

print("Waiting for connection...")
client_socket, client_address = server_socket.accept()
print(f"Connected to {client_address}")

while True:
  data = client_socket.recv(1024)
  if data == b"end":
    break
  print(f"recieved {data}")
  client_socket.sendall(b"hello")

client_socket.close()
server_socket.close()