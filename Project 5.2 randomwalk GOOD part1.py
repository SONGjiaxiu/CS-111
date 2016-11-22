""" Taylor Heilman
Haley Nugent
Escaape function"""

import math
import turtle
import random
import matplotlib.pyplot as mpl

tortoise=turtle.Turtle()

def distance(x1,x2,y1,y2):
    """ funciton to find the distance between the turtle object and the origin

       parameters:
          x1: x cordinate of first point
          x2: x cordinate of second point
          y1: y cordinate of first point
          y2: y cordinate of second point

          return: distance between the two points

          """


    d = math.sqrt((x2-x1)**2 + (y2-y1)**2) #distance formula
    return (d)


def angle (x, y):
    """ function which finds the angle of the turtle object
        parameters:
          x: x cordinate of object
          y1: y cordinate of object


          return: angle of object

          """

    
    if x == 0:      #avoid dividing by zero
        x = 0.001
    angle = math.degrees(math.atan(y/x))
    if angle < 0:
        if y < 0:
            angle = angle + 360    #quadrant IV
        else:
            angle = angle +180     #quadrant II
    elif y < 0:
        angle = angle + 180        #quadrant III
    return angle



def escape(openingDegrees, tortoise, draw):

"""      escape function which randomly moves and object until it find the
          escape angle
    parameters:
          openingDegrees: the angle in degrees of the escape area
          tortoise: the turtle object
          draw: a true or false value, if you want to draw the simulation or not

          return: steps taken to escape

          """    
    x = y = 0                    # initialize (x, y) = (0, 0)
    radius = 1                      # moving in unit radius circle
    stepLength = math.pi / 128      # std dev of each step
    steps = 0
    if draw:
        scale = 300                 # scale up drawing
        setupWalls(tortoise, openingDegrees, scale, radius)

    escaped = False # has particle escaped yet?
    
    while not escaped:
        preX = x  #
        preY = y
        x=x+random.gauss(0,stepLength) #random movement for x value
        y=y+random.gauss(0,stepLength) #random movement for y value
        d = distance(0, x, 0, y)       # call upon distance function

        if d > 1:            #if the object is on the perimeter of the circle
            ang = angle(x,y)

            if ang < 360 and ang > 360-openingDegrees:  #the object found the escape area
                escaped = True

            else:           #the object didn't find the escape area, return to previous spot
                x = preX
                y = preY
        steps = steps + 1  #keep track of steps
     
 

        if draw:
            tortoise.goto(x * scale, y * scale)     # move particle

    if draw:
        screen = tortoise.getscreen()   # update screen to compensate
        screen.update()                 #   for higher tracer value

    return steps


def setupWalls(tortoise, openingDegrees, scale, radius):

    """ a function to create a circle with the desired radius and eescape angle
      parameters:
          tortoise: the turtle object
          openingDegrees: the escape angle size
          scale: the scale of the circle being drawn
          radius: radius of the circle being drawn
 

          return: none

          """
    screen = tortoise.getscreen()
    screen.mode('logo')                 # east is 0 degrees
    screen.tracer(0)                    # speed up drawing

    tortoise.up()                       # draw boundary with
    tortoise.width(0.015 * scale)        #   shaded background
    tortoise.goto(radius * scale, 0)
    tortoise.down()
    tortoise.pencolor('lightyellow')     #color of the area of the circle
    tortoise.fillcolor('lightyellow')
    tortoise.begin_fill()
    tortoise.circle(radius * scale)
    tortoise.end_fill()
    tortoise.pencolor('black')         #color of the perimeter of the circle
    tortoise.circle(radius * scale, 360 - openingDegrees)
    tortoise.up()
    tortoise.home()

    tortoise.pencolor('blue')           # particle is a blue circle
    tortoise.fillcolor('blue')
    tortoise.shape('circle')
    tortoise.shapesize(0.75, 0.75)

    tortoise.width(1)                   # set up for walk
    tortoise.pencolor('green')
    tortoise.speed(0)
    tortoise.down()                     # comment this out to hide trail



def rwMonteCarlo(i, trials):
    """A Monte Carlo simulation to find the expected distance that a random walk ends up from the origin.
     Parameters:
          i: the step to increase the escape angle size
          trials: the number of random walks
       Return value: the average distance from the origin
       """

    totalDistance = 0                   #set distance = 0
    for trial in range(trials):
        openingDegrees = i + t
        distance = escape(openingDegrees,tortoise,False)    #call upon escape function
        totalDistance = totalDistance + distance   #keep track of total steps
    return openingDegrees, totalDistance / trials  #return the average of steps

def Caginalp(openingDegrees):
    """ a function which returns the value of the Caginalp function
    Parameters:
        openingdegrees: size of the escape angle

    Return: value of the Caginalp function"""
    
    angle= math.sin((openingDegrees/180*3.14)/4)
    #if angle <= 0:
        #angle = angle + math.pi
    #print(angle)       
    return 1/2 - 2*math.log(angle)

def plotEscapeSteps(minOpening, maxOpening, steps, trials):
  
    """Plots the average distances traveled by random walks for certain escape angle sizes
       Parameters:
          MinOpening: minimum escape angle size
          maxOpening: maximum escape angle size
          steps: steps to increase from minimum angle
          trials: amount of times run for each angle size
      
       Return value: none
       """


    averagedistance = []     # initial value of lists
    widths = []
    z = []
    anglelist = []

    for i in range(minOpening,maxOpening,steps):     #for loop increases
        totalDistance = 0
        for j in range(trials):
           
            openingDegrees = i + steps/trials * j
            distance = escape(openingDegrees,tortoise,False)  #stopping the drawing of the simulation
            totalDistance = totalDistance + distance     #adding up total steps
            anglelist.append(openingDegrees)
            t = Caginalp(openingDegrees)  #calling upon Caginal function
            z.append(t)
                    
        dist = totalDistance/trials * ((math.pi /128) ** 2)          
        averagedistance.append(dist)
        widths.append(i)                    #appending desired values
        
        
 
    mpl.plot(widths, averagedistance, label = 'Simulation')   #plotting graphs of values
    mpl.legend(loc = 'center right')
    mpl.xlabel('Opening Widths')               # labeling x and y axis
    mpl.ylabel('Average Number of Steps')
    mpl.plot(anglelist, z, label = 'Caginalp')
    mpl.show()
          




def main():
    plotEscapeSteps(10,190,10,5000)   # main function containing the plot function



main()
