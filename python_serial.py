#imports
import time
import serial
import keyboard
import sys
from ast import literal_eval
sys.path.append('..')

#Dictionary
keyToASCII = {-1: -1, 2: 49, 30: 97, 49: 110, 13: 61, 12: 45, 42: 103, 15: 103, 58: 103, 41: 103, 11: 114, 28: 112, 14: 112, 43: 112, 87: 112, 88: 112, 57: 121, 93: 121, 541: 114, 29: 103, 91: 103, 56: 103, 1: 103}
    
# for i in range(1, 9):
#     keyToASCII[i+1] = i+48

for i in range(69, 84):
    keyToASCII[i] = 98

num = 2
for i in range(5):
    for j in range(3):
        keyToASCII[j+num] = 103
        keyToASCII[j+3+num] = 121
        keyToASCII[j+6+num] = 114
        keyToASCII[j+9+num] = 112
    num += 14
    
keyToASCII[12] = 45
keyToASCII[13] = 61
keyToASCII[74] = 51
keyToASCII[78] = 56
    
#Serial message
oldKey = 0
def print_pressed_keys(e):
    line = ', '.join(str(code) for code in keyboard._pressed_events)
    # '\r' and end='' overwrites the previous line.
    # ' '*40 prints 40 spaces at the end to ensure the previous line is cleared.
    line = line.strip()
    
    print(line)
    
    
    try:
        key = literal_eval(line)
        line = chr(keyToASCII[key])
        try:  
            s.write(line.encode('utf-8')) 
        except:
            print("port isn't available")
    except:
        key = -1
    
    # print(" "+line)
    
    
    
# Serial setup
s = serial.Serial()
s.baudrate = 9600
s.port = 'COM4'

s.open()

# while True:  # making a loop
#     # used try so that if user pressed other than the given key error will not be shown
    
#     if(keyboard.is_pressed(key)):
#         kp(key)
    
#     if(keyboard.is_pressed('o')):
#         break;
    
    
#Keyboard input
keyboard.hook(print_pressed_keys)
keyboard.wait("esc")

s.close()