#Exercise 3: T-Shirt  
# Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. The function should print a sentence summarizing the size of the shirt and the message printed on it. Call the function once using positional arguments to make a shirt. Call the function a second time using keyword arguments.

#Summary of the shirt design & sizes 
def make_shirt(size, message):
    print("\nI'm going to make a " + size + "-sized t-shirt.")
    print('Its text design will be, "' + message + '"')

#Call the function using positional arguments
make_shirt('small', 'Just do it!')

#Call the function using keyword arguments 
make_shirt(message="Live, laugh, love!", size='medium')