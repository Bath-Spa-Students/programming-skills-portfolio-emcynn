#Practice Exercise 2
#Write a python program that takes courses marks as input and then calculates average of all the courses. After calculating the average, calculate the percentage of a student using total marks. Assume the total of all the courses marks is 500 or take the total marks from the user as input. 

#Number of courses
courses = int(input("Enter the number of courses: "))

#Initialize variables
total_marks = 0

#Input course marks and compute total marks
for i in range(courses):
    total_marks += float(input(f"Input the marks for course {i + 1}: "))

total_possible_marks = 500

#Compute average & percentage
avg = total_marks / courses
pct = (total_marks / total_possible_marks) * 100
print(f"\nAverage marks: {avg}")
print(f"Percentage: {pct}%")