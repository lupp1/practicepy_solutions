# Odd or even www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html
# Ask the user for a number. 
# Depending on whether the number is even or odd, print out an appropriate message to the user.

num = int(input('Insert a number: '))

if num % 2 == 1:
    print(f'{num} is odd.')
elif num % 2 == 0:
    print(f'{num} is even.')