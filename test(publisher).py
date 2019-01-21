import paho.mqtt.client as mqtt
import sqlite3
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler


pub_topic = "chat"
HOST = '127.0.0.1'
#HOST = '192.168.1.104'
sensor_data = 29


def get_sensor_data():
    pass


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("chat")



def publish_Go():
    global sensor_data
    client.publish(pub_topic,sensor_data)
    print(sensor_data)
    sensor_data = sensor_data+1
    conn = sqlite3.connect('information.db')
    c = conn.cursor()
    c.execute("insert into sensor(dataq) values ('%d')" %(sensor_data))
    conn.commit()
    conn.close()




if __name__ == '__main__':
    client = mqtt.Client()
    try:
        #sensor_No = input("请输入传感器编号")
        sensor_No = "21"
        client.will_set(pub_topic, "sensor " + sensor_No + " is offline")
        client.connect(HOST, 1883, 60)
    except:
        print('连接失败')
    else:
        client.on_connect = on_connect
        client.loop_start()

        pub_timer = BackgroundScheduler()
        pub_timer.add_job(func=publish_Go, trigger="interval", seconds = 3)
        pub_timer.start()

        print("heiheihei")
        while 1:
            get_sensor_data()

