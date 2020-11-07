#/usr/local/bin/python3

import argparse
import requests
from lxml import html

USERNAME = "__Mediant__"
PASSWORD = "g]P7R|meuwCi8@A%9Yav|w82{~H=9d2D+X$DjP&;"

LOGIN_URL = "https://fetlife.com/users/sign_in"
URL = "https://fetlife.com/groups/7331/group_memberships"

def main():
    session_requests = requests.session()

    # Get login csrf token
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    result = session_requests.get(LOGIN_URL, headers=headers)
    tree = html.fromstring(result.text)
    authenticity_token = list(set(tree.xpath("//input[@name='authenticity_token']/@value")))[0]

    # Create payload
    payload = {
        "username": USERNAME, 
        "password": PASSWORD,
        "authenticity_token": authenticity_token
    }

    # Perform login
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    result = session_requests.post(LOGIN_URL, data = payload, headers = headers)

    print(result.__dict__)

    # Scrape url
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36', 'referer' : URL}
    result = session_requests.get(URL, headers=headers)
    tree = html.fromstring(result.content)
    #bucket_names = tree.xpath("//div[@class='repo-list--repo']/a/text()")

    print(tree)
'''
def parse_args():
    parser = argparse.argumentParser()
    parser.addArgument('', '', help='')
    return parser.parse_args()
'''

if __name__ == '__main__':
    main()
