# Generate a random number between 1 and 9 (including 1 and 9). 
# Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. 
# (Hint: remember to use the user input lessons from the very first exercise)

from random import randint

def guess():
    x = randint(1, 9)
    guesses = []

    while True:
        print('Type exit to leave.')
        usr_input = input('\nInsert a number between 1 and 9: ')
        guesses.append(usr_input)

        if str(usr_input) == 'exit':
            break

        usr_input = int(usr_input)

        if usr_input > x:
            print('Too high.')
            continue
        
        elif usr_input < x:
            print('Too low.')
            continue
        
        else:
            print('Exactly right.')
            print(f"Congratulations. You've taken {len(guesses)} guesses and they are \n{guesses}")
            continue
                
guess()