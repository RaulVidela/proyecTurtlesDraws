#!/usr/bin/env python

import math
import rospy
import rosservice
from geometry_msgs.msg import Twist


PI = 3.141592
velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

def init_vel_msg():

    rospy.init_node('turtle_draw', anonymous=True)
    vel_msg = Twist()

    vel_msg.linear.x = 0
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0

    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0

    return vel_msg

def position_initial_turtle(x, y, theta):

    rospy.wait_for_service("/turtle1/teleport_absolute")
    rospy.wait_for_service("/turtle1/set_pen")

    turtle_pen = rospy.ServiceProxy("/turtle1/set_pen", rosservice.get_service_class_by_name("/turtle1/set_pen"))
    teleport = rospy.ServiceProxy("/turtle1/teleport_absolute", rosservice.get_service_class_by_name("/turtle1/teleport_absolute"))

    turtle_pen(255,255,255,1,1)

    teleport(x, y, theta)

    turtle_pen(255, 255, 255, 1, 0)


def move_in_line_straight(speed, distance):

    vel_msg = init_vel_msg()

    vel_msg.linear.x = speed

    _move_with(distance,speed, vel_msg)


def rotate(speed, angle, clockwise):

    vel_msg = init_vel_msg()
    # Converting from angles to radians
    angular_speed = speed * 2 * PI / 360

    # Checking if our movement is CW or CCW
    if clockwise:
        vel_msg.angular.z = -abs(angular_speed)
    else:
        vel_msg.angular.z = abs(angular_speed)

    _move_with(angle, angular_speed, vel_msg)


def move_point_to_point(point_initial, point_end):

    position_initial_turtle(point_initial[0] , point_initial[1] ,  0)

    delta_x = point_end[0] - point_initial[0]
    delta_y = point_end[1] - point_initial[1]

    ##verification,
    # if delta_x and delta_y value 0
    # hypotenuse and angle value 0
    if((delta_y != 0) or (delta_x != 0)):

        ##get distance between two points
        hypotenuse = float(math.sqrt(pow(delta_x,2)+pow(delta_y,2)))
        ##get angle between two points
        angle = math.degrees(math.acos(delta_x/hypotenuse))


        ##if is or not negative delta_y, defines the direction of rotation
        if(delta_y > 0):
            clockwise = False
        else:
            clockwise = True

        ##if the value of delta_x is 0, then the angle is 90,
        if(delta_x == 0 ):
            angle = 90

        ##if the value of delta_y is 0, then the angle can be 0 or 180,
        # depends on the value of delva_x
        if(delta_y == 0):
            clockwise = True
            if(delta_x > 0):
                angle = 0
            else:
                angle = 180
    else:
        ##in the case that the value of delta_x and delta_y is 0
        # then the values of angle and hyponuse are 0
        angle = 0
        hypotenuse = 0
        clockwise = True

    ##converting the angle from sexagesimal to radians
    angle = angle * PI / 180

    rotate(5,angle,clockwise)
    move_in_line_straight(5,hypotenuse)

def _move_with(relative_move, speed, vel_msg):

    t0 = rospy.Time.now().to_sec()
    current_move = 0

    while (current_move < relative_move):
        velocity_publisher.publish(vel_msg)
        t1 = rospy.Time.now().to_sec()
        current_move = (t1 - t0)*speed

    ##stop the turtle
    vel_msg.linear.x = 0
    vel_msg.angular.z = 0
    velocity_publisher.publish(vel_msg)


if __name__ == '__main__':

    move_point_to_point([2,2],[6,6])
    move_point_to_point([6,6],[4,6])

    move_point_to_point([4,6],[4,6])

    move_point_to_point([4,6],[4,8])
    move_point_to_point([4,6],[4,4])

    move_point_to_point([4,4],[2,4])
    move_point_to_point([4,4],[6,4])