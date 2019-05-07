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





kamera = PiCamera()
namn = datetime.now().strftime('%c')

try:

    while True:
        GPIO.setmode(GPIO.BOARD)
        
        #forward()
        PIN_TRIGGER = 7
        PIN_ECHO = 11
        
          
            
        def init():
            GPIO.setup(31, GPIO.OUT)
            GPIO.setup(33, GPIO.OUT)
            GPIO.setup(35, GPIO.OUT)
            GPIO.setup(37, GPIO.OUT)
        
        def forward():
            init()
            GPIO.output(31, True)
            GPIO.output(33, False)
            GPIO.output(35, True)
            GPIO.output(37, False)


        def reverse():
            init()
            GPIO.output(31, False)
            GPIO.output(33, True)
            GPIO.output(35, False)
            GPIO.output(37, True)

        def back_left():
            init()
            GPIO.output(31, False)
            GPIO.output(33, True)
            GPIO.output(35, False)
            GPIO.output(37, False)
            
        def back_right():
            init()
            GPIO.output(31, False)
            GPIO.output(33, False)
            GPIO.output(35, False)
            GPIO.output(37, True)

        def stopit():
            init()
            GPIO.output(31, False)
            GPIO.output(33, False)
            GPIO.output(35, False)
            GPIO.output(37, False)
        
        forward()
        
        GPIO.setup(PIN_TRIGGER, GPIO.OUT)
        GPIO.setup(PIN_ECHO, GPIO.IN)

        GPIO.output(PIN_TRIGGER, GPIO.LOW)

       # print ("Waiting for sensor to settle")

        time.sleep(0.2)

        #print ("Calculating distance")

        GPIO.output(PIN_TRIGGER, GPIO.HIGH)

        time.sleep(0.00001)

        GPIO.output(PIN_TRIGGER, GPIO.LOW)

        while GPIO.input(PIN_ECHO)==0:
            pulse_start_time = time.time()
        while GPIO.input(PIN_ECHO)==1:
            pulse_end_time = time.time()

        pulse_duration = pulse_end_time - pulse_start_time
        distance = round(pulse_duration * 17150, 2)
       # print ("Distance:",distance,"cm")
       
      
            
        
            
        if distance < 30:
            print("Hinder upptäckt",distance,"cm, Tar en bild och epostar den sen väljer annan väg")
            stopit()
            kamera.capture('/home/pi/robot/bilder/'+namn+'.jpeg')
            os.system("/home/pi/robot/send_mail.py")
	    #print("Distance:",distance,"cm")
            #back_right()
            r = random.randint(0,11)
            if r > 5:
                print("Backar höger")
                back_right()
                time.sleep(0.5)
               # print("Skickar bild på hindert....")
               # os.system("/home/pi/robot/send_mail.py")
                
            else:
                print("Backar vänster")
                back_left()
                time.sleep(0.5)
                #print("Skickar bild på hindert....")
                #os.system("/home/pi/robot/send_mail.py")
        
            
        
            
                
        else:
            forward()


            def getch():
                fd = sys.stdin.fileno()
                old_settings = termios.tcgetattr(fd)
                try:
                    tty.setraw(sys.stdin.fileno())
                    ch = sys.stdin.read(1)
             
                finally:
                    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
                return ch
                
                    
            char = getch() 


            if (char == "s"):
                print("Manuellt ändrar kurser")
                back_left()
                time.sleep(0.2)

            elif (char == 'a'):
                print("Manuellt ändrar kursen")
                back_right()
                time.sleep(0.2)    

except KeyboardInterrupt:
    print("Robot stannar")
    stopit()

    GPIO.cleanup()
    #os.system("/home/pi/robot/send_mail.py")
