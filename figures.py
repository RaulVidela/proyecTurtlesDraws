#!/usr/bin/env python

import math
import turtle_move

def square(center, length):

    colection_points= []
    point_1 = [0,0]
    point_2 = [0,0]
    point_3 = [0,0]
    point_4 = [0,0]

    half_length = float(length)/2

    point_1[0] = (float(center[0]) - half_length)
    point_1[1] = (float(center[1]) - half_length)

    point_2[0]=(float(center[0]) + half_length)
    point_2[1]=(float(center[1]) - half_length)

    point_3[0] =(float(center[0]) + half_length)
    point_3[1] =(float(center[1]) + half_length)

    point_4[0] =(float(center[0]) - half_length)
    point_4[1] =(float(center[1]) + half_length)

    colection_points.append(point_1)
    colection_points.append(point_2)
    colection_points.append(point_3)
    colection_points.append(point_4)
    print (colection_points)
    draw_figure(colection_points)

def triangle(center, length):

    colection_points = []
    point_1 = [0,0]
    point_2 = [0,0]
    point_3 = [0,0]

    half_length = float(length) / 2
    h = math.sqrt(pow(length,2)-pow(half_length,2))

    point_1[0] = (float(center[0]) - half_length)
    point_1[1] = (float(center[1]) - (h/3))

    point_2[0] = (float(center[0]) + half_length)
    point_2[1] = (float(center[1]) - (h/3))

    point_3[0] =(float(center[0]))
    point_3[1] =(float(center[1]) + (2*h/3))

    colection_points.append(point_1)
    colection_points.append(point_2)
    colection_points.append(point_3)

    draw_figure(colection_points)

def polygon(center, colection_points):

    size = len(colection_points)
    points_moved = []
    for x in range(size):

        point = colection_points[x]
        print ("punto : "+str(point))
        x = point[0] + center[0]
        y = point[1] + center[1]

        points_moved.insert(x,[x,y])
        print("coleccion : " + str(points_moved))

    draw_figure(points_moved)

def star():
    print ("hola")

def draw_figure(colection_of_points):

    size = len(colection_of_points)
    colection_of_points.append(colection_of_points[0])

    for x in range(size):
        y = x + 1
        point_a = colection_of_points[x]
        point_b = colection_of_points[y]
        turtle_move.move_point_to_point(point_a,point_b)




if __name__ == '__main__':

    print ("INICIO")
    polygon([6,6],[[2,2],[2,-2],[0,-3],[-2,0],[0,2]])
    print ("FIN")

    #        try:
    #
    #        except rospy.ROSInterruptException:
    #            pass