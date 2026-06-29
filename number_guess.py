# generate random num btw 1 to 100
# ask user for guess
# invalid num : PRINT error message 

# gives hints to guess the number 
# example - number is 56

# first guess : 20 
# print guess is low

# second guess 60
# print guess is close etc

# if number guessed
# print correct guess

import random

number_to_guess = random.randint(1,100)

while True:
    try:
        guess = int(input('guess a number between 1 and 100: '))
        
        if guess < number_to_guess:
            print('Guess too low !')
        elif guess > number_to_guess:
            print('Guess too high !')
        else:
            print('Congratulations you guessed the number!')
            break
    except ValueError:
        print('Please enter a valid number')
    