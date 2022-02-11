# Birthday Json www.practicepython.org/exercise/2017/02/06/34-birthday-json.html
# In the previous exercise we created a dictionary of famous scientists’ birthdays. 
# In this exercise, modify your program from Part 1 to load the birthday dictionary from a JSON file on disk, 
# rather than having the dictionary defined in the program.

import json


birthday = {}

with open("birthday.json", "r") as jfile:
    birthday = json.load(jfile)


def add_birthday():
    _name = str(input("Tell a name to add to the birthdays list\n")).title()
    input_date = str(input("Tell me their birthday (format MM/DD/YY)\n"))
    birthday[_name] = input_date
    with open("birthday.json", "w") as jfile:
        json.dump(birthday, jfile)
    print("{0} was added to my birthdays list.".format(_name))    

def search_birthday():
    search = str(input("Who's birthday do you want to search for?\n")).title()
    if search in birthday.keys():
        return print("{0} was born in {1}.".format(search, birthday[search]))
    else:
        print("This person isn't in my birthdays list.")

def main():
    op = ["1 - Search for birthdays", "2 - Add a birthday", "3 - Quit"]
    while True:
        for _ in op:
            print(_)
        _input = str(input("Enter an option:"))
        if _input == "1":
            return search_birthday()
        elif _input== "2":
            return add_birthday()
        elif _input == "3":
            quit()

if __name__ == "__main__":
    main()

