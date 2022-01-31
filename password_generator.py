# Password Generator www.practicepython.org/exercise/2014/05/28/16-password-generator.html
# Write a password generator in Python.
# Be creative with how you generate passwords - 
# strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols.
# The passwords should be random, generating a new password every time the user asks for a new password. 
# Include your run-time code in a main method.

import random
from string import ascii_letters, digits, punctuation
from time import sleep
import pyperclip

def main():
    random_char = ascii_letters + digits + punctuation
    characters = [i for i in random_char]
    password = []

    for i in range(20):
        password.append(random.choice(characters))
    return ''.join(password)

if __name__ == "__main__":
    new_password = main()
    pyperclip.copy(new_password)
    print(f'Your new password is {new_password}')
    sleep(5)


i = 0

