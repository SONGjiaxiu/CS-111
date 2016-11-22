import matplotlib.pyplot as mpl


def pond(years):
    """Simulation of fish in lake"""

    population = 12000
    for year in range(1,years+1):
        population= population + 0.08 * population - 1500
        print(year,population)

def pond2():
    """Simulation of fish in lake"""

    population = 12000
    year=1
    populationList=[]
    yearList=[]

    
    while population>0:
        population= population + 0.08 * population - 1500
        
        populationList.append(population) #adds population to our list
        yearList.append(year)

        print(year,population)
        year=year+1

        #print(yearList, populationList

    mpl.plot(yearList, populationList)
    mpl.xlabel('Year')
    mpl.ylabel('Number of Fish')
    mpl.show()

def main():
    pond2()

main()




"""while <condition>, we use the while loop to 
run the simulation for as long as their is a poistive
population, because in real life their can't be a negative population
"""
