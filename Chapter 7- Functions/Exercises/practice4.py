#Practice Exercise 4
#Write a Python program that defines a function to calculate the area of a circle, and then calls that function with a given radius.

import math
def circle_area(radius):
    return math.pi * radius**2

#Testing it out:
radius = int(input("Input the radius: ")) 
print(f"The area of a circle with radius {radius} is: {circle_area(radius):.2f}")