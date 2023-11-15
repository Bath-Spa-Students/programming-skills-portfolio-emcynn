#Exercise 5: Compute area of Circle
#Write a Python program which accepts the radius of a circle from the user and compute the area.

#assigning the value of pi
pi = 3.14159 

#request input from the user
r = float(input ("What is the radius of the circle : "))

#area of the circle based on the inputted radius
print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))