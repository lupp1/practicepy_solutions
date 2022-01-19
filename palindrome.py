# Ask the user for a string and print out whether this string is a palindrome or not. 
# (A palindrome is a string that reads the same forwards and backwards.)

string = input('Insert a word: ')

def main():
    return 'Palindrome' if string[::-1] == string[::1] else 'Not a palindrome.'
print(main())