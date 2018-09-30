import RPi.GPIO as GPIO      #imports GPIO Library
import time                  #imports time libary


in1=12             #This is where you initalize what pin of the SoC gets a signal
in2=13
in3=20
in4=21
ena=6
enb=26

GPIO.setmode(GPIO.BCM)           
GPIO.setwarnings(False)
GPIO.setup(in1,GPIO.OUT)      #Initialsing if a pin is either in or out signal
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(ena,GPIO.OUT)
GPIO.setup(enb,GPIO.OUT)
PWMA = GPIO.PWM(ena,50)     #starts a PWM sequence for the two motor pins
PWMB = GPIO.PWM(enb,50)
PWMA.start(20)        #where you set the duty Cycle (0-100) for the two motor pins (
PWMB.start(20)

def forward():
    GPIO.output(in1,GPIO.HIGH)      #moves the bot forward by enabliing high pins 2,3
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.HIGH)

def backwards():
    GPIO.output(in1,GPIO.LOW)    #moves bot backwards by enabling high pins 2,3
    GPIO.output(in2,GPIO.HIGH)
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)

def left():
    GPIO.output(in1,GPIO.LOW)     #moves bot left
    GPIO.output(in2,GPIO.HIGH)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.HIGH)

def right():                        #moves bot right
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)

def stop():                             #sets all signals to bot to low to stop
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.LOW)



forward()             #sequence of movements for bot to complete  seconds being in the parentheses
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
