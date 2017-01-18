#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 1/18/17 2:14 PM
# @Author  : Jackling 

from config import WEATHERMAP_API_KEY
import requests
BASE_URL = 'http://api.openweathermap.org/data/2.5/forecast?q={},cn&mode=json&APPID={}'

def get_hour_forecast(city):
    url = BASE_URL.format(city,WEATHERMAP_API_KEY)
    req = requests.post(url)
    res = req.json()
    res_list = []
    for row in res['list']:
        time = row['dt_txt']
        temp = row['main']['temp']
        wind_spd = row['wind']['speed']
        desc = row['weather'][0]['description']
        res_list.append([time,temp,wind_spd,desc])
    return res_list

if __name__=='__main__':
    print get_hour_forecast(city='xianyang')

