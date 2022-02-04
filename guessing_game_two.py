# Guessing Game Two www.practicepython.org/exercise/2015/11/01/25-guessing-game-two.html
# In a previous exercise, we’ve written a program that “knows” a number and asks a user to guess it.
# This time, we’re going to do exactly the opposite. 
# You, the user, will have in your head a number between 0 and 100. 
# The program will guess a number, and you, the user, will say whether it is too high, too low, or your number.
# At the end of this exchange, your program should print out how many guesses it took to get your number.
# As the writer of this program, you will have to choose how your program will strategically guess. 
# A naive strategy can be to simply start the guessing at 1, and keep going (2, 3, 4, etc.) until you hit the number. 
# But that’s not an optimal guessing strategy. An alternate strategy might be to guess 50 
# (right in the middle of the range), and then increase / decrease by 1 as needed. 
# After you’ve written the program, try to find the optimal strategy! 
# (We’ll talk about what is the optimal one next week with the solution.)

"""FYI: This code is probably wrongly coded, doesn't use binary search and is not that interactive."""

from random import randint
from time import sleep

def random_number() -> int:
    return randint(0, 50)

def guesses(r):
    g = []
    while True:
        g.append(r)
        print(f'Is your number {r}? (type too low, too high or exact for answer)')
        usr_answer = input().lower()
        if usr_answer == 'too low':
             r += randint(1, 4)
             continue
        elif usr_answer == 'too high':
             r -= randint(1, 4)
             continue
        elif usr_answer == 'exact':
            print('Nice! I got it. \n' \
                f'It only took me {len(g)} guesses!')
            break
                   

if __name__ == '__main__':
    print('Guess a number in your head between 0 and 50!')
    sleep(2)
    num = random_number()
    guesses(num)
