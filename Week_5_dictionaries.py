# Write a program that creates a dictionary containing the U.S. states as keys, and their capitals as values.
# (Use the Internet to get a list of the states and their capitals.)
# The program should then randomly quiz the user by displaying the name of a state and asking the user to enter that state’s capital.
# The program should keep a count of the number of correct and incorrect responses.
# (As an alternative to the U.S. states, the program can use the names of countries and their capitals.)

import random
from geo_data import us_states_and_capitals

print("Hello! Let's play a game. Guess the U.S. state's capital name.")
print("Press 'y' to start, or 'n' to quit.")

def wants_to_play():
    while True:
        char = input("Press 'y' to start, or 'n' to quit: ").lower()
        if char == 'y':
            print("Starting game...\n")
            return True
        elif char == 'n':
            print("Quitting.\n")
            return False
        else:
            print("Invalid input. Please press 'y' or 'n'.\n")

correct = 0
incorrect = 0

print("Please enter your answer in lowercase.")
while wants_to_play():
    state, capital = random.choice(list(us_states_and_capitals.items()))
    print(f"What's the capital city of {state}?")
    your_city = input().lower()
    if capital.lower() == your_city:
        print("🎉 Congratulations, you won!\n")
        correct += 1
    else:
        print(f"❌ Sorry, you're mistaken! The correct answer is {capital}.\n")
        incorrect += 1

print("Thank you for playing! You got {correct} correct and {incorrect} incorrect.")


