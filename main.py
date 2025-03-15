import socket
import ai
import secret

'''
RUN THIS ON COMPUTER

acts as a client and connects to the pi zero w
sends the ai prompts to the pi
'''

ai.make_request(secret.setup_prompt)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((secret.ip, secret.port))

'testing for the sockets'
# while True:
#   msg = input("Input message: ")
#   client_socket.sendall(msg.encode())
#   response = client_socket.recv(secret.msg_max_size)
#   print(response)

#   if msg == "end":
#     break

while True:
  msg = ai.make_request("give me a line")
  client_socket.sendall(msg.encode())

  if msg == "end":
    break

client_socket.close()