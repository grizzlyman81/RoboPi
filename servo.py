#!/usr/bin/python3

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(3, GPIO.OUT)
GPIO.setup(38, GPIO.OUT)

p2 = GPIO.PWM(38, 50)


p = GPIO.PWM(3, 50)



p.start(12.5)
p2.start(2.5)


p2.ChangeDutyCycle(12.5)
time.sleep(1)
    #p.ChangeDutyCycle(7.5)  # turn towards 90 degree
    #time.sleep(1)  # sleep 1 second
p.ChangeDutyCycle(0.5)  # turn towards 0 degree
time.sleep(1)  # sleep 1 second
p2.ChangeDutyCycle(2.5)
time.sleep(2)
p2.stop()
p.stop()
GPIO.cleanup()
