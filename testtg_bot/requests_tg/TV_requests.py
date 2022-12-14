from datetime import datetime
from bs4 import BeautifulSoup as bs
import requests
import lxml
ID = {
'Belarus1_id' : '140',
'Belarus2_id' : '86',
'ONT_id' : '89',
'STV_id' : '137',
'NTV_id' : '137',
'RTR_id' : '139',
'Belarus5_id' : '88',
'MIR_id' : '85',
'Eurosport_id' : '119',
'Eurosport2_id': '75'}

today_year = str(datetime.now().year)
today_month = str(datetime.now().month)
today_day = (datetime.now().day)


def any_programm(num_id, day):
    URL = f'https://tv.belta.by/program-ru/channel/{num_id}/dayForDisplay/{today_year}-{today_month}-{str(today_day+day)}/part/today/'
    response = requests.get(URL)
    soup1 = bs(response.text, 'lxml')  # html.parser альтернатива

    program_list = []
    chanel_past = soup1.find_all('div', class_="tv_chanel_list_proshlo")
    for i in chanel_past:
        time = i.find('div', class_="tv_chanel_date").text.replace('\n', '')
        show_name_past = list(i.find('div', class_='tv_chanel_title'))
        title_past = str(show_name_past[0]).strip()
        program_list.append(f'{time} {title_past}')

    chanel_now = soup1.find('div', class_='tv_chanel_list_now')
    try:
        time = chanel_now.find('div', class_='tv_chanel_date').text.replace('\n', '')
        show_name_now = list(chanel_now.find('div', class_='tv_chanel_title'))
        title_now = str(show_name_now[0]).strip()
        program_list.append(f'{time} {title_now}')
    except Exception as e:
        print(e)

    chanel_future = soup1.find_all('div', class_='tv_chanel_list')
    for x in chanel_future:
        time = x.find('div', class_="tv_chanel_date").text.replace('\n', '')
        show_name2 = list(x.find('div', class_='tv_chanel_title'))
        title_future = str(show_name2[0]).strip()
        program_list.append(f'{time} {title_future}')
    return program_list
def final_list(num, day):
    final_list1 = '\n'.join(any_programm(num, day))
    return final_list1



