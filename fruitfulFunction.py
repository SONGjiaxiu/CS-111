"""Function Example 9/16  FRUITFUL FUNCTION
the variable volume is given the value of the volume of the sphere
"""

import math

def volumeSphere(radius):
    """A function that computers the volume of a sphere
       Parameters:
          radius: the radius of the sphere

        Return value: the Volume of the sphere
    """
    return (4/3) * math.pi * radius **3  


def volumeShell(innerRadius, outerRadius):
    """A function that computes the volume of a shell
       Parameters:
           innerRadius: the inner radius of the shell
           outerRadius: the outer radius of the shell
    """
    return volumeSphere(outerRadius) - volumeSphere(innerRadius)


def main():
    volume = volumeShell(10,20)
    print(volume)
    
main()


