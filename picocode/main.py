import network
import socket
from time import sleep
import machine
import rp2
import sys
import secret
import screen

led = machine.Pin("LED", machine.Pin.OUT)

def connect():
    #Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(secret.ssid, secret.password)
    while wlan.isconnected() == False:
        if rp2.bootsel_button() == 1:
            sys.exit()
        print('Waiting for connection...')
        led.on()
        sleep(0.5)
        led.off()
        sleep(0.5)
    ip = wlan.ifconfig()[0]
    print(f'Connected on {ip}')
    led.on()
    return ip


ip = connect()


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((secret.host, secret.port))
server_socket.listen(1)

print("Waiting for connection...")
client_socket, client_address = server_socket.accept()
for _ in range(3):
    led.on()
    sleep(0.2)
    led.off()
    sleep(0.2)
print(f"Connected to {client_address}")


while True:
  data = client_socket.recv(secret.msg_max_size)
  if data == b"end":
    break

  screen.write_to_screen(data.decode("utf-8"))
  

client_socket.close()
server_socket.close()

