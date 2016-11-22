


def countdown(n):
    for i in range(n,0,-1):
        print(i)


def average(low, high):
    sum=0
    for item in range(low,high+1):
        sum = sum+item
    y = sum/((high+1)-low)
    return(y)
    
    
def factorial(n):
    answer=1
    for i in range(1,n+1):
        answer=i



def fun(number, iterations):
    for i in range(iterations):
        newNumber=(number//10)**2
        number2=(number%10)**2
        number=newNumber+number2
        print(number)
        


def clock(ticks):
    minutes = 0
    hours = 0
    print('{0:>2}:{1:0>2}'.format(0, 0))
    for i in range(ticks-1):
        minutes = (minutes+1)%60
        if minutes % 60 == 0:
            hours = hours +1
            
        if hours % 12 == 0:
            hours = 0
        print(hours,":",minutes)


def growth2(totalDays):
    population = 100
    for i in range(totalDays):
        population = (population+3)-.5
        print(int(population))


def sum (n):
    answer=0
    for i in range(1,n+1):
        answer = answer+i
    return(answer)
    

def main():
    fun(25,5)

main()
    
