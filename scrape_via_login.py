import sys
import requests
from lxml import html

USERNAME = "sci.agarg@gmail.com"
PASSWORD = "asdfghjkl11111"

LOGIN_URL = "https://sso.teachable.com/secure/146684/users/sign_in?clean_login=true&reset_purchase_session=1"
URL = sys.argv[1]

def main():
    session_requests = requests.session()

    # Get login csrf token
    result = session_requests.get(LOGIN_URL)
    tree = html.fromstring(result.text)
    authenticity_token = list(set(tree.xpath("//meta[@name='csrf-token']/@content")))[0]
    # print(authenticity_token)

    # Create payload
    payload = {
        "user[school_id]": "146684",
        "user[email]": USERNAME, 
        "user[password]": PASSWORD, 
        "csrf-token": authenticity_token
    }

    # Perform login
    result = session_requests.post(LOGIN_URL, data = payload, headers = dict(referer = LOGIN_URL))

    # Scrape url
    result = session_requests.get(URL, headers = dict(referer = URL))
    tree = html.fromstring(result.content)
    # bucket_names = tree.xpath("//div[@class='repo-list--repo']/a/text()")
    print(result.content)
    # print(tree)

if __name__ == '__main__':
    main()
