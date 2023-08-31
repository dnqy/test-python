import time
import RPi.GPIO as GPIO
import dht11
import datetime

# configuration
pin = 14
wait = 1

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using pin 14
instance = dht11.DHT11(pin = pin)

# loop
try:
  while True:
    result = instance.read()
    if result.is_valid():
      print("Last valid input: " + str(datetime.datetime.now()))
      print("Temperature: {} C".format(result.temperature))
      print("Humidity: {} %%".format(result.humidity))
    time.sleep(wait)
except KeyboardInterrupt:
  GPIO.cleanup()