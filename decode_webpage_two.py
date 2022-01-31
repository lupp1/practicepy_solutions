# Using the requests and BeautifulSoup Python libraries, 
# print to the screen the full text of the article on this website: 
# http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture.
# The article is long, so it is split up between 4 pages.
# Your task is to print out the text to the screen so that you can read the full 
# article without having to click any buttons.

import requests
from bs4 import BeautifulSoup

def get_text():

    url = 'https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture'
    req = requests.get(url)
    soup = BeautifulSoup(req.text, features='lxml')
    t = list(soup.find_all('div', attrs= 'body__inner-container'))

    with open('decode_webpage_two.txt', 'w') as file:
        for i in t:
            file.write(i.text)

if __name__ == '__main__':
    get_text()