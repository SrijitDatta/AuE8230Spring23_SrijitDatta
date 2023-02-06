#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
import math

def square_straight1():
    # Starts a new node
    rospy.init_node('turtlesim', anonymous=True)
    #Define the publisher
    pub = rospy.Publisher('/turtle1/cmd_vel',
                          Twist, queue_size=10)
    rate = rospy.Rate(10)
    vel = Twist()

    for i in range(0,4):
     #Setting the current time for distance calculation
     current_distance = 0
     t0 = rospy.Time.now().to_sec()
     
     while(current_distance <= 2):
       
      vel.linear.x = 0.2
      vel.linear.y = 0
      vel.linear.z = 0
      vel.angular.x = 0
      vel.angular.y = 0
      vel.angular.z = 0
     
      pub.publish(vel) 
            #Takes actual time to velocity calculation
      t1=rospy.Time.now().to_sec()
            #Calculates distancePoseStamped
      current_distance = 0.2*(t1-t0)
     
     #After the loop, stops the robot
     vel.linear.x = 0
     #Force the robot to stop
     pub.publish(vel)
            
     current_angle= 0
     desire_turn=(3.14159265)/2
     t0 = rospy.Time.now().to_sec()
                
     while(current_angle<=desire_turn):
            
      vel.linear.x = 0
      vel.linear.y = 0
      vel.linear.z = 0
      vel.angular.x = 0
      vel.angular.y = 0
      vel.angular.z = 0.2
            
      pub.publish(vel)
      t1 = rospy.Time.now().to_sec()
      current_angle = 0.2*(t1-t0)
	    
     vel.angular.z = 0
     pub.publish(vel)
  
if __name__ == '__main__':
    try:
        #Testing our function
        square_straight1()
        
    except rospy.ROSInterruptException: pass
