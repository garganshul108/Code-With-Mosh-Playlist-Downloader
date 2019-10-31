from bs4 import BeautifulSoup
import requests
import re

import sys

local_scrape_page = sys.argv[1]

with open(local_scrape_page) as file:
    soup = BeautifulSoup(file, 'lxml')

for link in soup.find_all('a', class_='download'):
    href = link['href']
    print(href)
    
    