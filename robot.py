#!/usr/bin/python3
import RPi.GPIO as GPIO
import time
import random

try:

    while True:
        GPIO.setmode(GPIO.BOARD)

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
            print("Sensorerna har upptäckt ett hinder",distance,"cm bort, kalkylerar annan väg!")
	    stopit() # Så den inte åker in i vägen när den skickar bilden
	    #Ta bild
            #Skicka epost
            r = random.randint(0,11)
            if r > 5:
                back_right()
                time.sleep(0.5)
#		print("Svänger höger!")
            else:
                back_left()
                time.sleep(0.5)
#		print("Svänger vänster!")
        else:
            forward()

except KeyboardInterrupt:
    print("Roboten har stannat")
    stopit()

    GPIO.cleanup()
