# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 07:05:11 2015

@author: quickfire
"""

import sys
from PyQt4 import QtGui, QtCore

s = 0   #set default attributes for watch items
m = 0
h = 0
c = 0
c2 = 0

        
class StopWatch(QtGui.QMainWindow):
    def __init__(self):
        super(StopWatch, self).__init__()
        
        self.setGeometry(25,25,300,200)
        self.setWindowTitle("StopWatch This.")
        
                    
        self.lcd = QtGui.QLCDNumber(self) #create an LCD widget for the stopwatch
        self.lcd.setGeometry(50,50,200,40)
        
        self.lcd2 = QtGui.QLCDNumber(self)
        self.lcd2.move(50,160)
        
        self.lcd3 = QtGui.QLCDNumber(self)
        self.lcd3.move(150,160)
        self.lcd3.setToolTip("Score : Tries")
        
        play = QtGui.QPushButton("Play",self)
        play.clicked.connect(self.player)
        play.setToolTip("Click to Play")
        play.move(50,15)
        
        
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.timehere) #create a timer function from QtCore
        
        starter = QtGui.QPushButton("Start", self)
        starter.clicked.connect(self.start)
        starter.move(50,100)
        
        resetter = QtGui.QPushButton("Reset", self)
        resetter.clicked.connect(self.reset)
        resetter.move(150,100)
        
        stopper = QtGui.QPushButton("Stop", self)
        stopper.clicked.connect(lambda: self.timer.stop()) #lambda function to stop stopwatch
        stopper.move(50,130)
        
        exitter = QtGui.QPushButton("Exit",self)
        exitter.clicked.connect(self.exithis)
        exitter.move(150,130)
        
        lapper = QtGui.QPushButton("Lap", self)
        lapper.clicked.connect(self.lap)
        lapper.move(150,15)
        
        
        
        self.show()

    def timehere(self): #start a clock display for the LCD
        global s,m,h
        
              
        if s < 59.99:
            s += .01
        else:
            if m < 59:
                s = 0
                m += 1
            elif h < 24 and m == 59:
                s = 0
                m = 0
                h += 1
            else:
                self.timer.stop(self)
                
        time = "{0}:{1}:{2}".format(h,m,"%.1f"%s)    
        self.lcd.setDigitCount(len(time))
        self.lcd.display(time)
               

    def start(self): #Starts the timer
        global s,m,h,c
        
        self.timer.start(10)
        
    def lap(self): #Creates an LCD view of the stopping point of a lap.
        global s,m,h
        
        secs = "{0}:{1}:{2}".format(h,m,"%.1f"%s)
        
        self.lcd2.setDigitCount(len(secs))
        self.lcd2.display(secs)

    def player(self): #Creates a game where stopping seconds to exact number
        global s,m,h,c,c2 #will give a score.
        
        secs = "{0}:{1}:{2}".format(h,m,"%.1f"%s)
        
        
        if int(secs[-1]) == 0: #convert 
            c += 1
        else:
            c2 += 1
        
        counter = "{0}:{1}".format(c,c2)
        
        self.lcd3.setDigitCount(len(counter))
        self.lcd3.display(counter)
        
        self.timer.stop()           

    def reset(self): #resets the timer to all 0 values.
        global s,m,h,c
        
        self.timer.stop()
        s = 0
        m = 0
        h = 0
        c = 0
        
        time = "{0}:{1}:{2}".format(h,m,'%.1f'%s)    
        self.lcd.setDigitCount(len(time))
        self.lcd.display(time)
        self.lcd2.display(time)
        
        counter = "{}".format(c)
        self.lcd3.setDigitCount(len(counter))
        self.lcd3.display(counter)
        
    def exithis(self): #creates a messagebox when clicking exit buttons/links
        choice = QtGui.QMessageBox.question(self, 'Close app?',
                                            "Are you sure you want to close app?",
                                            QtGui.QMessageBox.Yes|QtGui.QMessageBox.No)
                                            
        if choice == QtGui.QMessageBox.Yes:
            sys.exit() #Create a function to close the app.
            
        else:
            pass
      
        
def run_app(): #create a function to run the whole window.
    app = QtGui.QApplication(sys.argv)
    mainWindow = StopWatch()
    sys.exit(app.exec_())

run_app()    