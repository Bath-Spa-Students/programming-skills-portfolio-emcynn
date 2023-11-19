#Practice Exercise 1
#Write a Python function that takes two numbers as arguments and returns their sum.

def add_numbers(a, b):
    return a + b

x = int(input("Enter the first number:"))
y = int(input("Enter the second number:"))
sum = add_numbers(x, y)
print("The sum is:", sum)