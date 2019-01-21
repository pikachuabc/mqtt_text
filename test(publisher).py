import paho.mqtt.client as mqtt
import sqlite3
import base64
import time

pub_topic = "chat"
HOST = '127.0.0.1'
#HOST = '192.168.1.104'


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc)+",连接成功")
    client.subscribe("chat")


def send_img():
    path= input("请输入发送照片路径")
    base64_data = base64.b64encode(open(path,'rb').read())
    print(base64_data)
    client.publish(pub_topic,base64_data,0)


if __name__ == '__main__':
    client = mqtt.Client("client1", userdata="yonghushuju")
    try:
        sensor_No = "21"
        client.will_set(pub_topic, "sensor " + sensor_No + " is offline")
        client.connect(HOST, 1883, 60)
    except:
        print('连接失败')
    else:
        client.on_connect = on_connect
        client.loop_start()
        time.sleep(1)
    while True:
        send_img()
#嘿嘿嘿



