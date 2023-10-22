#Exercise 5: Compute area of Circle
#Write a Python program which accepts the radius of a circle from the user and compute the area.

#import math module
from math import pi

#request input from the user
r = float(input ("What is the radius of the circle : "))

#area of the circle based on the inputted radius
print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))