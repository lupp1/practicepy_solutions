# List Remove Duplicates www.practicepython.org/exercise/2014/05/15/14-list-remove-duplicates.html
# Write a program (function!) that takes a list and returns a new list 
# that contains all the elements of the first list minus all the duplicates.

def no_dupes(a: list) -> list:
    '''Turns list into a set, then returns a list without duplicate'''
    return list(set(a))

if __name__ == '__main__':
    duplicate_list = [1, 1, 2, 2, 5, 13, 13, 12, 7, 3, 5, 8, 0, 8, 'gust', 'gust']
    print(no_dupes(duplicate_list))