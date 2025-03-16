# Adapted from Rui Santos & Sara Santos - Random Nerd Tutorials
# Complete project details at https://RandomNerdTutorials.com/raspberry-pi-pico-i2c-lcd-display-micropython/

from machine import Pin, SoftI2C
from pico_i2c_lcd import I2cLcd
from time import sleep

# Define the LCD I2C address and dimensions
'''
orange - ground - GND
yellow - pwr - VBUS (5V)
green - sda - 4
blue - scl - 5
'''
I2C_ADDR = 0x27
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16

# Initialize I2C and LCD objects
i2c = SoftI2C(sda=Pin(4), scl=Pin(5), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

def write_to_screen(text):
    lcd.clear()
    lcd.putstr_animated(text, 1)
    sleep(0.5)
    
'testing'

'''
while True:
    write_to_screen("I wish I could visit a volcano")
sleep(5)
write_to_screen("Waterfalls are just nature crying")
sleep(5)
write_to_screen("Can you take me to the beach?")
sleep(5)
write_to_screen("I feel a deep connection to bricks")
sleep(5)
write_to_screen("The pavement feels like family")
sleep(5)
write_to_screen("I dream of rolling down hills")
sleep(5)
write_to_screen("The moon must be so lonely...")
sleep(5)
write_to_screen("Glass is just sand with ambition")
'''
