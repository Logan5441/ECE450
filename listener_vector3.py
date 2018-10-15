#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Pose
from AlphaBot import AlphaBot
Ab = AlphaBot()

def callback(data):
    sensor = [data.position.x,data.position.y,data.position.z,data.orientation.x,data.orientation.y,data.orientation.z]
#    Ab = AlphaBot()
    Ab.stop()
 #   from AlphaBot import AlphaBot
    if sensor[2] == 1:
        Ab.backward()
    elif sensor[0] == 1:
        Ab.left()
    elif sensor[3] == 1:
        Ab.right()
    else:
        Ab.right()
    rospy.loginfo("x = " + str(data.position.x) + " y = " + str(data.position.y) + " z = " + str(data.position.z) + "x1 = "+ str(data.orientation.x) + "y2 ="+ str(data.orientation.y) + "z3 = " + str(data.orientation.z))
   
   
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('sen_listener', anonymous=True)

    rospy.Subscriber("sen_ir", Pose, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
  #  from AlphaBot import AlphaBot
    listener()

