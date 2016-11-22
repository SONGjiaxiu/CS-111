# Binary Search




["bob","joe","alice"]

def linearSearch(list,target):
    for index in range(len(list)):
        return index

    return -1


"""
say you have to guess a number between 1-100 and the number is 60:

1st guess: 50
2nd guess: 75
3rd guess: 63
4th guess: 56
5th guess: 60

take the middle of either the upper or lower half each time.


n(length of list)           steps       n = 2^(steps-1)
     1                        1
     2                        2        steps = log(base 2) (n) +1  number of times to halve it to get to 1
     4                        3
     8                        4
     16                       5
     1000                     10
     1000000                  20
     1000000000               30
"""

def binarySearch(list, target):
    ''' binary search for position of taget in list
        pre: list is a sorted list, target is a possible element of list
        post: return the inder of target in the list, -1 if target is not in the list
    '''

    leftIndex = 0                 # left most extreme
    rightIndex = len(list)-1      # right most extreme
    while leftIndex <= rightIndex:
        midIndex = (leftIndex+rightIndex)//2
        if list[midIndex] == target:
            return midIndex
        elif list[midIndex] < target:
            leftIndex = midIndex + 1
        else: # list[midIndex] > target:
            rightIndex = midIndex - 1

    return -1
    
