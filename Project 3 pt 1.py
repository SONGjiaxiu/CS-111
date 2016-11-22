#!/usr/bin/env python3

import turtle

width = 1440            # width of the window
cols = width // 6       # number of columns of text
height = 600            # height of the window
rows = height // 100    # number of rows of text

def plot(tortoise, index, value, window):
    """Plot GC fraction value for window ending at position index."""
    
    if (index == window) or (index - window + 1) // cols != (index - window) // cols:
        tortoise.up()   
        tortoise.goto((index - window + 1) % cols, \
                      (index - window + 1) // cols + 0.7 + value * 0.25)
        tortoise.down()
    else:
        tortoise.goto((index - window + 1) % cols, \
                      (index - window + 1) // cols + 0.7 + value * 0.25)
        
def bar(tortoise, index, rf):
    """Draw a colored bar over codon starting at position index in
       reading frame rf.  Put the turtle's tail up and down to
       handle line breaks properly."""
       
    tortoise.up()
    tortoise.goto(index % cols, index // cols + (rf + 1) / 5)
    tortoise.down()
    tortoise.forward(1)
    tortoise.up()
    tortoise.goto((index + 1) % cols, (index + 1) // cols + (rf + 1) / 5)
    tortoise.down()
    tortoise.forward(1)
    tortoise.up()
    tortoise.goto((index + 2) % cols, (index + 2) // cols + (rf + 1) / 5)
    tortoise.down()
    tortoise.forward(1)

def gcFreq(dna, window, tortoise):
    """
    Calculate the gf frequency in a window
    Parameters:
         dna: list of dna being searched for G and C
         window: length of dna list being searched for G and C
         tortoise: turtle object being used

         Return value:none
"""
    
    # draw red lines at 0.5 above the sequence
    
    tortoise.pencolor('red')
    for index in range(len(dna) // cols + 1):
        tortoise.up()
        tortoise.goto(0, index + 0.825)
        tortoise.down()
        if index < len(dna) // cols:
            tortoise.goto(cols - 1, index + 0.825)
        else:
            tortoise.goto((len(dna) - window) % cols, index + 0.825)
            
    tortoise.pencolor('blue')
    tortoise.up()

    for index in range (len(dna) - window):                 #go for length of dna - lenght of window
            count = 0                                       #initialize count as 0
            for letter in range(index, index+window):       
                if dna[letter] == "C" or dna[letter] == "G":  #if the letter is C or G, add one to count
                    count = count + 1
            fraction = count / window                 #Divide count by the total number of letters
            plot(tortoise, index, fraction, window)     #plot the data
    
    # get initial window count
    
    # get subsequent window counts and plot them
    # to plot a fraction for the window ending at position index,
    # call plot(tortoise, index, fraction, window)
        
def orf1(dna, rf, tortoise):
    '''
         Function used to check for starting and stopping codons
         Parameters:
              dna: list of dna being searched
              rf: where the function begins the search
              tortoise: turtle object being used

              return value: none
              '''
    
    inorf1 = False                              #initialize inorf1 as false
    for i in range (3):                         #go through 3 times, checking every 3 letter combo
        for index in range(rf, len(dna), 3):    #start at rf, for the length of the dna, in steps of 3
            code=(dna[index:index + 3])         #code = the 3 letters being checked

        
            if code == "ATG":                   #if the 3 letters = ATG, inorf1=true, pencolor is blue
                inorf1 = True
                tortoise.pencolor('blue')
                bar(tortoise, index, rf)

            elif inorf1 == True and code != "TAA" and code != "TAG" and code != "TGA":
                tortoise.pencolor('blue')       #if the three current letters aren't ending codons don't change anything
                bar(tortoise, index, rf)    

            elif inorf1 == True and code == "TAA" or code == "TAG" or code == "TGA":
                tortoise.pencolor('red')        #if the three current letters are ending codons 
                bar(tortoise, index, rf)        #change inorf2 to false and make pen color red
                inorf1 = False
                
            elif inorf1 == False:               # If inorf1 is false don't change anything
                tortoise.pencolor('red')
                bar(tortoise, index, rf)
                

                
                
            
    
    # to place a bar in the current color over the codon starting at 
    # position index in reading frame rf, call
    # bar(tortoise, index, rf)

def viewer(dna):
    """Display GC content and ORFs in 3 forward reading frames."""
    
    dna = dna.upper()      # make everything upper case

    tortoise = turtle.Turtle()
    screen = tortoise.getscreen()
    screen.setup(width, height)                 # make a long, thin window
    screen.setworldcoordinates(0, 0, cols, rows) # scale coord system so 1 char fits at each point
    screen.tracer(100)
    tortoise.hideturtle()
    tortoise.speed(0)
    tortoise.up()
    
    # Draw DNA string in window.
    
    for index in range(len(dna)):
        tortoise.goto(index % cols, index // cols)
        tortoise.write(dna[index], font = ('Courier', 9, 'normal'))
        
    # Find ORFs in forward reading frames 0, 1, 2.
    
    tortoise.width(5)
    for index in range(3):
        orf1(dna, index, tortoise)
        
    # Plot GC frequency.
    
    tortoise.width(1)
    gcFreq(dna, 5, tortoise)

    screen.update()
    screen.exitonclick()
            
def main():
    # Read DNA from a file and find ORFs
    
    inputFile = open('Eco536-500.txt', 'r')
    dna = inputFile.read()
    viewer(dna)

main()
