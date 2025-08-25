# Project 2 - The Perfect Guess

import random

def perfect_guess():
    # Generate a random number between 1 and 100
    number = random.randint(1, 100)
    guesses = 0
    guess = None

    print("🎯 Welcome to The Perfect Guess Game!")
    print("I have chosen a number between 1 and 100. Can you guess it?")

    while guess != number:
        # Take user input
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("❌ Please enter a valid number.")
            continue

        guesses += 1

        if guess > number:
            print("Lower number please 👇")
        elif guess < number:
            print("Higher number please 👆")
        else:
            print(f"✅ Congratulations! You guessed the number {number} in {guesses} attempts.")

# Run the game
if __name__ == "__main__":
    perfect_guess()
