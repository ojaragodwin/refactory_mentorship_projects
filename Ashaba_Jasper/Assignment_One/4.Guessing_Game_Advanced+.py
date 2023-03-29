import random

# Function to get the user's desired range for the generated number
def get_range():
    print("Choose the range of the generated number:")
    while True:
        try:
            min_num = int(input("Minimum number: "))
            max_num = int(input("Maximum number: "))
            if min_num >= max_num:
                raise ValueError("Minimum number must be less than maximum number.")
            break
        except ValueError as e:
            print(e)
    return (min_num, max_num)

# Function to get the user's desired maximum number of guesses
def get_max_guesses():
    while True:
        try:
            max_guesses = int(input("Enter the maximum number of guesses allowed: "))
            if max_guesses < 1:
                raise ValueError("Maximum number of guesses must be at least 1.")
            break
        except ValueError as e:
            print(e)
    return max_guesses

# Function to generate the number within the given specified range
def generate_number(min_num, max_num):
    return random.randint(min_num, max_num)

# Function to calculate the score based on the number of guesses and range of the generated number
def calculate_score(num_guesses, min_num, max_num):
    range_size = max_num - min_num + 1
    max_score = range_size * 10
    penalty = num_guesses * 5
    score = max_score - penalty
    return max(score, 0)

# Get the user's desired range and maximum number of guesses
min_num, max_num = get_range()
max_guesses = get_max_guesses()

# Generate the random number within the specified range
number = generate_number(min_num, max_num)

# Keep track of the number of guesses and score
num_guesses = 0
score = 0

# Keep looping until the user guesses the number correctly or runs out of guesses
while num_guesses < max_guesses:
    # Ask the user to guess the number
    while True:
        try:
            guess = int(input("Guess a number between {} and {}: ".format(min_num, max_num)))
            if guess < min_num or guess > max_num:
                raise ValueError("Guess must be within the specified range.")
            break
        except ValueError as e:
            print(e)

    # Increment the number of guesses
    num_guesses += 1

    # Check if the guess is correct
    if guess == number:
        score = calculate_score(num_guesses, min_num, max_num)
        print("Congratulations! You guessed the number in", num_guesses, "guesses.")
        print("Your score is:", score)
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

    # Calculate the score so far and inform the user
    score = calculate_score(num_guesses, min_num, max_num)
    print("Your score so far is:", score)

    # Ask the user to guess again
    print("You have", max_guesses - num_guesses, "guesses left.")
    print() # Print a blank line for spacing
