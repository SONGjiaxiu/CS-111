'''
Taylor Heilman
January 20, 2015

search.py
This goal of this program is to compare the performance of linear search
and binary search.
'''
import random


def linearSearch(list,target):
    '''
    inputs: a list of numbers, a target number
    outputs: an index of the location of the target number in the list or
          -1 if the target element is not present in the list.
    preconditions: a list of numbers, no assumptions about their order.
    postconditions: a returned index (or -1), the list is not changed.
    '''
    for index in range(len(list)):
        if list[index] == target:
            return index

    return -1




'''
Main program:
This subroutine creates a list of randomly generated integers and sorts
them into ascending order.  It then creates a list of random search keys
and attempts to locate the keys within the search list.
'''
def main ():
    n = 10000000      # size of list of numbers
    cap = 200    # values in list are 1 to cap
    m = 10      # number of different targets to search for

    # create list of numbers to search through
    nums = [];
    for i in range(n):
        nums.append(random.randint(1,cap))
    # put them in sorted ascending order
    nums.sort()

    # create a list of random targets to search for
    targets = [];
    for i in range(m):
        targets.append(random.randint(1,cap))

    # for debugging, you can print the original list and/or list of targets
    #print('nums list:', nums)
    #print('targets list: ',targets)

    # create a dictionary for linear search indices
    spots1 = {}
    for target in targets:
        index = linearSearch(nums,target)
        if not target in spots1:
            spots1[target] = index
    print(spots1)


#===========================================================
# call the main program
#===========================================================
main()
