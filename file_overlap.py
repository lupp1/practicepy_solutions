# File overlap www.practicepython.org/exercise/2014/12/14/23-file-overlap.html
# Given two .txt files that have lists of numbers in them, find the numbers that are overlapping. 
# One .txt file has a list of all prime numbers under 1000, 
# and the other .txt file has a list of happy numbers up to 1000.
# (If you forgot, prime numbers are numbers that can’t be divided by any other number. 
# And yes, happy numbers are a real thing in mathematics - you can look it up on Wikipedia. 
# The explanation is easier with an example, which I will describe below.)

def file_overlap() -> list:

    with open('primenumbers.txt', 'r') as prime_file:
        prime_list = prime_file.readlines()
        x = '\n'.join(prime_list)
        prime_list = x.split()

    with open('happynumbers.txt', 'r') as happy_file:
        happy_list = happy_file.readlines()
        y = '\n'.join(happy_list)
        happy_list = y.split()
    
    overlapping = [_ for _ in prime_list if _ in happy_list]

    return overlapping

if __name__ == '__main__':
    print(f'This is the list of all numbers overlapping {file_overlap()}')