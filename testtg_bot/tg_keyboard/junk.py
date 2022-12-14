import os
from datetime import datetime

from reportlab.graphics import renderPM
from svglib.svglib import svg2rlg
from requests_tg import weather_picture


def help_picture(day, n):
    if (weather_picture(day)[n])[2:4] == 'c3':
        cut_picture = weather_picture(day)[n].replace((weather_picture(day)[n])[0:2], '')
    else:
        cut_picture = weather_picture(day)[n]
    return cut_picture
def help_weather(cut_picture):
    if os.path.isfile(f'C:/Users/37533/Desktop/testtg_bot/gismeteo-icons/{cut_picture}.png') == False:
        drawing = svg2rlg(f"C:/Users/37533/Desktop/testtg_bot/gismeteo-icons/{cut_picture}.svg")
        renderPM.drawToFile(drawing, f"C:/Users/37533/Desktop/testtg_bot/gismeteo-icons/{cut_picture}.png", fmt="PNG")

def find_day_weather(day_num):
    today_day_num = datetime.isoweekday(datetime.now())
    if day_num == today_day_num:
        day = ''
    if day_num == today_day_num+1:
        day = 'tomorrow'
    if day_num>today_day_num+1:
        days_gand = str(day_num-today_day_num+1)
        day = f"{days_gand}-day"
    if day_num<today_day_num:
        days_gand = 8-abs(day_num-today_day_num)
        day = f"{days_gand}-day"
    return day
def find_day_TV(day_num):
    today_day_num = datetime.isoweekday(datetime.now())
    if day_num >= today_day_num:
        day = day_num - today_day_num
    if day_num < today_day_num:
        day = abs(day_num - today_day_num)
    return day


