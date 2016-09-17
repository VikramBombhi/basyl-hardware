import time
import serial

ser = serial.Serial("COM3", 9600)

while True:
    data = ser.readline()
    data = data.decode('utf-8') #convers data to string
    print(data)
