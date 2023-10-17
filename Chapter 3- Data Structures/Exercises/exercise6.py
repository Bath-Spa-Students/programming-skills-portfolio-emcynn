#Shrinking Guest List
guests = ["Maryel Angela", "Seif Ibrahim", "Heba Albari"]

name = guests[0].title()
print("Greetings, " + name + "!" + " Please join us for a lovely dinner. We'd be delighted to have you for an enjoyable evening.")

name = guests[1].title()
print("Greetings, " + name + "!" + " Please join us for a lovely dinner. We'd be delighted to have you for an enjoyable evening.")

name = guests[2].title()
print("Greetings, " + name + "!" + " Please join us for a lovely dinner. We'd be delighted to have you for an enjoyable evening.")

#The current table won't arrive on time
print("\nUnfortunately, we can't accommodate the third guest.")

name = guests.pop()
print("Sorry, " + name.title() + " there's no room at the dinner table.\n")

# There should be two people left. Let's invite them.
name = guests[0].title()
print(name + ", please come to dinner.")

name = guests[1].title()
print(name + ", please come to dinner.")

# Empty out the list.
del(guests[0])
del(guests[0])

# Prove the list is empty.
print(guests)