import random

# Generate a random winning number between 500 and 1000
winning_number = random.randint(500, 1000)

# Prompt the user to guess a number
guess = int(input("Guess a number between 500 and 1000: "))

# Check if the user guessed correctly
if guess == winning_number:
    print("YOU WIN!!!")
     # Check if the guess is too low or too high
elif guess < winning_number:
    print("Too low!! Guess Again")
else:
    print("Too high !! Guess Again")

# Print the winning number (for testing purposes)
print("The winning number was:", winning_number)