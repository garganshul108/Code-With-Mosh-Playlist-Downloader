import sys
import requests
from lxml import html
from bs4 import BeautifulSoup

USERNAME = "sci.agarg@gmail.com"
PASSWORD = "asdfghjkl11111"

LOGIN_URL = "https://sso.teachable.com/secure/146684/users/sign_in?clean_login=true&reset_purchase_session=1"

f = open("contents.url", "r")
# print(f.readline())
def main():
    session_requests = requests.session()

    # Get login csrf token
    result = session_requests.get(LOGIN_URL)
    tree = html.fromstring(result.text)
    authenticity_token = list(set(tree.xpath("//meta[@name='csrf-token']/@content")))[0]
    authenticity_param = list(set(tree.xpath("//meta[@name='csrf-param']/@content")))[0]
    # print(authenticity_token)

    # Create payload
    payload = {
        "user[school_id]": "146684",
        "user[email]": USERNAME, 
        "user[password]": PASSWORD, 
        authenticity_param : authenticity_token
    }

    # Perform login
    result = session_requests.post(LOGIN_URL, data = payload, headers = dict(referer = LOGIN_URL))

    # Scrape url
    c = 0
    inp = f.readline()
    while(inp is not "END"):
        if(c%2 == 0):
            print(inp.split('\n')[0])
        else:
            URL = inp.split('\n')[0]
            result = session_requests.get(URL, headers = dict(referer = URL))
            soup = BeautifulSoup(result.content, 'lxml')
            link = soup.find_all('a', class_='download')
            if(len(link) >= 1):
                href = link[0]['href']
                print(href)

        c+=1
        inp = f.readline()
    # print(tree)

if __name__ == '__main__':
    main()
