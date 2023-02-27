
'''
# refactory_mentorship_projects

## 1. Guessing game

- The guessing game that we are going to implement in python has simple rules.
- First, the program generates a random number between 1 and 99.
- Then, it asks the user to guess the number.
- If the user enters a number less than the number generated by the system, the system tells the user that the guess is low. It then asks the user to guess the number again.
- If the number entered by the user is greater than the system-generated number, the system tells the user that guessed number is larger. It then asks the user to guess the number again.
- If the user guesses the number correctly, the system informs to the user and the game ends
'''

import random


number = random.randint(1,99)
myGuess = int(input('Guess the number I have: '))
'''
while True:
    myGuess = int(input('Guess the number I have: '))
    if(myGuess < number):
        print('Your guess is low')
        #mySecondGuess = int(input('Guess the number again: '))
    elif(myGuess > number):
        print('Your guess is larger than the number')
        #mySecondGuess = int(input('Guess again: '))
    else:
        print('Hooray!!! Your guess is correct! ')
        break
'''

while myGuess != number: # the while loop will run as long as the guess and the number are not equal
    if(myGuess < number):   # checking whether the guess is lower than the number
        print('Your guess is low')  # letting the user know the guessed number is smaller than the number
    else: # this is the case where (myGuess > number) 
        print('Your guess is larger than the number') # letting the user know the guessed number is bigger than the number
    myGuess = int(input('Guess again: ')) # myGuess is assigned to the new Guess from the user

print('Hooray!!! Your guess is correct! ') # the code reaches here when the guess and number are equal. Let the user know the guess is correct
print('---------------Guessing Game has ended---------------')