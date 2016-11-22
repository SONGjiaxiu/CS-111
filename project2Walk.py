# Random Walk Example

import matplotlib.pyplot as mpl
import random
import math
import turtle

def randomWalk(steps, tortoise):
    """Displays a random walk on a grid

       Parameters:
          steps: the number of steps in the random walk
          tortoise: a Turtle object

       Return value: the final distance from the origin
       """

    x = 0                   # initialize (x, y) = (0, 0)
    y = 0
    moveLength = 10         # length of a turtle step
    for step in range(steps):
        x=x+random.gauss(0,0.5)
        y=y+random.gauss(0,0.5)
 
        tortoise.goto(x * moveLength, y * moveLength) # draw one step

    return math.sqrt(x * x + y * y)     # return distance from (0, 0)

def rwMonteCarlo(steps, trials):
    """A Monte Carlo simulation to find the expected distance that a random walk ends up from the origin.
       Parameters
          steps: the number of steps in the random walk
          trials: the number of random walks
       Return value: the average distance from the origin
       """

    totalDistance = 0
    for trial in range(trials):
        distance = randomWalk(steps, None)
        totalDistance = totalDistance + distance
    return totalDistance / trials

def plotDistances(maxSteps, trials):
    """Plots the average distances traveled by random walks of 100, 200, ..., maxSteps steps
       Parameters:
          maxSteps: the maximum number of steps for the plot
          trials: the number of random walks in each simulation
       Return value: none
       """
    distances = []
    stepRange = range(100, maxSteps + 1, 100)
    for steps in stepRange:
        dist = rwMonteCarlo (steps, trials)
        distance.append(dist)

    mpl.plot(steprange, distnaces, label = 'Simulation')
    mpl.legend(loc = 'center right')
    mpl.xlabel('Number of Steps')
    mpl.ylabel('Distance From Origin')
    mpl.show()
   

george = turtle.Turtle()
randomWalk(10000, george)
            
