import time
import request
import serial


ser = serial.Serial("COM3", 9600) #TODO figure out port and baud rate

def getMean(array):
    return float(sum(numbers)) / max(len(numbers), 1)

if __name__ == "__main__":
    #TODO apparently the way windows assings ports requires a wait here
    params = {'token':'4BA0Ie0e5n'}
    moisture = []
    temperature = []
    light = []
    now = time.time()
    fiveMin = now + 300
    while True:
        data = ser.readline()
        data.decode('utf-8') #convers data to string
        data .rstrip() #removes newline shit
        data.replace('\x00', '') #removes \x00
        #TODO parse string and figure out what sensor the data come from
        moisture.append(moistureReading)
        temperature.append(temperatureReading)
        light.append(lightReading)
        if now > fiveMin:
            parms['moisture'] = getMean(moisture)
            del moisture[:]
            parms['temperature'] = getMean(temperature)
            del temperature[:]
            parms['light'] = getMean(light)
            del light[:]
            r = request.post("http://localhost:8080", data = parms)
            now = time.time()
