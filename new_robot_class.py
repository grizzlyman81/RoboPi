#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 17:26:47 2020

@author: bjopet
"""

# !/usr/bin/python
import RPi.GPIO as GPIO
import time
import random
from picamera import PiCamera
from datetime import datetime
import subprocess
import os

cam = PiCamera()
cam.vflip = True

name = datetime.now().strftime('%c')


class Robot:
    def __init__(self):

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

        while True:
            self.center_sensor()
            self.left_sensor()
            self.right_sensor()
            q = GPIO.input(23)
            w = GPIO.input(29)
            if q == 1:
                print("Hit!!!")
                self.stopit()
                time.sleep(1)
                self.back_right()
                time.sleep(1)

            elif w == 1:
                print("Hit!!!")
                self.stopit()
                time.sleep(1)
                self.back_left()
                time.sleep(1)



    def center_sensor(self):
        self.PIN_TRIGGER = 7
        self.PIN_ECHO = 11

        GPIO.setup(self.PIN_TRIGGER, GPIO.OUT)

        GPIO.setup(self.PIN_ECHO, GPIO.IN)

        GPIO.output(self.PIN_TRIGGER, GPIO.LOW)

        # print("Värmer upp sensorn")

        time.sleep(0.2)

        # print("Beräknar avstånd")

        GPIO.output(self.PIN_TRIGGER, GPIO.HIGH)

        time.sleep(0.00001)

        GPIO.output(self.PIN_TRIGGER, GPIO.LOW)

        while GPIO.input(self.PIN_ECHO) == 0:
            pulse_start_time = time.time()

        while GPIO.input(self.PIN_ECHO) == 1:
            pulse_end_time = time.time()

        pulse_duration = pulse_end_time - pulse_start_time

        distance = round(pulse_duration * 17150, 2)

        print("Avstånd:", distance, "cm")
        if distance < 40:
            self.stopit()
            cam.capture('/home/pi/bilder/' + name + '.jpeg')
            os.system('/home/pi/robot/send_mail.py')
            time.sleep(2)
            res = random.randint(0, 11)
            if res > 5:

                self.back_right()
                time.sleep(1.0)


            else:

                self.back_left()
                time.sleep(1.0)


        else:
            self.forward()

    def left_sensor(self):

        self.PIN_TRIGGER = 13
        self.PIN_ECHO = 15

        GPIO.setup(self.PIN_TRIGGER, GPIO.OUT)

        GPIO.setup(self.PIN_ECHO, GPIO.IN)

        GPIO.output(self.PIN_TRIGGER, GPIO.LOW)

        # print("Värmer upp sensorn")

        time.sleep(0.2)

        # print("Beräknar avstånd")

        GPIO.output(self.PIN_TRIGGER, GPIO.HIGH)

        time.sleep(0.00001)

        GPIO.output(self.PIN_TRIGGER, GPIO.LOW)

        while GPIO.input(self.PIN_ECHO) == 0:
            pulse_start_time = time.time()

        while GPIO.input(self.PIN_ECHO) == 1:
            pulse_end_time = time.time()

        pulse_duration = pulse_end_time - pulse_start_time

        distance = round(pulse_duration * 17150, 2)

        #print("Avstånd:", distance, "cm")
        if distance < 40:
            print("Hinder upptäckt påbörjar åtgärd")

            self.back_left()
            time.sleep(0.5)

    def right_sensor(self):

        self.PIN_TRIGGER = 16
        self.PIN_ECHO = 18

        GPIO.setup(self.PIN_TRIGGER, GPIO.OUT)

        GPIO.setup(self.PIN_ECHO, GPIO.IN)

        GPIO.output(self.PIN_TRIGGER, GPIO.LOW)

        time.sleep(0.2)

        GPIO.output(self.PIN_TRIGGER, GPIO.HIGH)

        time.sleep(0.00001)

        GPIO.output(self.PIN_TRIGGER, GPIO.LOW)

        while GPIO.input(self.PIN_ECHO) == 0:
            pulse_start_time = time.time()

        while GPIO.input(self.PIN_ECHO) == 1:
            pulse_end_time = time.time()

        pulse_duration = pulse_end_time - pulse_start_time

        distance = round(pulse_duration * 17150, 2)

        #print("Avstånd:", distance, "cm")
        if distance < 40:
            print("Hinder upptäckt påbörjar åtgärd")

            self.back_right()
            time.sleep(0.5)

    def stopit(self):

        GPIO.output(31, False)
        GPIO.output(33, False)
        GPIO.output(35, False)
        GPIO.output(37, False)
        GPIO.output(32, False)
        GPIO.output(36, False)
        GPIO.output(38, False)
        GPIO.output(40, False)

    def forward(self):
        GPIO.output(31, True)
        GPIO.output(33, True)
        GPIO.output(35, False)
        GPIO.output(37, True)
        GPIO.output(32, True)
        GPIO.output(36, True)
        GPIO.output(38, False)
        GPIO.output(40, True)

    def back(self):
        GPIO.output(31, True)
        GPIO.output(33, True)
        GPIO.output(35, True)
        GPIO.output(37, False)
        GPIO.output(32, True)
        GPIO.output(36, True)
        GPIO.output(38, True)
        GPIO.output(40, False)


    def back_right(self):
        GPIO.output(31, True)
        GPIO.output(33, True)
        GPIO.output(35, True)
        GPIO.output(37, False)
        GPIO.output(32, False)
        GPIO.output(36, False)
        GPIO.output(38, False)
        GPIO.output(40, False)

    def back_left(self):
        GPIO.output(31, False)
        GPIO.output(33, False)
        GPIO.output(35, False)
        GPIO.output(37, False)
        GPIO.output(32, True)
        GPIO.output(36, True)
        GPIO.output(38, True)
        GPIO.output(40, False)


if __name__ == "__main__":

    try:

        r = Robot()


    except KeyboardInterrupt:
        
        print("Stänger ner...")
        GPIO.output(31, False)
        GPIO.output(33, False)
        GPIO.output(35, False)
        GPIO.output(37, False)
        GPIO.output(32, False)
        GPIO.output(36, False)
        GPIO.output(38, False)
        GPIO.output(40, False)
        GPIO.cleanup()
