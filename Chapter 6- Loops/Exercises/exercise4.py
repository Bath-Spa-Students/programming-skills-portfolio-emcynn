# Exercise 4: Deli
'''Make a list called sandwich_orders and fill it with the names of various sandwiches. Then make an empty list called finished_sandwiches. 

Loop through the list of sandwich orders and print a message for each order, such as I made your tuna sandwich. As each sandwich is made, move it to the list of finished sandwiches. After all the sandwiches have been made, print a message listing each sandwich that was made.'''

#List of sandwich orders 
sandwich_orders = ['egg', 'ham', 'chicken', 'turkey', 'nutella']

#Empty list for finished sandwiches
finished_sandwiches = []

#Remove an order from the list 
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I'm working on your " + current_sandwich + " sandwich.")
    
#Add the finished sandwich to the other list
    finished_sandwiches.append(current_sandwich)

#Print the list of the finished sandwich orders 
print("\n")
for sandwich in finished_sandwiches:
    print(f"Your " + sandwich + " sandwich is done.")

