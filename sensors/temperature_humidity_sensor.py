import time
from seeed_dht import DHT

sensor = DHT("11", 16)

while True:
    humidity, temp = sensor.read()
    print(f'Temperature: {temp}°C, Humidity: {humidity}%')

    time.sleep(5)
