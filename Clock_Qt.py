# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 22:52:19 2020

@author: Jeremy La Porte
Release V1.0
Clock using real time
"""

from PyQt5 import QtCore, QtGui, QtWidgets
import PyQt5.QtCore 
from PyQt5.QtGui import QPainter, QBrush, QPen
import pyqtgraph as pg
import datetime
import sys
import numpy as np


class Ui_MainWindow(object):
    
    def setupUi(self,MainWindow):
        MainWindow.resize(1200, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(10, 40,800,800))
        self.graphicsView.setObjectName("graphicsView")
        self.scene = QtWidgets.QGraphicsScene()
        self.scene.setSceneRect(0,0,1,1)

        self.graphicsView.setScene(self.scene)

        self.timer3 = pg.QtCore.QTimer()
        self.timer3.timeout.connect(self.graph)
        self.timer3.start(100) # refresh rate in ms
        self.graphicsView.setRenderHint(QtGui.QPainter.Antialiasing)
        
        # Color and width of the elements
        self.pen = QtGui.QPen(QtCore.Qt.red,2)
        self.pen2 = QtGui.QPen(QtCore.Qt.blue,3)
        self.pen3 = QtGui.QPen(QtCore.Qt.green,10)
        self.pen4 = QtGui.QPen(QtCore.Qt.black,2)

        self.graph()
        
        
    def graph(self):
        """ Plot de clock"""
        self.scene.clear()
        # for i in range(0,400,6):
        #     line=QtWidgets.QGraphicsLineItem(0 ,i,0,i)
        #     line.setPen(self.pen)
        #     self.scene.addItem(line)
        #     line2=QtWidgets.QGraphicsLineItem(i ,0,i,0)
        #     line2.setPen(self.pen)
        #     self.scene.addItem(line2)
        for j in range(0,360,30):
            line3=QtWidgets.QGraphicsLineItem(np.cos(j*np.pi/180)*200 ,np.sin(j*np.pi/180)*200,np.cos(j*np.pi/180)*150,np.sin(j*np.pi/180)*150) # long ticks around the clock
            line3.setPen(self.pen)
            self.scene.addItem(line3)
            if j/30 == 0:
                item_text = self.scene.addText('12', QtGui.QFont('Arial Black', 15))
            else:
                item_text = self.scene.addText(str(int(j/30)), QtGui.QFont('Arial Black', 15))
                
            item_text.setPos((np.sin(j*np.pi/180)*235)-13,-(np.cos(j*np.pi/180)*235)-13)
            
        for j in range(0,360,15):
            line4=QtWidgets.QGraphicsLineItem(np.cos(j*np.pi/180)*200 ,np.sin(j*np.pi/180)*200,np.cos(j*np.pi/180)*180,np.sin(j*np.pi/180)*180) # short ticks around the clock
            line4.setPen(self.pen)
            self.scene.addItem(line4)
            
        self.scene.addEllipse(-210,-210,420,420,pen = self.pen) #clock outline
        now = datetime.datetime.now() #get time
        sec = now.second/30
        mic = now.microsecond/(1000000/2)
        minute = now.minute/30
        y_sec = np.cos(sec*np.pi)*200
        x_sec = np.sin(sec*np.pi)*200
        y_mic = np.cos(mic*np.pi)*115
        x_mic = np.sin(mic*np.pi)*115
        y_min = np.cos(minute*np.pi)*150
        x_min = np.sin(minute*np.pi)*150
        self.scene.addLine(0,0,0,0,pen = self.pen3) # middle of the clock
        self.scene.addLine(0,0,x_sec,-y_sec,pen = self.pen2) # seconds
        self.scene.addLine(0,0,x_mic,-y_mic,pen = self.pen4) # microseconds
        self.scene.addLine(0,0,x_min,-y_min,pen =  QtGui.QPen(QtCore.Qt.black,5)) # minutes

        # self.scene.addLine(QtCore.QLineF(QtCore.QPointF(0,0),QtCore.QPointF(200,200)),pen = pen)
        

if __name__ == "__main__":
    """ Show and Close the window"""
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

