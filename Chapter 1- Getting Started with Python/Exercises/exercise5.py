#import math module
from math import pi

#request input from user
r = float(input ("What is the radius of the circle : "))

#area of the circle based on the inputted radius
print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))