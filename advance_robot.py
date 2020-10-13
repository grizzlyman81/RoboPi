#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import random





class Robot:
    def __init__(self):
        
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(31, GPIO.OUT)
        GPIO.setup(33, GPIO.OUT)
        GPIO.setup(35, GPIO.OUT)
        GPIO.setup(37, GPIO.OUT)
        
        while True:
            self.center_sensor()
            self.left_sensor()
            self.right_sensor()

    def center_sensor(self):
        self.PIN_TRIGGER = 7
        self.PIN_ECHO = 11
        

        GPIO.setup(self.PIN_TRIGGER, GPIO.OUT)
        
        GPIO.setup(self.PIN_ECHO, GPIO.IN)

        GPIO.output(self.PIN_TRIGGER, GPIO.LOW)

       # print("Värmer upp sensorn")

        time.sleep(0.5)

        #print("Beräknar avstånd")

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
        if distance < 30:
            res = random.randint(0, 11)
            if res > 5:

                self.back_right()
                #time.sleep(1.5)


            else:

                self.back_left()
                #time.sleep(0.5)


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

        #print("Beräknar avstånd")

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
        if distance < 30:
            print("Hinder upptäckt påbörjar åtgärd")
            
            self.back_left()
            
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
        
        print("Avstånd:", distance, "cm")
        if distance < 30:
            print("Hinder upptäckt påbörjar åtgärd")
            
            self.back_right()

    def stopit(self):


        
        GPIO.output(31, False)
        GPIO.output(33, False)
        GPIO.output(35, False)
        GPIO.output(37, False)
        time.sleep(0.5)

    def forward(self):
        GPIO.output(31, False)
        GPIO.output(33, True)
        GPIO.output(35, False)
        GPIO.output(37, True)

    def back_right(self):
        GPIO.output(31, True)
        GPIO.output(33, False)
        GPIO.output(35, False)
        GPIO.output(37, False)
        time.sleep(1.5)

    def back_left(self):
        GPIO.output(31, False)
        GPIO.output(33, False)
        GPIO.output(35, True)
        GPIO.output(37, False)
        time.sleep(1.5)


if __name__ == "__main__":

    try:
        
        r = Robot()
        #r.center_sensor()
        #r.left_sensor()
        #r.right_sensor()
        #r.stopit()
        #r.forward()
        #r.back_right()
        #r.back_left()
        
    except KeyboardInterrupt:
        print("Stänger ner...")
        GPIO.cleanup()

