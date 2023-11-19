#Practice Exercise 3
#Write a python program that takes an input 5 from user and then type cast those values to string, int and float in the separate variables. Print all the variables.

#Request input & type cast
input = input("Enter a value: ")
string, int, float = str(input), int(input), float(input)

#Displaying the result
print(f"Original input: {input}")
print(f"As string: {string}")
print(f"As integer: {int}")
print(f"As float: {float}")