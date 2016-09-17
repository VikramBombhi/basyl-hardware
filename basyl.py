import time
import requests
import serial
import json

ser = serial.Serial("COM3", 9600)

def getMean(array):
    return float(sum(array)) / max(len(array), 1)

if __name__ == "__main__":
    params = {'arduino_token':'hello123'}
    moisture = []
    temperature = []
    light = []
    humidity = []
    timer = time.time() + 120
    while True:
        now = time.time()
        data = ser.readline()
        data = data.decode('utf-8') #convers data to string
        data = data.rstrip() #removes newline shit
        data = data.replace('\x00', '') #removes \x00
        data = data.split(':')
        if len(data)<2:
            data = ['empty', 404]
        print(data)
        data[1] = float(data[1])

        if data[0] == 'moisture':
            moisture.append(data[1])
        if data[0] == 'light':
            light.append(data[1])
        if data[0] == 'humidity':
            humidity.append(data[1])
        if data[0] == 'temp':
            temperature.append(data[1])

        if now > timer:
            print('timer done')
            params['moisture'] = getMean(moisture)
            params['temperature'] = getMean(temperature)
            params['light'] = getMean(light)
            params['humidity'] = getMean(humidity)
            del humidity[:]
            del moisture[:]
            del temperature[:]
            del light[:]
            postData = {'reading': json.dumps(params)}
            print(postData)
            r = requests.Session().post("https://17e8487b.ngrok.io/notify", data = postData)
            print('post request sent')
            timer = time.time() + 120
