#Practice Exercise 5
#Write a Python program that uses the elif statement to determine the season based on the month provided as input.

#Request input (month) as an integer
month = int(input("Enter the month (1-12): "))

#Determine the season based on the month
if 1 <= month <= 12:
    if 3 <= month <= 5:
        season = "Spring"
    elif 6 <= month <= 8:
        season = "Summer"
    elif 9 <= month <= 11:
        season = "Fall"
    else:
        season = "Winter"

    print(f"The season for the {month}'th month of the year is {season}.")
else:
    print("Invalid input. Please enter a number between 1 and 12.")
