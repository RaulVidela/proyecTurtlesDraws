#!/usr/bin/env python

import rospy

from geometry_msgs.msg import Twist

import rosservice

PI = 3.14
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

def position_initla_turtle(x, y, theta):

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

    _move_with(distance, speed, vel_msg)


def rotate(speed, angle, clockwise):

    rospy.init_node('turtle_draw', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

    vel_msg = init_vel_msg()
    # Converting from angles to radians
    angular_speed = speed * 2 * PI / 360
    relative_angle = angle * 2 * PI / 360

    # Checking if our movement is CW or CCW
    if clockwise:
        vel_msg.angular.z = -abs(angular_speed)
    else:
        vel_msg.angular.z = abs(angular_speed)

    _move_with(relative_angle, angular_speed, vel_msg)


def _move_with(relative_move, speed, vel_msg):

    # Setting the current time for distance calculus
    t0 = rospy.Time.now().to_sec()
    current_move = 0

    while (current_move < relative_move):
        velocity_publisher.publish(vel_msg)
        t1 = rospy.Time.now().to_sec()
        current_move = (t1 - t0)*speed

    vel_msg.linear.x = 0
    vel_msg.angular.z = 0
    velocity_publisher.publish(vel_msg)