from bs4 import BeautifulSoup
import requests as r

url = 'https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture'
req = r.get(url)
soup = BeautifulSoup(req.text, 'html.parser')

def getText(elem):
    text = [line.get_text() for line in soup.find_all(elem) if len(line) > 1]
    return text

# print(getText('h2'))
print(soup.get_text())