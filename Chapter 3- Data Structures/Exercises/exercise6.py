#Shrinking Guest List
'''You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests.

•Start with your program from Exercise 3-5. Add a new line that prints a message saying that you can invite only two people for dinner.
•Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
•Print a message to each of the two people still on your list, letting them know they’re still invited.
•Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.'''

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

#Invite the 2 remaining guests
name = guests[0].title()
print(name + ", you are still invited to dinner.")

name = guests[1].title()
print(name + ", you are still invited to dinner.")

#Clear out the list.
del(guests[0])
del(guests[0])

#Prove the list is empty.
print(guests)