#!/usr/bin/python3

import RPi.GPIO as GPIO
from datetime import datetime
from picamera import PiCamera
import time
#import keyboard
import random
import termios
import tty
import sys
import os

os.system("sudo service motion stop")


GPIO.setmode(GPIO.BOARD)

GPIO.setup(31, GPIO.OUT)
GPIO.setup(33, GPIO.OUT)
GPIO.setup(35, GPIO.OUT)
GPIO.setup(37, GPIO.OUT)

kamera = PiCamera()
namn = datetime.now().strftime('%c')

def cen_echo():
    cen_trigger = 7
    cen_echo = 11
    GPIO.setup(cen_trigger, GPIO.OUT)
    GPIO.setup(cen_echo, GPIO.IN)

    GPIO.output(cen_trigger, GPIO.LOW)

    #print ("Waiting for sensor to settle")

    time.sleep(0.2)

    #print ("Calculating distance")

    GPIO.output(cen_trigger, GPIO.HIGH)

    time.sleep(0.00001)

    GPIO.output(cen_trigger, GPIO.LOW)

    while GPIO.input(cen_echo)==0:
        pulse_start_time = time.time()
    while GPIO.input(cen_echo)==1:
        pulse_end_time = time.time()

    pulse_duration = pulse_end_time - pulse_start_time
    distance = round(pulse_duration * 17150, 2)
   # print ("Distance:",distance,"cm")
    if distance < 30:
        print("Center")
    if distance < 30: 
               
        stopit()
        kamera.capture('/home/pi/robot/bilder/'+namn+'.jpeg')
        os.system("/home/pi/robot/send_mail.py")
                #print("Distance:",distance,"cm")
                #back_right()
        r = random.randint(0,11)
        if r > 5:
                    
            back_right()
            time.sleep(0.5)
                
                            
        else:
                    
            back_left()
            time.sleep(0.5)
           
        
                    
                
    else:
        forward()


def left_echo():
    left_trigger = 40
    left_echo = 15
    GPIO.setup(left_trigger, GPIO.OUT)
    GPIO.setup(left_echo, GPIO.IN)

    GPIO.output(left_trigger, GPIO.LOW)

    #print ("Waiting for sensor to settle")

    time.sleep(0.2)

   # print ("Calculating distance")

    GPIO.output(left_trigger, GPIO.HIGH)

    time.sleep(0.00001)

    GPIO.output(left_trigger, GPIO.LOW)

    while GPIO.input(left_echo)==0:
        pulse_start_time = time.time()
    while GPIO.input(left_echo)==1:
        pulse_end_time = time.time()

    pulse_duration = pulse_end_time - pulse_start_time
    distance = round(pulse_duration * 17150, 2)
   # print ("Distance:",distance,"cm")
    if distance < 30:
        print("Left")
        back_left()
        time.sleep(0.2)



def right_echo():
    right_trigger = 12
    right_echo = 13
    GPIO.setup(right_trigger, GPIO.OUT)
    GPIO.setup(right_echo, GPIO.IN)

    GPIO.output(right_trigger, GPIO.LOW)

    #print ("Waiting for sensor to settle")

    time.sleep(0.2)

    #print ("Calculating distance")

    GPIO.output(right_trigger, GPIO.HIGH)

    time.sleep(0.00001)

    GPIO.output(right_trigger, GPIO.LOW)

    while GPIO.input(right_echo)==0:
        pulse_start_time = time.time()
    while GPIO.input(right_echo)==1:
        pulse_end_time = time.time()

    pulse_duration = pulse_end_time - pulse_start_time
    distance = round(pulse_duration * 17150, 2)
   # print ("Distance:",distance,"cm")
    if distance < 30:
        print("right")
        back_right()
        time.sleep(0.2)


def forward():
    
    GPIO.output(31, True)
    GPIO.output(33, False)
    GPIO.output(35, True)
    GPIO.output(37, False)


def reverse():
    
    GPIO.output(31, False)
    GPIO.output(33, True)
    GPIO.output(35, False)
    GPIO.output(37, True)

def back_left():
    
    GPIO.output(31, False)
    GPIO.output(33, True)
    GPIO.output(35, False)
    GPIO.output(37, False)
            
def back_right():
    
    GPIO.output(31, False)
    GPIO.output(33, False)
    GPIO.output(35, False)
    GPIO.output(37, True)

def stopit():
    
    GPIO.output(31, False)
    GPIO.output(33, False)
    GPIO.output(35, False)
    GPIO.output(37, False)



try:

    while True:
        #GPIO.setmode(GPIO.BOARD)
        cen_echo()
        left_echo()
        right_echo()
     
            
        
          
                
            
                
 

    

except KeyboardInterrupt:
    print("Robot stopping")
    stopit()

    GPIO.cleanup()
