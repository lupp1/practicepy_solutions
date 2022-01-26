# List Ends www.practicepython.org/exercise/2014/04/25/12-list-ends.html
# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) 
# and makes a new list of only the first and last elements of the given list.

def list_ends(a: list):
    try:
        return [a[0], a[-1]]
    except IndexError:
        return 'Index error, can\'t parse list with index < 1.'

print(list_ends([1]))