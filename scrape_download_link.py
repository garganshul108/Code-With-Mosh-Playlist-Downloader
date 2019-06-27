from bs4 import BeautifulSoup
import requests
import re

import sys

local_scrape_page = sys.argv[1]

with open(local_scrape_page) as file:
    soup = BeautifulSoup(file, 'lxml')

link = soup.find('a', class_='download')
href = link['href']
print(href)
    
    