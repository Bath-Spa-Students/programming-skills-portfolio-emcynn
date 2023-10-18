#Shrinking Guest List
'''You just heard that one of your guests can’t make the
dinner, so you need to send out a new set of invitations. You’ll have to think of
someone else to invite.

•Start with your program from Exercise 3-4. Add a print() call at the end of your program stating the name of the guest who can’t make it.

•Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.

•Print a second set of invitation messages, one for each person who is still in your list.'''

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