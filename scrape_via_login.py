import sys
import requests
from lxml import html

USERNAME = "<ENTER YOUR EMAIL>"
PASSWORD = "<ENTER YOUR PASSWORD>"
SCHOOL_ID = "<YOUR STD ID>"

LOGIN_URL = "https://sso.teachable.com/secure/".SCHOOL_ID."/users/sign_in?clean_login=true&reset_purchase_session=1"
URL = sys.argv[1]

def main():
    session_requests = requests.session()

    # Get login csrf token
    result = session_requests.get(LOGIN_URL)
    tree = html.fromstring(result.text)
    authenticity_token = list(set(tree.xpath("//meta[@name='csrf-token']/@content")))[0]
    authenticity_param = list(set(tree.xpath("//meta[@name='csrf-param']/@content")))[0]

    # Create payload
    payload = {
        "user[school_id]": SCHOOL_ID,
        "user[email]": USERNAME, 
        "user[password]": PASSWORD, 
        authenticity_param : authenticity_token
    }

    # Perform login
    result = session_requests.post(LOGIN_URL, data = payload, headers = dict(referer = LOGIN_URL))

    # Scrape url
    result = session_requests.get(URL, headers = dict(referer = URL))
    print(result.content)

if __name__ == '__main__':
    main()
