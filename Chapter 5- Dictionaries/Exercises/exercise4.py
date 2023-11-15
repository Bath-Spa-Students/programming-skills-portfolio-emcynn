#Exercise 4: Rivers
'''Make a dictionary containing three major rivers and the country each river runs through. One key-value pair might be 'nile': 'egypt'.
* Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
* Use a loop to print the name of each river included in the dictionary.
* Use a loop to print the name of each country included in the dictionary.'''

rivers = {
    'Yangtze River': 'China',
    'Nile River': 'Egypt',
    'Amazon River': 'South America',
    }

for river, country in rivers.items():
    print("The " + river.title() + " flows through " + country.title() + ".")

print("\nThis data set encompasses the following rivers:")
for river in rivers.keys():
    print("• " + river.title())

print("\nThis data set encompasses the following countries:")
for country in rivers.values():
    print("• " + country.title())