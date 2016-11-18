#!/usr/bin/env python
# encoding: utf-8


"""
@author: Jackling Gu
@file: wunderground_util.py
@time: 16-11-16 12:12
"""
from bs4 import BeautifulSoup
import operator
import urllib2
import datetime

TARGET_ASTRO = 'Actual Time'
BASE_URL = 'https://www.wunderground.com/history/wmo/58926/{}/{}/{}/DailyHistory.html?req_city={}&req_state=35&req_statename=China&reqdb.zip=00000&reqdb.magic=301&reqdb.wmo=58926&MR=1'

def trans_time(year,month,day,time_str):
    tmp_str ='{}-{}-{} {}'.format(year,month,day,time_str[:-4])
    return str(datetime.datetime.strptime(tmp_str, "%Y-%m-%d %I:%M %p"))

def get_his_data(city,year,month,day):
    url = BASE_URL.format(year,month,day,city)
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    html_doc = response.read()

    max_t,min_t,wind_spd,sunrise,sunset = -1,-1,-1,'',''
    #print html_doc
    soup = BeautifulSoup(html_doc,'lxml')

    tds = soup.find_all('td')
    td_cnt = len(tds)

    for i in range(td_cnt):
        cls_name = tds[i].get('class')
        try:
            if cls_name[0] == 'indent':
                tmp_str = tds[i].string
                if tmp_str == 'Max Temperature':
                    max_t = tds[i+1].find_all('span')[1].string
                elif tmp_str == 'Min Temperature':
                    min_t =  tds[i + 1].find_all('span')[1].string
                elif tmp_str == 'Wind Speed':
                    wind_spd = tds[i + 1].find_all('span')[1].string
                else:
                    pass
        except:
            pass

    astro_tds = soup.find(id='astronomy-mod').find_all('td')
    astro_tds_cnt = len(astro_tds)
    for i in range(astro_tds_cnt):
         if TARGET_ASTRO in astro_tds[i].string:
             sunrise = trans_time(year,month,day,astro_tds[i+1].string)
             sunset = trans_time(year,month,day,astro_tds[i+2].string)
             break
    try:
        condition_url = url+'h&format=1'
        request = urllib2.Request(condition_url)
        response = urllib2.urlopen(request)
        conditions = response.read().split('\n')
        condition_dict = {}
        for row in conditions:
            if 'AM' in row or 'PM' in row:
                tmp_cond = row.split(',')[-3]
                if tmp_cond not in condition_dict:
                    condition_dict[tmp_cond] = 0
                condition_dict[tmp_cond] += 1
        sorted_cond_d = sorted(condition_dict.items(),key=operator.itemgetter(1))
        final_cond = sorted_cond_d[-1][0]
    except:
        final_cond = ''
    return max_t,min_t,wind_spd,sunrise,sunset,final_cond

def get_his_hour_data(city,year,month,day):
    condition_url = BASE_URL.format(year,month,day,city)+'h&format=1'
    request = urllib2.Request(condition_url)
    response = urllib2.urlopen(request)
    conditions = response.read().split('\n')
    res_list = []
    for row in conditions[2:]:
        try:
            data_list = row.split(',')
            if len(data_list)<7:
                continue
            time = trans_time(year,month,day,str(data_list[0])+'1234')
            temp = data_list[1]
            wind_spd = data_list[7]
            wind_spd = 0 if wind_spd.isalpha() else wind_spd
            tmp_cond = data_list[-3]
            res_list.append([time,temp,wind_spd,tmp_cond])
        except:
            pass
    return res_list




if __name__=='__main__':
    print get_his_data('xianyang',2016,3,12)
    print get_his_hour_data('xianyang',2016,3,12)

