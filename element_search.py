# Element Search www.practicepython.org/exercise/2014/11/11/20-element-search.html
# Write a function that takes an ordered list of numbers 
# (a list where the elements are in order from smallest to largest) and another number. The function 
# decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean.

def search(ordered: list, num: int) -> str:
    return print(f'Is {num} in list?', num in ordered)

if __name__ == '__main__':
    ordered_list = sorted([9, 10, 3, 2, 1, 5, 7, 25, 17, 15, 6, 11])
    number = int(input('Insert a number: '))
    search(ordered_list, number)
