#Exercise 5: No Pastrami
#Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times. Add code near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all occurrences of 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up in finished_sandwiches.

#List of sandwich orders
sandwich_orders = ['egg', 'pastrami', 'ham', 'pastrami', 'chicken', 'pastrami', 'turkey', 'nutella']

#List of finished sandwich orders 
finished_sandwiches = []

#Notify that the deli has run out of pastrami
print(f"I'm sorry, we're all out of pastrami today.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

#Loop through the sandwich orders list 
print("\n")
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I'm working on your " + current_sandwich + " sandwich.")

#Add the finished sandwich to the other list
    finished_sandwiches.append(current_sandwich)

#Print the list of the finished sandwich orders 
print("\n")
for sandwich in finished_sandwiches:
    print(f"Your " + sandwich + " sandwich is ready.")