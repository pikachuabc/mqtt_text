import paho.mqtt.client as mqtt
import sqlite3
import base64

pub_topic = "chat"
HOST = '127.0.0.1'
#HOST = '192.168.1.104'


def get_sensor_data():
    pass


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("chat")


def send_img():
    path = input("请输入发送文件路径及名称")
    base64_data = base64.b64encode(open(path,'rb').read())
    return base64_data


if __name__ == '__main__':
    client = mqtt.Client()
    try:
        sensor_No = "21"
        client.will_set(pub_topic, "sensor " + sensor_No + " is offline")
        client.connect(HOST, 1883, 60)
    except:
        print('连接失败')
    else:
        client.on_connect = on_connect
        client.loop_forever()
    while True:
        send_img()
#嘿嘿嘿



