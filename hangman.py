# In this exercise, we will finish building Hangman. 
# In the game of Hangman, the player only has 6 incorrect guesses (head, body, 2 legs, and 2 arms) before they lose the game.
# In Part 1, we loaded a random word list and picked a word from it. 
# In Part 2, we wrote the logic for guessing the letter and displaying that information to the user. 
# In this exercise, we have to put it all together and add logic for handling guesses.

import random
from pick_word import pick_a_word

def main() -> str:
    word = pick_a_word()
    i = len(word)
    s = [' _ ' * i]
    tiles = s[0].split()
    print(word)
    guesses = []

    # TODO: When the player wins or loses, let them start a new game.
    while True:
        user_guess = input('Guess your letter: ').upper()   
        for idx in range(len(word)):
            if word[idx] == user_guess:
                tiles[idx] = user_guess
            
        guesses.append(user_guess)
        print(f"You still have {abs(len(guesses) - 6)} guesses.")

        if len(guesses) >= 6:
            print("You don't have anymore guesses available!")
            break

        if word == user_guess or ''.join(tiles):
            print('Congratulations, you got it right!!') 
            break

        if user_guess not in word:
            print('Incorrect!')
            continue

        print(' '.join(tiles))

if __name__ == "__main__":
    main()
             