import random as rd

# make number
# give feedback
# congrats opprotunity to play again?
# exit method
num = rd.randint(1,9)
total = []
counter = 0
while True: 
    guess = input('Guess a number 1-9 --- ')
    try: 
        guess = int(guess)
    except:
        print('Please, guess a number')
        break
    total.append(guess)
    counter += 1
    if guess > num: print(guess, 'is too big! Try again.')
    elif guess < num: print(guess, 'is too small! Try again.')
    elif guess == num: 
        print('You got it right!', guess, '=', num)
        gameOverMan = input('Play again? ["yes" if yes] --- ')
        print(gameOverMan)
        if gameOverMan == 'yes':
            num = rd.randint(1,9)
            total = []
            counter = 0 
            continue
        else:
            print('Thanks for playing!')
            print('# of Guesses:', counter, '\nYour Guesses:', total) 
            break
    print('# of Guesses:', counter, '\nYour Guesses:', total)