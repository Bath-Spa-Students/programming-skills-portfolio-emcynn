#Exercise 3: Print date and Time
#Write a Python program to display the current date and time.

#Access datetime module 
import datetime

#Get current date 
current_date = datetime.date.today()
print("Current Date: ", current_date)

#Get current time
current_time = datetime.datetime.now().time()
print("Current Time: ", current_time)