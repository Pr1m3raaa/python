from bs4 import BeautifulSoup as bs
import requests
import lxml
from PIL import Image
from urllib.request import urlopen
headers ={
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36 OPR/40.0.2308.81',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'DNT': '1',
    'Accept-Encoding': 'gzip, deflate, lzma, sdch',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.6,en;q=0.4'
}
def shop_picture_dobronom():
    pic_dict_dobronom = []
    URL = 'https://www.dobronom.by/promotions/'
    response = requests.get(URL, headers=headers)
    soup1 = bs(response.text, 'lxml')

    pictures = soup1.find_all('img')
    for i in pictures:
        if i.get('alt') == 'доброном':
            pic_dict_dobronom.append('https://www.dobronom.by'+i.get('src'))
    return pic_dict_dobronom



def shop_picture_evroopt():
    pic_dict_evroopt = []
    URL = 'https://evroopt.by/redprice/vse-tovary/'
    response = requests.get(URL, headers=headers)
    soup1 = bs(response.text, 'lxml')

    pictures = soup1.find_all('img')
    for i in pictures:
        z = i.get('class')
        if type(z) == list:
            if z[0] == 'aligncenter':
                pic_dict_evroopt.append(i.get('src')+'?random=64')
    return pic_dict_evroopt

def shop_picture_santa():
    pic_dict_santa = []
    URL = 'https://www.slivki.by/giper-shop/santa-skidki-minsk?utm_source=search_result&utm_medium=%D1%81%D0%B0%D0%BD%D1%82%D0%B0'
    response = requests.get(URL, headers=headers)
    soup1 = bs(response.text, 'lxml')

    pictures = soup1.find_all('div', class_='sale-lazy-wrap')
    for i in pictures:
        pic = i.find('img')
        pic_dict_santa.append(pic.get('data-original')+'?random=64')
    return pic_dict_santa












