# Birthday Months www.practicepython.org/exercise/2017/02/28/35-birthday-months.html 
# In the previous exercise we saved information about famous scientists’ names and birthdays to disk. 
# In this exercise, load that JSON file from disk, extract the months of all the birthdays,
# and count how many scientists have a birthday in each month.

from collections import Counter
import json

def main() -> dict:
    birth_dict = {}
    appears = []
    with open("birthday.json", "r") as jfile:
        birth_dict = json.load(jfile)
    for key, value in birth_dict.items():
        for month, number in months.items():
            if value.startswith(number):
                appears.append(month)
    c = Counter(appears)

    return dict(c)


months = {
            "January": "01",
            "February": "02",
            "March": "03",
            "April": "04",
            "May": "05",
            "June": "06",
            "July": "07",
            "August": "08",
            "September": "09",
            "October": "10",
            "November": "11",
            "December": "12"
            }
            
main()