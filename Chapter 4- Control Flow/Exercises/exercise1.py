#Exercise 1: Alien Colors #1
'''Imagine an alien was just shot down in a game. Create a variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.
•Write an if statement to test whether the alien’s color is green. If it is, print a message that the player just earned 5 points.
•Write one version of this program that passes the if test and another that fails. (The version that fails will have no output.)'''

#Pass: assigning color green to the Alien 
alien_color = 'green'

#Program version that passes 
if alien_color == 'green':
    print("You earned 5 points!")

#Fail: assigning a different color  
alien_color = 'yellow'

#Program version that fails 
if alien_color == 'green':
    print("You earned 5 points!")