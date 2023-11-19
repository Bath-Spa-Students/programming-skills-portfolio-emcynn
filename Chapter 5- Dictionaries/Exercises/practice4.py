#Practice Exercise 4 
#Write a Python program to iterate through both the keys and values of a dictionary and print them

#Dictionary
dictionary = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

#Iterate through keys and values
for key, value in dictionary.items():
    print(f"Key: {key}, Value: {value}")