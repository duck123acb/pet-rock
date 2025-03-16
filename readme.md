# Sentient Stone 🪨🤖
## Overview
Pet Rock is a quirky and interactive project that brings a sentient rock to life using [mistral](https://mistral.ai/):7b. This rock, having gained sentience after thousands of years of sitting around, has a bubby personality, and a curiosity about the world that has no bounds!

It’s powered by [Ollama](https://ollama.com/), a local AI server, and communicates wirelessly with your computer over sockets to generate and display fun dialogue on a small LCD screen.

## Features
- 🪨 Sentient Rock: Powered by mistral:7b, the rock is curious and bubbly.
- 💬 Dialogue Generation: Responds with short, poetic sentences!
- 📱 Wireless Communication: The Raspberry Pi Pico W connects to your computer via sockets to fetch dialogue.
- 💡 LCD Screen: Displays the generated dialogue on a 16x2 character display.
- 🔊 Buzzer: Emulates a 'speaking' noise with buzzing!

## Components
- Raspberry Pi Pico W: The brain of the operation.
- Ollama with Mistral:7b: AI model for generating dialogue.
- LCD 16x2: Displays the rock’s responses.
- Passive Buzzer: To emulate a speaking voice.
- Jumper Wires: To connect components like the LCD.
- Breadboard: To easily connect the hardware to the Pico.
- Computer: Capable of running Ollama and Mistral:7b.
- 3D Printed Case: To hold the hardware!

## Running Locally
### Prerequisites:
- Install [Python](https://www.python.org/)
- Install [Ollama](https://ollama.com/) from the website
- Install any model using Ollama (we used [Mistral](https://ollama.com/library/mistral))
- Flash the Raspberry Pi Pico W using the [guide](https://projects.raspberrypi.org/en/projects/get-started-pico-w/1). (You only need to follow this page!)
### Steps to Build:
1. Connect the Raspberry Pi Pico W to the breadboard
2. Connect the LCD to the breadboard. 
```
  Ground - GND
  POWER - VBUS (5V)
  SDA - GPIO 4
  SCL - GPIO 5
```

3. Connect the Passive Buzzer to the breadboard.
```
  One side - GND
  Other side - GPIO 16
```

### Steps to Run:
1. Add all of the files in the [picocode](https://github.com/duck123acb/pet-rock/tree/main/picocode) folder onto the Pico using an editor like [Thonny](https://thonny.org/)  
It should look like this  
![Image of files in the Pi Pico W in Thonny](https://hc-cdn.hel1.your-objectstorage.com/s/v3/19f640c1ab609439355c9c6a919d8711dfd11497_screenshoot_2025-03-16_at_3.49.54_pm.png)

2. Add `secret.py` to the Pico W and use the following format:
```
host = '0.0.0.0'
ip = "000.000.0.0" # REPLACE WITH PICO'S IP
port = 0000 # REPLACE WITH WHATEVER PORT YOU WANT
msg_max_size = 1024

ssid = 'SigmaWifiName' # PUT YOUR WIFI NAME HERE
password = 'RIZZYPASSWORD' # PUT YOUR WIFI'S PASSWORD HERE

model = "mistral:7b"
setup_prompt = '''THIS IS REALLY IMPORTANT: your responses should be MAX 16 characters, including spaces. Don't give quotes. ONLY use letters in your response. You DON'T have any senses. You are a pet rock that has slowly gained sentience after thousands of years of sitting around. You're naturally curious about the world. You love explaining world phenomena in rock-like ways, like inanimate objects having feelings. You should act like an anthropomorphic rock. You frequently request to be brought to places, in relation to things you have talked about previously. Other than requesting to be taken places, you don't ask any questions. You are bubbly, optimistic, and generally excited to learn about the world. When i say: "give me a line" generate something the rock would say.'''
```  
This will act as a config file. You can change the model to whatever model you downloaded from Ollama. You can edit the prompt to your liking as well.  

3. Add `secret.py` to the root of the project as well. Your project should look like this now.  
![File Structure](https://hc-cdn.hel1.your-objectstorage.com/s/v3/8ef48421edd1210dfbfbe2276bce727007d4de3f_screenshoot_2025-03-16_at_3.59.23_pm.png)

4. Run Ollama (or run `ollama serve` in your terminal idrk if ur not on a Mac)

5. Run `main.py` on both your computer and the Raspberry Pi Pico W. It may take a few minutes to setup. The Pico's LED will blink

6. Enjoy!