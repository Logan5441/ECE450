import RPi.GPIO as GPIO
import time


in1=12
in2=13
in3=20
in4=21
ena=6
enb=26

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(ena,GPIO.OUT)
GPIO.setup(enb,GPIO.OUT)
PWMA = GPIO.PWM(ena,50)
PWMB = GPIO.PWM(enb,50)
PWMA.start(20)
PWMB.start(20)

def forward():
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.HIGH)

def backwards():
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)

def left():
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.HIGH)

def right():
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)

def stop():
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.LOW)



forward()
time.sleep(5)
stop()
time.sleep(1)
backwards()
time.sleep(10)
stop()
time.sleep(1)
forward()
time.sleep(5)
stop()
time.sleep(1)
right()
time.sleep(1.2)
stop()
time.sleep(1)
forward()
time.sleep(5)
stop()
time.sleep(1)
backwards()
time.sleep(5)
stop()
time.sleep(1)
left()
time.sleep(2.4)
stop()
time.sleep(1)
forward()
time.sleep(5)
stop()
time.sleep(1)
backwards()
time.sleep(5)
stop()
time.sleep(1)
right()
time.sleep(1.2)
stop()
