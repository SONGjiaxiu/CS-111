# CS 111
# Oct. 1, 2014
# An implementation of the SIR model

import matplotlib.pyplot as mpl

def SIR(population, days, dt):
    """Simulates the SIR model of infectious disease and plots
    the population sizes over time.

    Parameters:
    population: the population size
    days: number of days to simulate
    dt: the value of "Delta t" in the simulation (fraction of a day)

    Return value: None
    """

    susceptible = population - 1    # susceptible count = S(t)
    infected = 1.0                  # infected count = I(t)
    recovered = 0.0                 # recovered count = R(t)

    recRate = 0.25                  # recovery rate, r
    infRate = 0.0004                # infection rate, d
    SList = [susceptible]
    IList = [infected]
    RList = [recovered]
    timeList = [0]
    time = 0

    # Loop using the difference equations goes here.

    while time < days:
        newlyInfected = infRate * susceptible * infected * dt
        newlyRecovered = recRate * infected * dt
        susceptible = susceptible - newlyInfected
        infected = infected + newlyInfected - newlyRecovered
        recovered = recovered + newlyRecovered
        time = time + dt
        SList.append(susceptible)
        IList.append(infected)
        RList.append(recovered)
        timeList.append(time)
        
     
    mpl.plot(timeList, SList, label = 'Susceptible')
    mpl.plot(timeList, IList, label = 'Infected')
    mpl.plot(timeList, RList, label = 'Recovered')
    mpl.legend(loc = 'center right')

    mpl.xlabel('Days')
    mpl.ylabel('Individuals')
    mpl.show()
    

def main():
    SIR(2200,30,.01)


main()
    
