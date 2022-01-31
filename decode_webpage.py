# Decode A Web Page www.practicepython.org/exercise/2014/06/06/17-decode-a-web-page.html
# Use the BeautifulSoup and requests Python packages to print out a list of all the article 
# titles on the New York Times homepage.
from bs4 import BeautifulSoup
import requests

def main():
    text = ""
    for i in h3:
        text += i.text
    print(text)

if __name__ == "__main__":
    
    url = "https://www.nytimes.com/"
    req = requests.get(url)
    req_html = req.text
    soup = BeautifulSoup(req_html, 'html.parser')
    h3 = soup.find_all('h3') 
    
    main()
