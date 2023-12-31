import time
import RPi.GPIO as GPIO
import dht11
import datetime
import paho.mqtt.client as mqtt

# configuration
host = 'ec2-3-112-43-17.ap-northeast-1.compute.amazonaws.com' 
port = 1883 
topic = 'test' 
pin = 14
wait = 1

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# mqtt initialize
client = mqtt.Client()
client.connect(host, port=port)

# read data using pin 14
instance = dht11.DHT11(pin = pin)

# loop
try:
  while True:
    result = instance.read()
    if result.is_valid():
      client.publish("Last valid input: " + str(datetime.datetime.now()))
      client.publish("Temperature: {} C".format(result.temperature))
      client.publish("Humidity: {} %%".format(result.humidity))
    time.sleep(wait)
except KeyboardInterrupt:
  GPIO.cleanup()