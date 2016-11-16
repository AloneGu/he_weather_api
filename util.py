#!/usr/bin/env python
# encoding: utf-8


"""
@author: Jackling Gu
@file: util.py.py
@time: 16-11-14 12:07
"""

china_city_list = eval(open('china_city_list.json').read())


def trans_city_name(city_name):
    for tmp_d in china_city_list:
        try:
            if tmp_d['cityEn'] == city_name or tmp_d['cityZh'] == city_name:
                return tmp_d['id']
        except:
            return None


if __name__ == '__main__':
    print trans_city_name('guangzhou')
    print trans_city_name('咸阳')
