#!/usr/bin/env python

import math
import turtle_move
import numpy

PI = 3.141592

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

def star(center, spikes,min_r,max_r):

    if(spikes > 2):

        colection_point = []

        angle = 360 / spikes

        print (angle)
        ## averiguar el segundo punto

        angle_of_rotation = 0

        for z in range(spikes):

            if(angle_of_rotation <= 90):
                print (" angle_of_rotation <= 90 "+str(angle_of_rotation))
                angle_calculate = angle_of_rotation
                print (angle_calculate)
                quadrant = 1
            elif ((angle_of_rotation > 90) and (angle_of_rotation <= 180)):
                print (" angle_of_rotation > 90 and angle_of_rotation <= 180 "+str(angle_of_rotation))
                angle_calculate = 180 - angle_of_rotation
                quadrant = 2
                print (angle_calculate)
            elif((angle_of_rotation > 180) and (angle_of_rotation <= 270)):
                print (" angle_of_rotation > 180 and angle_of_rotation <= 270 "+str(angle_of_rotation))
                angle_calculate = angle_of_rotation - 180
                quadrant = 3
                print (angle_calculate)
            else:
                print (" else : "+str(angle_of_rotation))
                angle_calculate = 360 - angle_of_rotation
                quadrant = 4
                print (angle_calculate)


            print ("seno :   " +str(numpy.sin(numpy.deg2rad(angle_calculate))))
            print ("coseno : " +str(numpy.cos(angle_calculate*PI/180)))
            delta_x =abs(math.sin(angle_calculate*PI/180) * min_r)
            delta_y =abs(math.cos(angle_calculate*PI/180) * min_r)
            print ("delta x "+str(delta_x))
            print ("delta y "+str(delta_y))

            if(quadrant == 1):
                print ("cuadrante 1")
                x = center[0] + delta_x
                y = center[1] + delta_y
            elif (quadrant == 2):
                print ("cuadrante 2")
                x = center[0] + delta_x
                y = center[1] - delta_y
            elif(quadrant == 3):
                print ("cuadrante 3")
                x = center[0] - delta_x
                y = center[1] - delta_y
            elif(quadrant == 4):
                print ("cuadrante 4")
                x = center[0] - delta_x
                y = center[1] + delta_y

            print ("x : "+str(x) + "--  y : "+str(y))
            colection_point.append([x,y])
            print (colection_point)

            angle_of_rotation += angle


        draw_figure(colection_point)


    else:
        print("insufficient number of spikes")

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
    star([5,5],3,3,4)
    star([5,5],4,3,4)
    star([5,5],6,3,4)
    print ("FIN")

    #        try:
    #
    #        except rospy.ROSInterruptException:
    #            pass