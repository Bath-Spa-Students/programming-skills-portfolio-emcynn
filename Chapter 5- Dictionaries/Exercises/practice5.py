#Practice Exercise 5
#Write a Python program to merge two dictionaries into one.

#Two dictionaries
dictionary1 = {'a': 1, 'b': 2}
dictionary2 = {'c': 3, 'd': 4}

#Merge the dictionaries with the ** unpacking operator
merged_dictionary = {**dictionary1, **dictionary2}

#Display the updated dictionary
print("Merged Dictionary:", merged_dictionary)