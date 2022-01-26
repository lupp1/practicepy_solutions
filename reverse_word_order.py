# Reverse Word Order www.practicepython.org/exercise/2014/05/21/15-reverse-word-order.html
# Write a program (using functions!) that asks the user for a long string containing multiple words.
# Print back to the user the same string, except with the words in backwards order.

def reverse_order(string: str) -> str:
    x = string.split()
    sorted_list = x[::-1]
    return  ' '.join(sorted_list)

if __name__ == '__main__':
    s = input('Enter a sentence to be reversed: ')
    print(s, reverse_order(s), sep='\n')