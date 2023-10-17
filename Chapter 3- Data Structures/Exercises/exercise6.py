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

# Invite the 2 remaining guests
name = guests[0].title()
print(name + ", you are still invited to dinner.")

name = guests[1].title()
print(name + ", you are still invited to dinner.")

# Clear out the list.
del(guests[0])
del(guests[0])

# Prove the list is empty.
print(guests)