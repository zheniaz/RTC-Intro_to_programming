# One foot equals 12 inches. Write a function named feet_to_inches that accepts a number of feet
# as an argument and returns the number of inches in that many feet.
# Use the function in a program that prompts the user to enter a number of feet
# then displays the number of inches in that many feet.

INCHES_PER_FOOT = 12

def feet_to_inches (feet) :
    return feet * INCHES_PER_FOOT

current_feet_number = int(input("Enter the number of feet: "))
inches = feet_to_inches(current_feet_number)
print(f"{current_feet_number} feet is equal to {inches} inches.")