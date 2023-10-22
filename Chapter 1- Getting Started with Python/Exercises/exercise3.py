#Print date and Time
#Write a Python program to display the current date and time.

import datetime
current_date = datetime.date.today()
print("Current Date: ", current_date)

current_time = datetime.datetime.now().time()
print("Current Time: ", current_time)