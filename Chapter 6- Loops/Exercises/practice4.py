#Practice Exercise 4
#Write a Python program that uses the break statement to exit a for loop when a specific condition is met.

#Set the maximum number of entries
max_entries = 5

#Initialize an empty list to store user input
numbers = []

#Iterate over the predefined entries with for loop 
for entry_number in range(1, max_entries + 1):
    user_input = int(input(f"Input number {entry_number} (enter a negative number to stop): "))

    #Exit if the user entered a negative number
    if user_input < 0:
        print("Negative number entered. Stopping the input.")
        break  

    #Add the non-negative number to the list
    numbers.append(user_input)

#Display the inputs from the user
print("Numbers entered:", numbers)