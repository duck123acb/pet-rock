import socket

ip = "192.168.8.255"
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect(ip, 4200)