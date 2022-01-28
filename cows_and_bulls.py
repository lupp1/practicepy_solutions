# Create a program that will play the “cows and bulls” game with the user. The game works like this:
# Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. 
# For every digit that the user guessed correctly in the correct place, they have a “cow”. 
# For every digit the user guessed correctly in the wrong place is a “bull.” 
# Every time the user makes a guess, tell them how many “cows” and “bulls” they have.
# Once the user guesses the correct number, the game is over. 
# Keep track of the number of guesses the user makes throughout teh game and tell the user at the end.

from random import randint


def usr_input():
        return str(input('Guess a four digit number (exit to leave): '))

def main():
    cows = []
    bulls = []
    guesses = 0
    while True:
        guesses += 1
        guess = usr_input()
        if len(guess) == 4:
            for i in range(0, 4):
                if guess[i] in four_digits and guess[i] is four_digits[i]:
                    cows.append(1)
            
                if guess[i] in four_digits and guess[i] is not four_digits[i]:
                    bulls.append(1)
                
                if guess == four_digits:
                    print('You guessed correctly!')
                    break

            print(f'You made {guesses} guesses', f'You have {sum(cows)} cows and {sum(bulls)} bulls', sep='\n')

        else:
            print('Insert a four digit number.')
            continue
        
        if guess == 'exit':
            quit()

if __name__ == '__main__':
    four_digits = str(randint(1, 9)) + str(randint(0, 9)) + str(randint(0, 9)) + str(randint(0, 9))
    main()
        
