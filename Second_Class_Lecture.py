# 1. Write an if-else statement that displays 'Speed is normal' if the speed variable is within the range of 24 to 56.
#   If the speed variable’s value is outside this range, display 'Speed is abnormal'.

current_speed = int(input("Enter the current speed in miles per gallons: "))

if 24 <= current_speed <= 56:
    print("Speed is normal")
else:
    print("Speed is abnormal")

# 2. Running on a particular treadmill you burn 4.2 calories per minute.
#   Write a program that uses a loop to display the number of calories burned after 10, 15, 20, 25, and 30 minutes.

BURN_CALORIES_PER_MINUTE = 4.2

for i in range(10, 31, 5):
    calories_burned = i * BURN_CALORIES_PER_MINUTE
    print(calories_burned)