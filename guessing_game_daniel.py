#This program is a guessing game where you input a number between 1 and 99. The program terminates once the user inputs the correct number.

#welcome note to user.

print("Welcome to Ortega's World")
print("Guess any number between 1 and 99. ")



"""
Use import function to import a list of random number 1 - 99.
Commit a memory space numb with our range of random numbes
User can only guess an integer which they are to input on our screen
Given that the guessed number might be higher or lower than the random number, we use an if, elif and else function
Use the break function to avoid having an infinite loop and end the game.

"""

import random
numb = random.randrange(1, 99)
guess = int(input("Enter number: "))

while numb!= guess:
    if guess < numb:
        print("Number is low. ")
        guess = int(input("Enter Number Again: "))

    elif guess > numb:
        print("Number is high. Please Guess Again: ")
        guess = int(input("Enter Number Again: "))

    else:
      break
print("Voila...!!!. You Guessed Right")
                    
#end                    
