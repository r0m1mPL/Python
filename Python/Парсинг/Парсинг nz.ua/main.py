import requests
from bs4 import BeautifulSoup

session = requests.Session()

url = 'https://nz.ua/menu/'

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,'
    'application/signed-exchange;v=b3;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/91.0.4472.124 Safari/537.36',
}


def get_csrf(url, headers):
    response = session.get(url=url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    csrf = soup.find('div', class_='site-login').find('input').get('value')
    return csrf



csrf = get_csrf(url, headers)
print(csrf)
data = {
    '_csrf': 'csrf',
    'LoginForm[login]': login,
    'LoginForm[password]': password,
    'LoginForm[rememberMe]': '1',
}

response = session.post(url=url, data=data, headers=headers)
open('response.html', 'w').write(response.text)
print(response)
response = session.post(url=url, data=data, headers=headers)
print(response.text)
# url_menu = 'https://nz.ua/id6723262'
#
# response_menu = session.get(url=url_menu, headers=headers)
# open('response_menu.html', 'w').write(response.text)
# print(response_menu)
# print()