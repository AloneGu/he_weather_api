#!/usr/bin/env python
# encoding: utf-8


"""
@author: Jackling Gu
@file: weather_worker.py
@time: 16-11-14 11:20
"""


import requests
from config import API_KEY
from util import trans_city_name

BASE_URL = 'https://free-api.heweather.com/v5/'



class WeatherWorker(object):

    def __init__(self):
        pass

    def get_history_data(self,start,end,city):
        pass

    def get_basic_data(self,city):
        city_id = trans_city_name(city)
        tmp_url = BASE_URL + 'weather?key={}&city={}'.format(API_KEY,city)
        print tmp_url
        res = requests.get(tmp_url)
        res_dict = eval(res.content)['HeWeather5'][0]
        return res_dict


