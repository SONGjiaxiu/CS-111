# CS 111
# Created by Taylor Heilman
# December 9, 2014
# An simulation of a periodic comets' orbiting path


import turtle
import random
import time


from turtle import *
def comet():
    ''' Comet function.  Asks the user for his/her desired input and then graphs
        the corresponding comet.
        Pre: input must be a value from 1-6
        Post: uses turtle graphics to draw the orbit of desired comet.
    '''

    comet = int(input('''Which comet would you like you simulate?:
                    Halley's Comet = 1
                    Ikeya–Zhang Comet = 2
                    Encke's Comet = 3
                    Comet Hartley 2 = 4
                    Tempel Comet = 5
                    Comet Holmes = 6

                    Type the number associated with your desired comet:  '''))



    
    if comet == 1: #"Halley's Comet"
        speed(1)
        shapesize(.5) #size of comet
        ht()
        up()
        setposition(-23,38)  # set turtle position
        right(230)
        st()
        down()
        shape('circle')
        bgpic('halley.gif') #change background
        bgcolor('black')
        orbit = 75         #orbital period of 75 years
        counter(orbit)
        print("Next appearance will be in 2061")
        fact()
        while True:
            red = random.random() # returns a number between 0 and 1
            green = random.random()
            blue = random.random()
            color(red,green,blue)
            circle(100)

  

    elif comet == 2: #"Ikeya–Zhang Comet":
        speed(1)
        shapesize(.5)   #size of comet
        ht()
        up()
        setposition(-55,22) # set turtle position
        right(65)
        st()
        down()
        shape('circle')
        bgpic('ikeya.gif')  #change background
        bgcolor('black')
        orbit = 366.41         #orbital period of 366.41 years
        counter(orbit)
        print("Next appearance will be in 2343")
        fact()
        while True:
            red = random.random() # returns a number between 0 and 1
            green = random.random()
            blue = random.random()
            color(red,green,blue)
            circle(200)

    elif comet == 3: #"Encke's Comet":
        speed(2)
        shapesize(.5)   #size of comet
        ht()
        up()
        setposition(-75,25)  # set turtle position
        right(95)
        st()
        down()
        shape('circle')
        bgpic('encke.gif')  #change background
        bgcolor('black')
        orbit = 3.3      #orbital period of 3.3 years
        counter(orbit)
        fact()
        while True:
            red = random.random() # returns a number between 0 and 1
            green = random.random()
            blue = random.random()
            color(red,green,blue)
            circle(40)
        

    elif comet == 4: #"Comet Hartley 2": 
        speed(2)
        shapesize(.5)   #size of comet
        ht()
        up()
        setposition(-55,55)
        right(135)
        st()
        down()
        shape('circle')
        shapesize(.5)
        bgpic('hartley.gif')  #change background
        bgcolor('black')
        orbit = 6.46             #Orbital period of 6.46 Years
        counter(orbit)
        fact()
        #for i in range():
        while True:
            red = random.random() # returns a number between 0 and 1
            green = random.random()
            blue = random.random()
            color(red,green,blue)
            circle(58)
       



        
    elif comet == 5: #"Tempel": 
        speed(2)
        shapesize(.5)  #size of comet
        ht()
        up()
        setposition(-15,5) # set turtle position
        right(-55)
        st()
        down()
        shape('circle')
        bgpic('tempel.gif')  #change background
        bgcolor('black')
        orbit = 6.5         #orbital period of 6.5 years
        counter(orbit)
        fact()
        while True:
            red = random.random() # returns a number between 0 and 1
            green = random.random()
            blue = random.random()
            color(red,green,blue)
            circle(50)


    elif comet == 6: #"Comet Holmes": 
        speed(6)
        ht()
        up()
        setposition(-23,38)  # set turtle position
        right(200)
        st()
        down()
        shape('circle')
        shapesize(.5)   
        bgpic('holmes.gif')  #change background
        bgcolor('black')
        orbit = 6.9            # Orbital period= 6.9 years
        counter(orbit)
        fact()
        while True:
            red = random.random() # returns a number between 0 and 1
            green = random.random()
            blue = random.random()
            color(red,green,blue)
            circle(45)


    else:
        print('''
        The input value does not correspond to a comet, please try again.
  

                                                                         ''')                                                                          
        main()       


     

def counter(orbit):
    ''' counter function.  Prints a count of the amounf of years it takes for
        the comet to complete an orbit of the Sun.
        Pre: input orbit is a positive int/float
        Post: Prints numbers from 0-input value and prints total orbital period.
        '''
    years = 0
    print('Orbital Period:')
    while years < orbit+1:

        if orbit > 50:
            print(years, 'Years')
            years = years + 5
            if years >= int(orbit):
                print('Total Orbital Period of', orbit, 'Years')
                return 0

        else:
            print(years, 'Years')
            years = years +1
            if years == int(orbit):
                print(years, 'Years')
                print('Total Orbital Period of', orbit, 'Years')
                return 0




def fact():
    
    y =   random.random()
    x = int(y*10)

    print('''
Fun Fact:''')
        
    if x == 1:
        print('''The nucleus of a comet is made of ice and can be as small as a few meters across to giant boulders a few kilometres across.''')
    elif x ==2:
        print('''The closest point in a comet’s orbit to the Sun is called “perihelion”. The most distant point is called “aphelion”.''')
    elif x == 3:
        print('''As a comet gets closer to the Sun, it begins to experience heat. That causes some of its ices to sublimate (similar to dry ice sizzling in sunlight). If the ice is close to the comet’s surface, it may form a small “jet” of material spewing out from the comet like a mini-geyser.''')
    elif x ==4:
        print('''Material streams from comets and populates the comet’s orbit. If Earth (or another planet) happens to move through that stream, those particles fall to Earth as meteor showers.''')
    elif x ==5:
        print('''As a comet gets close to the Sun, it loses some of its mass due to the sublimation. If a comet goes around enough times, it will eventually break up. Comets also break up if they come TOO close to the Sun or another planet in their orbits.''')
    elif x == 6:
        print('''Comets are usually made of frozen water and supercold methane, ammonia and carbon dioxide ices. Those are mixed with rock, dust, and other metallic bits of solar system debris.''')
    elif x ==7:
        print('''Comets have two tails: a dust tail (which you can see with the naked eye) and a plasma tail, which is easily photographed but difficult to see with your eyes.''')
    elif x ==8:
        print('''Currently there are over 3,000 known comets. However, scientists predict that there could be up to one billion comets in our solar system''')
    elif x== 9:
        print('''The most famous comet is Halley's Comet. It has been observed since at least 240 B.C. Its orbit makes it visible from Earth every 76 years. It was named after the British astronomer Edmond Halley.''')
    else:
        print('''The Oort cloud is an outer region of the Solar System 50,000-150,00 times the distance from the Sun to Earth that is believed to contain dormant comets. Some of the comets that originate here have orbits lasting millions of years.''')


    
            
def main():
    ''' main function.  Calls upon other functions

    Parameters:
        none

    Return Value:
        none
    '''   
    turtle.bgpic('planetsmvmt.gif')
    turtle.bgcolor('black')
    turtle.shape('circle')
    comet()

  
   
    
main()


