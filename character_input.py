# Character input www.practicepython.org/exercise/2014/01/29/01-character-input.html[
# Create a program that asks the user to enter their name and their age. 
# Print out a message addressed to them that tells them the year that they will turn 100 years old.

import datetime as dt

date = dt.date.today()
year = date.year

try:
    name = input('Insert your name: ')
    age = int(input('Insert your age: '))
    while age < 100:
        age += 1
        year += 1
        if age == 100:
            print(f'Hello {name}, the year you\'ll turn 100 years old is {year}.')

except ValueError as err:
    print(f'{err}: Insert an integer')
    quit()



