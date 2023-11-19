#Exercise 2: Alien Colors #2
'''Choose a color for an alien as you did in Exercise 5-3, and write an if-else chain.
•If the alien's color is green, print a statement that the player just earned 5 points for shooting the alien.
•If the alien's color isn't green, print a statement that the player just earned 10 points.
•Write one version of this program that runs the if block and another that runs the else block.'''

#Assigning a color to the Alien 
alien_color = 'green'

#Running the if block
if alien_color == 'green':
    print("You earned 5 points!")
else:
    print("You earned 10 points!")

#Running the else block
alien_color = 'red'
if alien_color == 'green':
    print("You earned 5 points!")
else:
    print("You earned 10 points!")