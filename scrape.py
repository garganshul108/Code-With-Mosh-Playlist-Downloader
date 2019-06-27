from bs4 import BeautifulSoup
import requests
import re


with open('mosh.html') as file:
    soup = BeautifulSoup(file, 'lxml')


# print(soup.prettify())

# match = soup.title.text
# print(match)

output = open('output.txt','w')

pattern = re.compile(r'\s+')


counter = 0
for match in soup.find_all('a', class_='item'):

    name = match.find('span', class_='lecture-name').text.strip()
    name = re.sub(pattern, '', name)
    name = name.split('-')
    if name[0]=='1' :
        counter += 1
    name[0] = name[0]+'-'
    newname = str(counter) + '.'
    for s in name:
        newname = newname + s        
    href = match['href']
    href = 'https://codewithmosh.com'+href
    
    source = requests.get(href).text
    
    minsoup = BeautifulSoup(source, 'lxml')
    print(minsoup.title.text)
    print(minsoup)
    # hhref = minsoup.find('div', class_='lecture-attachment')

    # hhref = minsoup.find('div', class_='video-options')
    hhref = minsoup.find_all('a', class_='download')
  
    for kk in hhref:
        kk = kk['href']
        print(kk)
    print(newname)
    