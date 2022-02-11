# Birthday dictionaries www.practicepython.org/exercise/2017/01/24/33-birthday-dictionaries.html
# For this exercise, we will keep track of when our friend’s birthdays are, 
# and be able to find that information based on their name. 
# Create a dictionary (in your file) of names and birthdays. 
# When you run your program it should ask the user to enter a name, and return the birthday of that person back to them. 

def main():

    birth_dict = {"Albert Einstein": "03/14/1879", 
        "Ada Lovelace": "27/11/1852", 
        "Benjamin Franklin": "01/17/1706"}

    print("\nWelcome to the birthday dictionary. We know the birthdays of: ")
    
    try: 
        for keys in birth_dict.keys():
            print(keys)
        user_input = input("\nWho's birthday do you want to look up? \n").title()
        print(f"{user_input}'s birthday is {birth_dict[user_input]}.")

    except KeyError as err:
        print(f"{err} we don't have this person's name available in our database.")
        main()

if __name__ == "__main__":
    main()