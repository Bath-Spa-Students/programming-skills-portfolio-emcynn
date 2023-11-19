#Practice Exercise 3
#Write a Python program that uses a loop to find the sum of all the numbers from 1 to 100.

#Initialize variable
sum = 0

#Iterate over the range of 1-101
for number in range(1, 101):
    #Add each number to the sum
    sum += number

#Print the sum
print("Sum of numbers from 1-100:", sum)