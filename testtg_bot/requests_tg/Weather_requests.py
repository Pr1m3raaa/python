from bs4 import BeautifulSoup as bs
import requests
import lxml




headers ={
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36 OPR/40.0.2308.81',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'DNT': '1',
    'Accept-Encoding': 'gzip, deflate, lzma, sdch',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.6,en;q=0.4'}


def weather_time(day):
    time = []
    time1 = []
    URL = f'https://www.gismeteo.by/weather-ushachi-11023/{day}'
    response = requests.get(URL, headers=headers)
    soup1 = bs(response.text, 'lxml')

    times = soup1.find_all('div', class_='row-item')
    for i in times:
        if type(i.get('title'))== str:
            time.append((i.find('span')).text)
    for q in time:
        time1.append(f'{q[:len(q)-2]}-{q[len(q)-2:]}')
    return time1

def weather_gradus(day):
    gradus = []
    URL = f'https://www.gismeteo.by/weather-ushachi-11023/{day}'
    response = requests.get(URL, headers=headers)
    soup1 = bs(response.text, 'lxml')

    graduses = soup1.find_all('div', class_='value')
    for i in graduses:
        if i.find('span', class_='unit unit_temperature_c') != None:
            gradus.append(i.find('span', class_='unit unit_temperature_c').text)
    return gradus[4:] if day == '' else gradus[6:]

def weather_picture(day):
    pictures = []
    URL = f'https://www.gismeteo.by/weather-ushachi-11023/{day}'
    response = requests.get(URL, headers=headers)
    soup1 = bs(response.text, 'lxml')

    all_pictures = soup1.find_all('use')
    for i in all_pictures:
        get_href = i.get('xlink:href')
        if get_href[1:2] == 'd' or get_href[1:2] == 'n':
            pictures.append(get_href.replace('#',''))
    return pictures[4:]


def combined_text(day):
    n = 0
    comb_dict = []
    for i in weather_time(day):
        comb_dict.append(f'{weather_time(day)[n]} - {weather_gradus(day)[n]}')
        n+=1
    return comb_dict







