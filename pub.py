import time
import paho.mqtt.client as mqtt

#configuration
host = 'ec2-3-112-43-17.ap-northeast-1.compute.amazonaws.com' 
port = 1883 
topic = 'test' 
wait = 1

# mqtt initialize
client = mqtt.Client()
client.connect(host, port=port)

# loop
try:
  i = 0
  client.loop_start()
  while True:
    client.publish(topic, 'hello'+str(i))
    time.sleep(wait)
    i += 1
except KeyboardInterrupt:
  client.disconnect()