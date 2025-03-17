import socket
import ai
import secret
from time import sleep
from random import randint

'''
RUN THIS ON COMPUTER

acts as a client and connects to the pi zero w
sends the ai prompts to the pi
'''

'testing for the sockets'
  # while True:
  #   msg = input("Input message: ")
  #   client_socket.sendall(msg.encode())
  #   response = client_socket.recv(secret.msg_max_size)
  #   print(response)

  #   if msg == "end":
  #     break

def main():
  print(secret.setup_prompt)
  ai.make_request(secret.setup_prompt)
  print(f"{secret.model} connected!")

  client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  client_socket.connect((secret.ip, secret.port))

  while True:
    msg = ai.make_request(secret.setup_prompt)
    print(msg)
    client_socket.sendall(msg.encode())

    if msg == "end":
      break

    sleep(randint(20, 25))

  client_socket.close()


if __name__ == "__main__":
  main()