#Practice Exercise 2
#Write a Python function that calculates the factorial of a given positive integer using recursion.

def recur_factorial(x):  
   if x == 1:  
       return x  
   else:  
       return x*recur_factorial(x-1)  
#Request input from the user  
user_input = int(input("Input a number: "))  
#Check if the number is negative  
if user_input < 0:  
   print("Error occurred. Negative numbers cannot have factorials")  
elif user_input == 0:  
   print("The factorial of 0 is 1")  
else:  
   print("The factorial of",user_input,"is",recur_factorial(user_input))  