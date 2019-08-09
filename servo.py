
	
import RPi.GPIO as GPIO
import time
import pigpio
pi = pigpio.pi()
from datetime import datetime
from picamera import PiCamera
kamera = PiCamera()
import os


GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)
#GPIO.setup(10, GPIO.OUT)
SERVO = 15

try:
    while True:
        name = datetime.now().strftime('%c')
        i=GPIO.input(4)
        pi.set_servo_pulsewidth(SERVO, 1000) # Start position of Servo
        print("Position: 1000")
        time.sleep(10) # time for servo to stop and stand still
        if i==0:
            print("No movement")
            
            pi.set_servo_pulsewidth(SERVO, 1500) # New Position
            print("Moved sensor to 1500")
            time.sleep(10)
            
        elif i == 1:
            print("Movement")
            kamera.capture('/home/pi/bevaka/bilder/motion/'+name+'.jpeg')
            os.system('/home/pi/backup/attach_test.py')
            time.sleep(5)
            i = 0
         
            pi.set_servo_pulsewidth(SERVO, 1500)
            print("Moved sensor to 1500")
            time.sleep(10)
        if i==0:
            print("No Movement")
            
            pi.set_servo_pulsewidth(SERVO, 2000)
            print("Moved sensor to 2000")
            time.sleep(10)
        elif i == 1:
            print("Movement")
            kamera.capture('/home/pi/bevaka/bilder/motion/'+name+'.jpeg')
            os.system('/home/pi/backup/attach_test.py')
            time.sleep(5)
            i = 0
            pi.set_servo_pulsewidth(SERVO, 2000)
            print("Moved Ssensor to 2000")
            time.sleep(10)
            
       
        if i==0:
            print("No Movement")
            
        elif i == 1:
            print("Movement")
            kamera.capture('/home/pi/bevaka/bilder/motion/'+name+'.jpeg')
            os.system('/home/pi/backup/attach_test.py')
            time.sleep(10)
            i = 0
except KeyboardInterrupt:
    pi.stop()
    GPIO.cleanup()
