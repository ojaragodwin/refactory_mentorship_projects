import random


number = int(random.randint(1,99))
your_guess = int(input('enter your number: ' ))
if((number < your_guess) ):
    
    print("your guess is  less than the number,please guess again")
elif(number > your_guess):
    print("your guess is  greater than the number,please guess again")   
else:
    print("you have guessed right ,you win") 