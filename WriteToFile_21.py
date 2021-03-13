import requests as req
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com/'
headers = {'Accept-Encoding': 'identity'}
r = req.get(url, headers=headers)
r_html = r.text

soup = BeautifulSoup(r_html, features='html.parser')
headlines = [line.get_text() for line in soup.find_all('h2')]

with open('headlines.txt', 'w') as openFile:
    [openFile.write(line + '\n') for line in headlines]

