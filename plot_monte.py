"""
Chapter 2.6 in our textbook describes using a Monte Carlo simulation to
approximate the value of pie.

The program below is a partial implementation of the simulation. It also
contains the setup code for creating a visualization to accompany the
simulation.

The simulation generates some number of points (the higher the number, the
more accurate the approximation of pi) within a 1 x 1 plane (each points' x
and y values are floating point numbers between 0 and 1). Counting the number
of points that have a distance of less than 1 from the origin, and
multiplying that by 4, yields our approximation of pi.

1. Read chapter 2.6 (you can skim 2.6.1-2.6.3 if you're comfortable using if
   statements) in Python Programming in Context. This section describes the
   Monte Carlo simulation in detail, as well as provides the code for a
   program that the one below is based on.
2. Finish our version of the Monte Carlo simulation described in the reading
   by adding the missing code under the comments that begin with a number.
"""
import math
import random
import turtle

def monte_pi(darts):

    t = turtle.Turtle()
    wn = turtle.Screen()

    # set the dimensions of the window
    wn.setup(500, 500)

    # constrain the coordinate system so that it represents a 1 x 1 plane
    wn.setworldcoordinates(0, 0, 1, 1)

    # turn animation off
    wn.tracer(0)

    t.up()

    # 1. create a variable to keep track of how many points fall within the
    #    quarter circle
    in_circle = 0


    # 2. generate points (the parameter, called darts, represents the number
    #    of points to be generated)

    for i in range(darts):
        x = random.random()
        y = random. random()
        t.up()
        t.goto(x, y)
        d = math.sqrt(x ** 2 + y ** 2)
        if d <= 1:
            in_circle += 1
            t.dot(5, "blue")
        else:
            t.dot(5, "red")

    #    a. determine which ones fall within the quarter circle
    #    b. plot the points using a turtle function called dot
    #    c. use the turtle function color, to color the points within the
    #       the circle blue... and outside of the color red:
    #       t.color('blue')
    #       t.dot()


    # 3. use the formula in the book for calculating an approximation for pi
    pi = in_circle / darts * 4

    # only close the window when it is clicked
    wn.exitonclick()

    print("We can estimate pi to be %s" %pi)

monte_pi(2000)