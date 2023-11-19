#Exercise 4: Rivers
'''Make a dictionary containing three major rivers and the country each river runs through.
* Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
* Use a loop to print the name of each river included in the dictionary.
* Use a loop to print the name of each country included in the dictionary.'''

#Dictionary of rivers 
rivers = {
    'Yangtze River': 'China',
    'Nile River': 'Egypt',
    'Amazon River': 'South America',
    }

#Print sentence about each river
for river, country in rivers.items():
    print(f"The {river} flows through {country}.")

#Display names of each river 
print("\nRivers included in the dictionary:")
for river in rivers:
    print("• " + river)

#Display names of each country
print("\nCountries included in the dictionary:")
for country in rivers:
    print("• " + country)