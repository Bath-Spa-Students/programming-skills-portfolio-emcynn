#Exercise 1: Pizza Toppings
#Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. As they enter each topping, print a message saying you’ll add that topping to their pizza.

#Request the user to select a pizza topping 
prompt = "\nEnter a pizza topping of your choice (or 'quit' to finish): "

#Adding the topping to the pizza 
while True:
    pizza_topping = input(prompt)
    if pizza_topping != 'quit':
        print("  I'll add " + pizza_topping + " to your pizza.")
    
#Exit the loop if the user enters "quit" value
    else: 
        print("Okay, that would be all!")
    break