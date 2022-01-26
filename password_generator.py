# Password Generator www.practicepython.org/exercise/2014/05/28/16-password-generator.html
# Write a password generator in Python.
# Be creative with how you generate passwords - 
# strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols.
# The passwords should be random, generating a new password every time the user asks for a new password. 
# Include your run-time code in a main method.

import random
from string import ascii_letters, digits, punctuation

def main():
    random_char = ascii_letters + digits + punctuation
    characters = [i for i in random_char]
    password = []

    for i in range(20):
        password.append(random.choice(characters))
    
    return ''.join(password)

if __name__ == "__main__":
    print(f'Your new password is {main()}')