# Max of Three www.practicepython.org/exercise/2016/03/27/28-max-of-three.html
# Implement a function that takes as input three variables, and returns the largest of the three. 
# Do this without using the Python max() function!

"""This works"""

def max_three(a, b, c):
    s = (a, b, c)
    for index in range(len(s)):
        for _ in s:
            if _ > s[index]:
                return print(_)
        if _ > s[index]:
            return print(_)
                 
if __name__ == '__main__':
    max_three(9, 2, 5)
