# List overlap www.practicepython.org/exercise/2014/03/05/05-list-overlap.html
# Take two lists, say for example these two:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are common between the lists 
# (without duplicates). 
# Extras:
# 1 . Randomly generate two lists to test this

from random import randint, shuffle 

def overlap() -> list:

    overlaps = list(set(s + m))
    shuffle(overlaps)

    return overlaps
    
if __name__ == "__main__":
    m = [x for x in range(randint(0, 100))]
    s = [y for y in range(randint(0, 100))]
    overlap()