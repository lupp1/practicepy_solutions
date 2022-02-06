# Read From File www.practicepython.org/exercise/2014/12/06/22-read-from-file.html
# Given a .txt file that has a list of a bunch of names, count how many of each name there are in the file, and print out the results to the screen. 
# I have a .txt file for you, if you want to use it!
import re
from collections import Counter

def read_from_file():
    a = []
    with open('Training_01.txt', 'r') as file:
        pattern = re.compile(r'^.*/(\w+)/(\w+)/(\w+).(\w+)$')
        for i in file.readlines():
            mo = pattern.search(i)
            a.append(mo.group(2)) 

    for k, v in Counter(a).items():
        print(f'Category {k} appeared {v} times.')
        
if __name__ == '__main__':
    read_from_file()