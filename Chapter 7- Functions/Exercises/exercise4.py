#Exercise 4: Large Shirts
#Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.

def make_shirt(size='large', message='I love Python!'):
    print(f"\nI'm going to create a {size}-sized t-shirt.")
    print(f'Its text design will be, "{message}".')

#Call the function to make a large-sized shirt with the set default message
make_shirt()

#Call the function to make a medium-sized shirt with the set default message
make_shirt(size='medium')

#Call the function to make a medium-sized shirt with a different message
make_shirt('medium', 'Just do it')