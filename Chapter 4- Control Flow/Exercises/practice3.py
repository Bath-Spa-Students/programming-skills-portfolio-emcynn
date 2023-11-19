#Practice Exercise 3
#Write a python program with nested decision structures that perform the following: If amount1 is greater than 10 and amount2 is less than 100, display the greater of amount1 and amount2

#Assigning values to amount1 and amount2
amount1 = 85
amount2 = 49

#Check if vars meet conditions 
if 10 < amount1 and amount2 < 100:
    #Display greater amt with max() 
    greater_amount = max(amount1, amount2)
    print("Greater amount:", greater_amount)
else:
    print("Conditions not met.")
