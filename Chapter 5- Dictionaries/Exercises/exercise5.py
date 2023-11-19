#Exercise 5: Pets
'''Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the owner's name. Store these dictionaries in a list called pets. Next, loop through your list and asyou do, print everything you know about each pet.'''

#Store information about each pet.
pets = [
    {'Animal type': 'cat', 'Pet Owner': 'Rianne'},
    {'Animal type': 'puppy', 'Pet Owner': 'Marvey'},
    {'Animal type': 'bird', 'Pet Owner': 'Denzy'},
]

#Display details about each pet.
for pet in pets:
    animal = pet['Animal type']
    owner = pet['Pet Owner']
    print(f"{owner} owns a {animal}.")