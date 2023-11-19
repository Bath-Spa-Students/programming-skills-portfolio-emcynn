#Practice Exercise 5
#Write a Python program that uses a while loop to find the largest number among a series of user-input values until they enter '0' to exit the loop.

#Initialize a variable to store the largest number
largest_number = None

#Use a while loop to repeatedly prompt the user for input
while True:
    user_input = input("Enter a number (enter '0' to exit): ")

    if user_input == '0':
        break

    #Convert the user input to a float and ignore invalid input
    try:
        number = float(user_input)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue

    #Update the largest number if the current number is greater
    if largest_number is None or number > largest_number:
        largest_number = number

#Display the largest input number
print("The largest number entered is:", largest_number if largest_number is not None else "None")