#Exercise 5: Pets
'''Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the owner’s name. Store these dictionaries in a list called pets. Next, loop through your list and asyou do, print everything you know about each pet.'''

#Empty list to input the pets in.
pets = []

#Store information about each pet.
pet = {
    'Animal type': 'Cat',
    'Name': 'Kyo',
    'Pet Owner': 'Rianne',
    'Weight': '4kg',
    'Eats': 'Dry cat food',
}
pets.append(pet)

pet = {
    'Animal type': 'Puppy',
    'Name': 'Chu-chu',
    'Pet Owner': 'Marvey',
    'Weight': '3kg',
    'Eats': 'Meat & plant-based food',
}
pets.append(pet)

pet = {
    'Animal type': 'Kitten',
    'Name': 'Nacci',
    'Pet Owner': 'Yani',
    'Weight': '1kg',
    'Eats': 'Canned cat food',
}
pets.append(pet)

#Display details about each pet.
for pet in pets:
    print("\nEverything I know about " + pet['Name'].title() + ":")
    for key, value in pet.items():
        print("\t" + key + ": " + str(value))