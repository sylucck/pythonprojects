# Ask the user to roll a dice
# Import the random module
# If user enter y, 
  # Generate two random numbers
  #Print the numbers
# if the user enters n,
  # Print a  message and exit the program
import random


while True:
    # Ask the user for input
    user_input = input("Do you want to roll the dice? (y/n): ").strip().lower()
    if user_input == "y":
        # Generate two random numbers between 1 and 6
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        # Print the numbers
        print(f'You rolled a {dice1} and a {dice2}')
    elif user_input == "n":
        # Print a message and exit the program
        print("Thanks for playing. Goodbye!")
        break
    else:
        # If the user enters an invalid input, print a message
        print("Invalid input. Please enter 'y' or 'n'.") 