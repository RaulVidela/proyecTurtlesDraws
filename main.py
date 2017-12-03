#!/usr/bin/env python
import string
import figures


def menu_initial():
    print("Choose a figure")
    print("Triangle : 1")
    print("Square   : 2")
    print("Polygon  : 3")
    print("Star     : 4")

    return input("Chosen figure : ")

def input_center():
    print("input the center")
    x = input( "value x : ")
    y = input( "value y : ")
    return [x,y]

def date_of_the_triangle():

    center = input_center()
    print("input the length ")
    length = input("length : ")

    figures.triangle(center,length)

def date_of_the_squre():

    center = input_center()
    print(" input the length ")
    length = input("length : ")

    figures.square(center, length)

def date_of_the_polygon():
    center = input_center()
    colection_of_points = []

    print(" input the number of points ")
    number_of_point = input("number of point : ")

    for z in range(number_of_point):

        print(" input the point number : "+str(z))
        x = input("value x : ")
        y = input("value y : ")

        colection_of_points.append([x,y])

    figures.polygon(center,colection_of_points)

def date_of_the_star():
    center = input_center()

    #spikes
    print(" input the number of spikes, minimum 3 ")
    spikes = input("spikes : ")
    while(spikes < 2):
        print(" number of spikes invalid")
        spikes = input("spikes : ")
    # min_r
    print(" input the small radio ")
    min_r = input("minimum radio : ")
    # max_r
    print(" input the large radio ")
    max_r = input("maximum radio : ")

    figures.star(center,spikes,min_r,max_r)


if __name__ == '__main__':

    print("Welcome")

    option = -1
    while(option!= 0):

        option = menu_initial()
        print("\n")
        if(option == 1):
            date_of_the_triangle()
        elif(option==2):
            date_of_the_squre()
        elif(option==3):
            date_of_the_polygon()
        elif(option==4):
            date_of_the_star()
        else:
            print("The chosen figure is invalid")

        print("\n")
        finish = 0

        finish = input("input '-1' for finish : ")

        if ( finish == -1):
            option = 0
        else:
            option = -1

