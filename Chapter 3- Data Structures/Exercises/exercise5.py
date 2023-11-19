#Exercise 5: Guest List 
'''You just heard that one of your guests can't make the dinner, so you need to send out a new set of invitations. You'll have to think of someone else to invite.
• Start with your program from Exercise 3-4. Add a print() call at the end of your program stating the name of the guest who can't make it.
• Modify your list, replacing the name of the guest who can't make it with the name of the new person you are inviting.
• Print a second set of invitation messages, one for each person who is still in your list.'''

#List of invited guests
guests = ["Maryel Angela", "Seif Ibrahim", "Heba Albari"]

#Printing an invitation message for each person
print(f"Greetings, " + guests[0] + "!" + " Please join us for a lovely dinner. We'd be delighted to have you for an enjoyable evening.")

print(f"Greetings, " + guests[1] + "!" + " Please join us for a lovely dinner. We'd be delighted to have you for an enjoyable evening.")

print(f"Greetings, " + guests[2] + "!" + " Please join us for a lovely dinner. We'd be delighted to have you for an enjoyable evening.")

#Invite someone else since guest[1] can't attend 
print(f"\nSorry, " + guests[1] + " can't make it to dinner.")
del(guests[1])
guests.insert(1, 'Yani Ariele')

#Print the invitations again.
print(f'\n{guests[0]}' + ", please come to dinner.")
print(f'{guests[1]}' + ", please come to dinner.")
print(f'{guests[2]}' + ", please come to dinner.")