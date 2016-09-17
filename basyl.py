import time
import request
import serial


ser = serial.Serial("COM4", 9600) #TODO figure out port and baud rate

def getMean(array):
    return float(sum(numbers)) / max(len(numbers), 1)

if __name__ == "__main__":
    #TODO apparently the way windows assings ports requires a wait here
    params = {}
    moisture = []
    temperature = []
    light = []
    now = time.time()
    fiveMin = now + 300
    while True:
        moistureReading = moistureSer.readline() #TODO figure out how to get this individul data latter
        temperatureReading = temperatureSer.readline() #TODO figure out how to get this individul data latter
        lightReading = lightSer.readline() #TODO figure out how to get this individul data latter
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
