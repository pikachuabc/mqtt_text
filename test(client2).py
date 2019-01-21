import paho.mqtt.client as mqtt

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("chat")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic + ":" + msg.payload.decode())

client = mqtt.Client()
client.on_connect = on_connect
"""回调函数，这里的client.on_connect是作为属性的，需要传入函数的地址"""
client.on_message = on_message
HOST = '127.0.0.1'
#HOST = '192.168.1.104'
client.connect(HOST, 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()