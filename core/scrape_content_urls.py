from bs4 import BeautifulSoup
import requests
import re

import sys

local_scrape_page = sys.argv[1]

with open(local_scrape_page) as file:
    soup = BeautifulSoup(file, 'lxml')

pattern = re.compile(r'\s+')

counter = 1
for match in soup.find_all('a', class_='item'):

    name = match.find('span', class_='lecture-name').text.strip()
    name = re.sub(pattern, '', name)
    name = str(counter) + '.' + name
    counter+=1
    print(name)

    href = match['href']
    href = 'https://codewithmosh.com'+href
    print(href)
    
    