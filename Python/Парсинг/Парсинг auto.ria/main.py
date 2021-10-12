import requests
from bs4 import BeautifulSoup as bs
import csv
import os


host = 'https://auto.ria.com'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'accept': '*/*'
}
file_path = 'cars.csv'


def get_html(url, params=None):
    r = requests.get(url, headers=headers, params=params)
    return r


def get_pages_count(html):
    soup = bs(html, 'html.parser')
    pagination = soup.find_all('span', class_='mhide')
    if pagination:
        return int(pagination[-1].get_text())
    else:
        return 1


def get_content(html):
    soup = bs(html, 'html.parser')
    items = soup.find_all('div', class_='proposition')
    cars = []
    for item in items:
        photos = item.find('span', class_='badge badge--live')
        if photos:
            photos = photos.get_text(strip=True)
        else:
            photos = 'Без живих фото'
        temp_items = item.find_all('span', class_='item')
        del temp_items[0]
        characteristics = ''
        for i in range(len(temp_items)):
            characteristics = characteristics + temp_items[i].get_text(strip=True) + ';'
        characteristics = characteristics.replace('•', ' ')
        cars.append({
            'mark': item.find('span', class_='link').get_text(strip=True),
            'link': host + item.find('a', class_='proposition_link').get('href'),
            'price(dol)': item.find('span', class_='green').get_text(strip=True),
            'price(grn)': item.find('span', class_='size16').get_text(strip=True),
            'city': item.find('span', class_='item region').get_text(strip=True),
            'state': item.find('span', class_='badge').get_text(strip=True),
            'characteristics': characteristics,
            'photos': photos,
        })
    return cars


def save_file(items, path):
    with open(path, 'w', newline='') as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerow(['Марка', 'Ссылка', 'Цена в дол', 'Цена в грн',
                         'Город', 'Состояние', 'Характеристики', 'Фото'])
        for item in items:
            writer.writerow([item['mark'], item['link'], item['price(dol)'], item['price(grn)'],
                             item['city'], item['state'], item['characteristics'], item['photos']])


def parse():
    url = input('Введите url: ')
    url = url.strip()

    html = get_html(url)
    if html.status_code == 200:
        pages_count = get_pages_count(html.text)
        cars = []
        for page in range(1, pages_count + 1):
            print(f'Парсинг страницы {page} из {pages_count}...')
            html = get_html(url, params={'page': page})
            cars.extend(get_content(html.text))
            save_file(cars, file_path)
        print(f'Получено {len(cars)} автомобилей')
        os.startfile(file_path)
    else:
        print('Error\n')


parse()
