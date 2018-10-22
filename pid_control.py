import RPi.GPIO as GPIO
import time

CS = 5
Clock = 25
Address = 24
DataOut = 23

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(Clock,GPIO.OUT)
GPIO.setup(Address,GPIO.OUT)
GPIO.setup(CS,GPIO.OUT)
GPIO.setup(DataOut,GPIO.IN,GPIO.PUD_UP)


if __name__ == '__main__':

	from AlphaBot import AlphaBot
        from Bang_bang import TRSensor
	maximum = 35;
	integral = 0;
	last_proportional = 0
	
	TR = TRSensor()
	Ab = AlphaBot()
	Ab.stop()
	print("Line follow Example")
	time.sleep(0.5)
	for i in range(0,400):
		TR.calibrate()
		print i
	print(TR.calibratedMin)
	print(TR.calibratedMax)
	time.sleep(0.5)	
	Ab.backward()
        
        
        actual = 0.0
        mag = 1
        setvalue = 0 
        kp = 50

        lbound = -2
        hbound = 2
       
        maxpwm = 20
        spd = 0
	while True:
                position = TR.readCalibrated()		#print(position)
		
		# The "proportional" term should be 0 when we are on the line.
	    
                actual = 0
                if position[2] >  600: 
                   actual = actual
                elif position[1] > 600:
                   actual = actual - 1*mag
                elif position[3] > 600:
                   actual = actual + 1*mag
                elif position[4] >600: 
                   actual = actual + 3*mag
                elif position[0] >600:
                   actual = actual - 3*mag
              
                actual = actual       
             
                correct = setvalue - actual 
                spd = correct*kp
                if abs(spd) > maxpwm:
                    spd  = maxpwm-1
                print(spd)

                if correct > lbound and correct < hbound:
                    Ab.setPWMB(maxpwm)
                    Ab.setPWMA(maxpwm)
                elif correct > lbound:
                    Ab.setPWMB(maxpwm-spd)
                    Ab.setPWMA(maxpwm)
                elif correct < hbound:
                    Ab.setPWMB(maxpwm)
                    Ab.setPWMA(maxpwm-spd)
