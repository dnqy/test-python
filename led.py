import time
import RPi.GPIO as GPIO

# configureation
pin = 17 # GPIOピン番号
wait = 0.5 # 0.5秒ずつ点灯‧消灯

# initialize GPIO
GPIO.setmode(GPIO.BCM) # 番号でピンを指定するモード
GPIO.setup(pin, GPIO.OUT) # GPIO を出⼒モード

# main
try:
  while True:
    GPIO.output(pin, 1)
    time.sleep(wait)
    GPIO.output(pin, 0)
    time.sleep(wait)
except KeyboardInterrupt:
  GPIO.cleanup()