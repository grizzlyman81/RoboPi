# Ta bort linjen under denna kommentar och testa igen
#!/usr/bin/python3
import RPi.GPIO as GPIO
import time
from flask import Flask
from flask import render_template, request
app = Flask(__name__)

GPIO.setwarnings(False)


GPIO.setmode(GPIO.BOARD)

@app.route("/")
def index():
    return render_template('robot.html')


    
def init():
    GPIO.setup(31, GPIO.OUT)
    GPIO.setup(33, GPIO.OUT)
    GPIO.setup(35, GPIO.OUT)
    GPIO.setup(37, GPIO.OUT)

@app.route('/up_side')

def up_side():
    init()
    GPIO.output(31, True)
    GPIO.output(33, False)
    GPIO.output(35, True)
    GPIO.output(37, False)
    return 'true'


@app.route('/down_side')

def down_side():
    init()
    GPIO.output(31, False)
    GPIO.output(33, True)
    GPIO.output(35, False)
    GPIO.output(37, True)
    
    return 'true'
        
@app.route('/left_side')
def left_side():
    init()
    GPIO.output(31, True)
    GPIO.output(33, True)
    GPIO.output(35, False)
    GPIO.output(37, False)
    
    return 'true'

@app.route('/right_side')

def right_side():
    init()
    GPIO.output(31, True)
    GPIO.output(33, False)
    GPIO.output(35, False)
    GPIO.output(37, True)
    return 'true'
    
    
@app.route('/stop')

def stop():
    init()
    GPIO.output(31, False)
    GPIO.output(33, False)
    GPIO.output(35, False)
    GPIO.output(37, False)
   # GPIO.cleanup()
    
    return 'true'   # <--- Denna var bort kommenterad löste ValueError

if __name__ == "__main__":
# print "Start"
 app.run(host='192.168.0.191',port=5010)
pi@RoboPi:~/robot $ 
