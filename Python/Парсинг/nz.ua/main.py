import requests
from bs4 import BeautifulSoup


def get_data():
    url = 'https://nz.ua/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    }
    html = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(html.text, 'lxml')
    csrf = soup.find('body').find('div', class_='site-login').find('input').get('value')
    payload = {
        '_csrf': csrf,
        'LoginForm[login]': login
        'LoginForm[password]': password,
        'LoginForm[rememberMe]': '1',
    }
    html = requests.post('https://nz.ua/', data=payload)
    soup = BeautifulSoup(html.text, 'html.parser')
    with open(f'page.html', 'w', encoding='utf-8') as file:
        file.write(str(soup))


def main():
    get_data()


if __name__ == '__main__':
    main()