#Guest List 
#If you could invite anyone, living or deceased, to dinner, who would you invite? Make a list that includes at least three people you’d like to invite to dinner. Then use your list to print a message to each person, inviting them to dinner.

guests = ["Maryel Angela", "Seif Ibrahim", "Heba Albari"]

name = guests[0].title()
print("Greetings, " + name + "!" + " Please join us for a lovely dinner. We'd be delighted to have you for an enjoyable evening.")

name = guests[1].title()
print("Greetings, " + name + "!" + " Please join us for a lovely dinner. We'd be delighted to have you for an enjoyable evening.")

name = guests[2].title()
print("Greetings, " + name + "!" + " Please join us for a lovely dinner. We'd be delighted to have you for an enjoyable evening.")

name = guests[1].title()
print("\nSorry, " + name + " can't make it to dinner.")

# Seif can't attend dinner! Let's invite Yani instead.
del(guests[1])
guests.insert(1, 'Yani Ariele')

# Print the invitations again.
name = guests[0].title()
print("\n" + name + ", please come to dinner.")

name = guests[1].title()
print(name + ", please come to dinner.")

name = guests[2].title()
print(name + ", please come to dinner.")