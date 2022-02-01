# Write To A File www.practicepython.org/exercise/2014/11/30/21-write-to-a-file.html
# Take the code from the How To Decode A Website exercise (if you didn’t do it or just want to play with some different code, use the code from the solution) 
# and instead of printing the results to a screen, write the results to a txt file. 
# In your code, just make up a name for the file you are saving to.

def write_to_file(file_name):
    text = """
import requests
from bs4 import BeautifulSoup
 
base_url = 'http://www.nytimes.com'
r = requests.get(base_url)
soup = BeautifulSoup(r.text)
 
for story_heading in soup.find_all(class_="story-heading"): 
    if story_heading.a: 
        print(story_heading.a.text.replace("\n", " ").strip())
    else: 
        print(story_heading.contents[0].strip())
"""
    with open(f'{file_name}.txt', 'w') as file:
        file.write(text)

if __name__ == "__main__":
    filename = input('Insert a file_name to write the file to: ')
    write_to_file(filename) 
