#USB Shopper 
# Define the cost of one USB stick and the total budget
usb_stick = 6
budget = 50

# Calculate the maximum number of USB sticks she can buy
num_usb_sticks = budget // usb_stick

#Calculate remaining money after buying USB sticks
remaining_budget = budget % usb_stick

#Results
print("The girl can buy", num_usb_sticks, "USB sticks with £50.")
print("She will have £", remaining_budget, "left.")
