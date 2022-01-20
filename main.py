import requests, random
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

ua = UserAgent()
headers = {
    'authority': 'prnt.sc',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Yandex";v="22"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'upgrade-insecure-requests': '1',
    'user-agent': f'{ua}',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'none',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'accept-language': 'ru,en;q=0.9,zh;q=0.8',
}

symbols = list('abcdefghijklmnopqrstuvwxyz0123456789')


def find_img():
    rand = ''.join(random.sample(symbols, 6))
    url = f'https://prnt.sc/{rand}'
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    link_img = soup.img['src']
    return link_img
# img_response = requests.get(link_img)
# img_bin = img_response.content
# img = open(f'{rand}' + '.jpg', 'wb')
# img.write(img_bin)
# img.close()
