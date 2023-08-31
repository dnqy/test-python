import paho.mqtt.client as mqtt

#configuration
host = 'ec2-3-112-43-17.ap-northeast-1.compute.amazonaws.com'
port = 1883
topic = 'test'

print("Start subscriber: topic {} on {}:{}".format(topic, host, port))

def on_connect(client, userdata, flags, respons_code):
    print('status {0}'.format(respons_code))
    client.subscribe(topic)

def on_message(client, userdata, msg):
  print(str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

## main
client.connect(host, port, 60)
client.loop_forever()