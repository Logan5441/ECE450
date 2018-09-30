import RPi.GPIO as GPIO         #import reqired libriarys
import time

SERVO1 = 27       #sets pin numbers to varaybles 
SERVO2 = 22
TRIG = 17
ECHO = 5

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(SERVO1,GPIO.OUT, initial=GPIO.LOW)     #specifing the pins as output and enabling them low
GPIO.setup(SERVO2,GPIO.OUT, initial=GPIO.LOW)
p1 = GPIO.PWM(SERVO1,50)               #defnies PWM to servos 
p2 = GPIO.PWM(SERVO2,50)
p1.start(0)
p2.start(0)

def ServoEle(angle):
    p1.ChangeDutyCycle(2.5 + 10.0 * angle / 180)      #lets you set angle of the vertially moving servo

def ServoAzi(angle):
    p2.ChangeDutyCycle(2.5 + 10.0 * angle / 180)   #lets you set the angle of the horizontally moving servo


ServoAzi(5)           #runs through a test of horizontal servo first in 5 incrimetns then from 180 deg to 5 deg
time.sleep(1)
ServoAzi(36)
time.sleep(1)
ServoAzi(67)
time.sleep(1)
ServoAzi(98)
time.sleep(1)
ServoAzi(129)
time.sleep(1)
ServoAzi(160)
time.sleep(1)
ServoAzi(180)
time.sleep(1)
ServoAzi(5)
time.sleep(1)



ServoEle(5)           #runs through a test of Vertical servo first in 5 incrimetns then from 180 deg to 5 deg
time.sleep(1)
ServoEle(36)
time.sleep(1)
ServoEle(67)
time.sleep(1)
ServoEle(98)
time.sleep(1)
ServoEle(129)
time.sleep(1)
ServoEle(160)
time.sleep(1)
ServoEle(180)
time.sleep(1)
ServoEle(5)
time.sleep(1)
