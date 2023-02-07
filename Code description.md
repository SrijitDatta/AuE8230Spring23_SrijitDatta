Circle:

The goal here is to make the turtle bot trace a circular path continuously. The Twist module is imported as it is a common data structure used to represent velocity information for robots.
The linear and angular velocity of the robot can be specified.
In this code, a while loop is used, and inside it is the linear and angular velocity specified. The turtlebot traces a circular path with a constant linear and angular velocity continuously.
 

Square open loop:

The goal here is to make the turtle bot trace a square path when a set of instructions is provided.
The turtle bot traces an area of 2x2 square units and moves with a velocity of 0.2 units per second.
After taking time outside the loop, the current time is determined for each iteration of the loop.
The current distance is thus equal to the velocity times the product of the time inside the loop divided by the time outside the loop.
The while loop must end if the current distance is more than 0.2 units.
A similar approach is used for rotating the turtle bot once travelled in a straight line.
The turtle turns until it reaches an angle of pi/2 radians, at which point it can trace out the square's second side.


source: Moving in a straight line and Rotating left and right: Roswiki
http://wiki.ros.org/turtlesim/Tutorials/Moving%20in%20a%20Straight%20Line
http://wiki.ros.org/turtlesim/Tutorials/Rotating%20Left%20and%20Right



Square closed loop:

A P controller is used to regulate the velocity of the turtlebot. As the robot approaches the turn, the velocity with which it movees reduces.
The math module is imported as it provides a collection of functions and constants that would be used in the code to calculate the angles.
Two vectors are defined each containing the x and y coordinates of the desired position at each step.
Since the turtle has to trace a 3x3 square, the x and y co ordinates are defined in each array.
A for loop is incorporated which helps define the position where the turtle needs to be at every increment.
A while loop is defined inside it which keeps track of the distance covered and when it is, it exits the loop.
At the end of the while loop the turlte roates by pi/2 radians.
This while loop is iterated 5 times and the goal is achieved.
The constant for P controller is taken as 10.
source: gotogoal on Roswiki
http://wiki.ros.org/turtlesim/Tutorials/Go%20to%20Goal