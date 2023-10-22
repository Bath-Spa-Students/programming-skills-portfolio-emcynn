#USB Shopper 
'''A girl heads to a computer shop to buy some USB sticks. She loves USB sticks and wants as many as she can get for £50. They are £6 each.

Write a programme that calculates how many USB sticks she can buy and how many pounds she will have left.

You will to use the arithmetic operators to complete this exercise.'''

#Define the cost of one USB stick and the total budget
usb_stick = 6
budget = 50

#Calculate the maximum number of USB sticks she can buy
num_usb_sticks = budget // usb_stick

#Calculate remaining money after buying USB sticks
remaining_budget = budget % usb_stick

#Results
print("The girl can buy", num_usb_sticks, "USB sticks with £50.")
print("She will have £", remaining_budget, "left.")
