#Exercise 5: Cities
#Write a function called describe_city() that accepts the name of a city and its country. The function should print a simple sentence. Give the parameter for the country a default value. Call your function for three different cities, at least one of which is not in the default country.

def describe_city(city, country='Turkey'):
    print(f"{city} is a city located in {country}.")

#Call function for three different cities
describe_city('Konya')
describe_city('Milan', 'Italy') #Not in the default country
describe_city('Antalya')