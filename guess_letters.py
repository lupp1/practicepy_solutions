# Let’s continue building Hangman. 
# In the game of Hangman, a clue word is given by the program that the player has to guess, letter by letter. 
# The player guesses one letter at a time until the entire word has been guessed. 
# (In the actual game, the player can only guess 6 letters incorrectly before losing).
# Let’s say the word the player has to guess is “EVAPORATE”. 
# For this exercise, write the logic that asks a player to guess a letter and displays letters in the clue word that were guessed correctly. 
# For now, let the player guess an infinite number of times until they get the entire word.

import random
from pick_word import pick_a_word


def main() -> str:
    word = pick_a_word()
    i = len(word)
    s = [' _ ' * i]
    tile = s[0].split()
    print(word)
    guesses = []

    while True:
        user_guess = input('Guess your letter: ').upper()   
        for idx in range(len(word)):
            if word[idx] == user_guess:
                tile[idx] = user_guess

        if user_guess not in word:
            print('Incorrect!')
            continue
        print(' '.join(tile))

if __name__ == "__main__":
    main()
                    
                 