#!/usr/bin/env python
# encoding: utf-8


"""
@author: Jackling Gu
@file: demo.py
@time: 16-11-14 11:41
"""

from weather_worker import WeatherWorker

if __name__=='__main__':
    t = WeatherWorker()
    print t.get_basic_data('guangzhou')