# Generate random 4 -pin 
# ask for guess
# cow for digit in right place
# bulll for digit in wrong place
# give feedback
# keep count of try numbers
# repeat until they get it right

import random as r

def get_guess():
    guess = input('Enter 4 Integers (or "exit" to quit) --- ')
    if len(guess) != 4: guess = '1234'
    guess = [int(i) for i in [i for i in guess]]
    return guess


def check_guess(answer, guess):
    if guess == 'exit': return 'exit'
    n = 0
    bulls = 0
    cows = 0 
    print('guess:', guess)
    while n < len(answer) or n < len(guess):
        if answer[n]  == guess[n]: cows+=1
        elif answer[n] in guess and answer[n] != guess[n]: bulls +=1
        n += 1
    print('bulls:', bulls, 'cows:', cows)
    return cows

def the_game():
    feedback = 0
    answer = (r.sample(range(10), 4))
    print("answer:", answer)
    while feedback < 4:
        feedback = check_guess(answer, get_guess())
    print('Congrats! you win.')

the_game()

    


