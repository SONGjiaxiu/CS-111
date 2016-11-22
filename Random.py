"""
seed(a) sets the seed for the PRNG
random() returns a pseduorandom number in [0,1)
randrange(start, stop, step)returns a randomly selected number from the range
uniform(a,b) returns a random floating point number between a and b
gauss(mean,stddev)the given mean and standard deviation
"""

import random

def dieRoll():
    """
    Returns the resutly of one die roll
    input: None
    return value: a random value from 1 to 6
    """
    return random.randrange(1,7)


def coinFlip():
    result = random.random()
    if result > .5:
        return "Heads"
    else:
        return "Tails"

def randomInteger(n):
    return random.randrange(0,n+1)


def randomDecimal(n):
    return random.randrange(0,n+1) * random.random()

    

def biasedCoinFlip(p):
    result = random.random()
    if result < p:
        return "Heads"
    else:
        return "Tails"


def coinCount(n):
    tails = 0
    heads = 0
    tailList = [0]
    headList = [0]
    for i in range(100):
        result = random.random()
        if result > .5:
            heads = heads+1
        else:
            tails = tails+1

        tailList.append(tails)
        headList.append(heads)
    return "Heads:", heads, "Tails:", tails
        
        
        

def main():
    print(dieRoll())
        
    

main()
    
