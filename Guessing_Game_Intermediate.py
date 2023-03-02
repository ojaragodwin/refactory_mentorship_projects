import random

# Generate a random number between 1 and 99
number = random.randint(1, 99)

# Set the maximum number of guesses allowed
max_guesses = 5

# Keep track of the number of guesses
num_guesses = 0

# Keep looping until the user guesses the number correctly or runs out of guesses
while num_guesses < max_guesses:
    # Ask the user to guess the number
    guess = int(input("Guess a number between 1 and 99: "))

    # Increment the number of guesses
    num_guesses += 1

    # Check if the guess is correct
    if guess == number:
        print("Congratulations! You guessed the number in", num_guesses, "guesses.")
        break

    # Check if the user has run out of guesses
    if num_guesses == max_guesses:
        print("Sorry, you have run out of guesses. The number was", number)
        break

    # Give the user a hint
    if guess < number:
        print("Your guess is too low.")
    else:
        print("Your guess is too high.")

    # Ask the user to guess again
    print("You have", max_guesses - num_guesses, "guesses left.")
    print() # Print a blank line for spacing
