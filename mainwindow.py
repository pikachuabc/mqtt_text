# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from apscheduler.schedulers.qt import QtScheduler
import paho.mqtt.client as mqtt


class Ui_MainWindow(object):
    received_data = "#"

    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 300)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")

        self.sensor1 = QtWidgets.QLabel(self.centralWidget)
        self.sensor1.setGeometry(QtCore.QRect(140, 82, 81, 41))
        self.sensor1.setObjectName("sensor1")
        self.sensor1_data= QtWidgets.QLabel(self.centralWidget)
        self.sensor1_data.setGeometry(QtCore.QRect(220, 81, 81, 41))
        self.sensor1_data.setObjectName("sensor1_data")


        self.sensor2 = QtWidgets.QLabel(self.centralWidget)
        self.sensor2.setGeometry(QtCore.QRect(140, 120, 82, 41))
        self.sensor2.setObjectName("sensor2")
        self.sensor2_data= QtWidgets.QLabel(self.centralWidget)
        self.sensor2_data.setGeometry(QtCore.QRect(220, 121, 81, 41))
        self.sensor2_data.setObjectName("sensor2_data")

        MainWindow.setCentralWidget(self.centralWidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.sensor1.setText(_translate("MainWindow", "传感器1数据"))
        self.sensor1_data.setText(_translate("MainWindow", "#"))
        self.sensor2.setText(_translate("mMainWindow", "传感器2数据"))
        self.sensor2_data.setText(_translate("MainWindow", "#"))

    def change_label(self):
        Client_connect = MQTT_Client()
        Client_connect.MQTT()
        change=QtScheduler()
        change.add_job(func=self.change,trigger="interval", seconds = 2)
        change.start()

    def change(self):
        self.sensor1_data.setText(Ui_MainWindow.received_data)
        self.sensor1_data.repaint()


class MQTT_Client(Ui_MainWindow):
    client = mqtt.Client()
    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code " + str(rc))
        client.subscribe("chat")

    def on_message(self, client, userdata, msg):
        Ui_MainWindow.abc = msg.payload.decode()
        print(Ui_MainWindow.received_data)

    def MQTT(self):
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        HOST = '127.0.0.1'
        # HOST = '192.168.1.104'
        self.client.connect(HOST, 1883, 60)
        print("connect successfully")
        self.client.loop_start()






