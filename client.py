import socket

ip = "192.168.8.25"
port = 4200

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((ip, port))

while True:
    msg = input("Input message: ")
    client_socket.sendall(msg.encode())
    response = client_socket.recv(1024)
    print(response)

    if msg == "end":
        break


client_socket.close()