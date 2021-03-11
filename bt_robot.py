#!/usr/bin/python3
from bluedot import BlueDot
import RPi.GPIO as GPIO
from signal import pause
import time
import subprocess
import os

from picamera import PiCamera
from datetime import datetime

cam = PiCamera()
cam.vflip = True

name = datetime.now().strftime('%c')

GPIO.setmode(GPIO.BOARD)

GPIO.setup(31, GPIO.OUT)
GPIO.setup(33, GPIO.OUT)
GPIO.setup(35, GPIO.OUT)
GPIO.setup(37, GPIO.OUT)
GPIO.setup(32, GPIO.OUT)
GPIO.setup(36, GPIO.OUT)
GPIO.setup(38, GPIO.OUT)
GPIO.setup(40, GPIO.OUT)
GPIO.setup(23, GPIO.IN)
GPIO.setup(29, GPIO.IN)

try:









    def dpad(pos):
        if pos.top:
            print("Framåt!")

            GPIO.output(31, True)
            GPIO.output(33, True)
            GPIO.output(35, False)
            GPIO.output(37, True)
            GPIO.output(32, True)
            GPIO.output(36, True)
            GPIO.output(38, True)
            GPIO.output(40, False)
        elif pos.bottom:
            print("Backar")
 
            GPIO.output(31, True)
            GPIO.output(33, True)
            GPIO.output(35, True)
            GPIO.output(37, False)
            GPIO.output(32, True)
            GPIO.output(36, True)
            GPIO.output(38, False)
            GPIO.output(40, True)
            
            
        elif pos.left:
            print("Backar vänster")
            #TEst att sätta 31 -37 True alla
            GPIO.output(31, True)
            GPIO.output(33, True)
            GPIO.output(35, False)
            GPIO.output(37, True)
            GPIO.output(32, True)
            GPIO.output(36, True)
            GPIO.output(38, False)
            GPIO.output(40, True)
                
            
            
            
        elif pos.right:
            print("Backar höger")
            #TEst att sätta 36-40 True
            GPIO.output(31, True)
            GPIO.output(33, True)
            GPIO.output(35, True)
            GPIO.output(37, False)
            GPIO.output(32, True)
            GPIO.output(36, True)
            GPIO.output(38, True)
            GPIO.output(40, False)
            
        elif pos.middle:

            print("Tar en bild avvakta 2 sek!!!")
            GPIO.output(31, False)
            GPIO.output(33, False)
            GPIO.output(35, False)
            GPIO.output(37, False)
            GPIO.output(32, False)
            GPIO.output(36, False)
            GPIO.output(38, False)
            GPIO.output(40, False)
            cam.capture('/home/pi/bilder/' + name + '.jpeg')
            os.system('/home/pi/robot/send_mail.py')
            




    def stop():

        GPIO.output(31, False)
        GPIO.output(33, False)
        GPIO.output(35, False)
        GPIO.output(37, False)
        GPIO.output(32, False)
        GPIO.output(36, False)
        GPIO.output(38, False)
        GPIO.output(40, False)



    bd = BlueDot()
    bd.when_pressed = dpad
    bd.when_released = stop
    pause()

except KeyboardInterrupt:
    
    print("STänger ner program")
