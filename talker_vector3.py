#!/usr/bin/env python
# license removed for brevity
import rospy
from geometry_msgs.msg import Pose
import RPi.GPIO as GPIO
import time

CS = 5 
Clock = 25
Address = 24
DataOut = 23


def talker(IR_val):
    
    pub = rospy.Publisher('sen_ir', Pose, queue_size=10)
    rospy.init_node('camera', anonymous=True)
 #   rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        Values = TR.AnalogRead()
        for i in range(0,5):
                if Values[i] < 600:
                    detect[i] = 1
                else:
                    detect[i] = 0
        sen_ir = Pose()
        sen_ir.position.x = IR_val[0]
        sen_ir.position.y = IR_val[1]
        sen_ir.position.z = IR_val[2]
        sen_ir.orientation.x = IR_val[3]
        sen_ir.orientation.y = IR_val[4]
        sen_ir.orientation.z = IR_val[5]
        rospy.loginfo(sen_ir)
        pub.publish(sen_ir)
  #      rate.sleep()


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(Clock,GPIO.OUT)
GPIO.setup(Address,GPIO.OUT)
GPIO.setup(CS,GPIO.OUT)
GPIO.setup(DataOut,GPIO.IN,GPIO.PUD_UP)


if __name__ == '__main__':
    try:
        from Bang_bang import TRSensor
        TR = TRSensor()
        detect = [0,0,0,0,0,0]
        #while True:
    
       #     Values = TR.AnalogRead()
       #     for i in range(0,5):
       #         if Values[i] < 800:
       #             detect[i] = 1
       #         else:
       #             detect[i] = 0
        talker(detect)
           # print(detect)
    
    except rospy.ROSInterruptException:
        pass
