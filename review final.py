def TowerOfHanoi(n,source,spare,destination): # n= number of disks
    if n ==1:     #base case
        print("move from", source, "to", destination)
    else:
        #move (n-1) disks from source to spare
        TowerOfHanoi(n-1,source,destination,spare)
        print("move from", source,"to",destination)
        TowerOfHanoi(n-1,spare,source,destination)




def bacteria(): # B(t+1) = B(t) + (B(t) * 10/100)   B(0) = 100
    B = 100
    for t in range(100):
        B = B + (B*0.1)


def bacteria2(dt):  #B(t+delta t) = B(t) + (B(t) * 10/100) * delta t
    B = 100
    time = 0
    while time < 100:
        B = B + (B*.1)*dt
        time = time + dt
        
"""Solving a recursive problem:  input list and string
                                 returns list with all string input removed
list = ["a","b","c","a","d"]      remove 'a'
1. make an example
    if you have a list or string. Recursive break up = look at first
    thing in list/string and the rest of the list /string
2.Check the first element in the list, if it = 'a' remove from
    list and return the rest of the list, else keep first element and return
    rest of the list
3.


"""

def remove(list,string):
    if len(list) == 0:  #base case
        return []
    
    if list[0] == string:              #work
        return remove(list[1:],string)


    else:
        return [list[0]] + remove(list[1:], string)
        


def upper(string):
    if len(string) == 0:
        return 0

    if s[0].lower() != s[0]:
        return 1 + upper(string[1:])
    else:
        return upper(string[1:])


def searchList(l,t):
    for row in range(len(l)):
        for col in range(len(l[0])):
            if l[row][col] == t:
                return True
    return False


def firstLetter(l):
    d = {}
    for i in range(len(list)):
        word = l[i]
        letter = word[0]
        if letter in d:
            d[letter] = d[letter] + 1
        else:
            d[letter] = 1
    return d


def length(l):
    if l == []:
        return 0
    return 1 + length(l[1:])



    
def bous(salary):
    for key in salary:
        salary[key] = salary[key] * 1.05

def main():
    TowerOfHanoi(15,1,2,3)

main()
