# !/usr/bin/python
import RPi.GPIO as gpio
import time
import random
#from picamera import PiCamera
from datetime import datetime
import subprocess
import os

## Ingen skillnad jämfört med side_Way_Robot.py men denna kan ändringar göras i utan att riskera att det pajar helt

class Robot:
    def __init__(self): #Setting up all gpio pins

        gpio.setmode(gpio.BOARD)
        gpio.setup(11, gpio.OUT)
        gpio.setup(13, gpio.OUT)
        gpio.setup(15, gpio.OUT)
        gpio.setup(12, gpio.OUT)
        gpio.setup(16, gpio.OUT)
        gpio.setup(18, gpio.OUT)
        gpio.setup(33, gpio.OUT)
        gpio.setup(35, gpio.OUT)
        gpio.setup(37, gpio.OUT)
        gpio.setup(36, gpio.OUT)
        gpio.setup(38, gpio.OUT)
        gpio.setup(40, gpio.OUT)

        while True:
            self.right_sensor()
            self.left_sensor()

    def left_sensor(self):
        #print("left sensor")

        self.PIN_TRIGGER = 7
        self.PIN_ECHO = 32

        gpio.setup(self.PIN_TRIGGER, gpio.OUT)

        gpio.setup(self.PIN_ECHO, gpio.IN)

        gpio.output(self.PIN_TRIGGER, gpio.LOW)

        

        time.sleep(0.1)

        gpio.output(self.PIN_TRIGGER, gpio.HIGH)

        time.sleep(0.00001)

        gpio.output(self.PIN_TRIGGER, gpio.LOW)

        while gpio.input(self.PIN_ECHO) == 0:
            pulse_start_time = time.time()

        while gpio.input(self.PIN_ECHO) == 1:
            pulse_end_time = time.time()

        pulse_duration = pulse_end_time - pulse_start_time

        distance = round(pulse_duration * 17150, 2)

        print("Avstånd:", distance, "cm")
        if distance < 10:
            self.stopit()
            print("Vänster sensor")
           
            time.sleep(1.5)
            
            res = random.randint(0, 11)
            if res > 5:

                self.right()
                print("Svänger höger")
                time.sleep(1.5)


            else:

                self.left()
                print("Svänger Vänster")
                time.sleep(1.5)


        else:
            self.forward()
         
         
    def right_sensor(self):
       # print("right sensor")

        self.PIN_TRIGGER = 29
        self.PIN_ECHO = 31

        gpio.setup(self.PIN_TRIGGER, gpio.OUT)

        gpio.setup(self.PIN_ECHO, gpio.IN)

        gpio.output(self.PIN_TRIGGER, gpio.LOW)

        

        time.sleep(0.1)

        gpio.output(self.PIN_TRIGGER, gpio.HIGH)

        time.sleep(0.00001)

        gpio.output(self.PIN_TRIGGER, gpio.LOW)

        while gpio.input(self.PIN_ECHO) == 0:
            pulse_start_time = time.time()

        while gpio.input(self.PIN_ECHO) == 1:
            pulse_end_time = time.time()

        pulse_duration = pulse_end_time - pulse_start_time

        distance = round(pulse_duration * 17150, 2)

        print("Avstånd:", distance, "cm")
        if distance < 10:
            self.stopit()
            print("Höger sensor")
           
            time.sleep(1.5)

            res = random.randint(0, 11)
            if res > 5:

                self.right()
                print("svänger Höger")
                time.sleep(1.5)


            else:

                self.left()
                print("Svänger Vänster")
                time.sleep(1.5)


        else:
            self.forward()


    def forward(self):
        gpio.output(11, False)
        gpio.output(13, True)
        gpio.output(15, True)  # Främre vänster
        gpio.output(12, False)
        gpio.output(16, True)
        gpio.output(18, True) # Främre Höger
        gpio.output(33, True) # Bakre vänster
        gpio.output(35, True)
        gpio.output(37, False) 
        gpio.output(36, False)
        gpio.output(38, True)
        gpio.output(40, True)
        

    def back(self):
        gpio.output(11, True)
        gpio.output(13, False)
        gpio.output(15, True)  # Främre vänster
        gpio.output(12, True)
        gpio.output(16, False)
        gpio.output(18, True) # Främre Höger
        gpio.output(33, True) # Bakre vänster
        gpio.output(35, False)
        gpio.output(37, True) 
        gpio.output(36, True)
        gpio.output(38, False)
        gpio.output(40, True) 
        

    def right(self):
        gpio.output(11, False)
        gpio.output(13, True)
        gpio.output(15, True)  # Främre vänster
        gpio.output(12, True)
        gpio.output(16, False)
        gpio.output(18, True) # Främre Höger
        gpio.output(33, True) # Bakre vänster
        gpio.output(35, False)
        gpio.output(37, True) 
        gpio.output(36, False)
        gpio.output(38, True)
        gpio.output(40, True) 
        

    def left(self):
        gpio.output(11, True)
        gpio.output(13, False)
        gpio.output(15, True)  # Främre vänster
        gpio.output(12, False)
        gpio.output(16, True)
        gpio.output(18, True) # Främre Höger
        gpio.output(33, True) # Bakre vänster
        gpio.output(35, True)
        gpio.output(37, False) 
        gpio.output(36, True)
        gpio.output(38, False)
        gpio.output(40, True) 
        




    def stopit(self):
        gpio.output(11, False)
        gpio.output(13, False)
        gpio.output(15, False)  # Främre vänster
        gpio.output(12, False)
        gpio.output(16, False)
        gpio.output(18, False) # Främre Höger
        gpio.output(33, False) # Bakre vänster
        gpio.output(35, False)
        gpio.output(37, False) 
        gpio.output(36, False)
        gpio.output(38, False)
        gpio.output(40, False)
        


if __name__ == "__main__":

    try:

        r = Robot()


    except KeyboardInterrupt:

        gpio.output(11, False)
        gpio.output(13, False)
        gpio.output(15, False)  # Främre vänster
        gpio.output(12, False)
        gpio.output(16, False)
        gpio.output(18, False) # Främre Höger
        gpio.output(33, False) # Bakre vänster
        gpio.output(35, False)
        gpio.output(37, False) 
        gpio.output(36, False)
        gpio.output(38, False)
        gpio.output(40, False)