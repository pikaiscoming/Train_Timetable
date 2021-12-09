# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 21:23:10 2021

@author: 皮皮卡卡
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup as BS
import requests
import datetime
import pprint
import re

dt = datetime.datetime.now()
day = dt.strftime('%Y/%m/%d')
Min = int(dt.strftime('%M'))
hour = int(dt.strftime('%H'))
if Min >= 30:
    hour +=1
    Min = '00'
else:
    Min = '00'
time = str(hour)+':'+Min    
end = str(hour+1)+':'+Min
data = {
        '_csrf': '1275647f-8532-4d14-9fb0-bcb84bf61f4c',
        'startStation': "1000-臺北",
        'endStation': "1100-中壢",
        'transfer': "ONE",
        'rideDate': "2021/12/09",
        'startOrEndTime': "true",
        'startTime': "",
        'endTime': "",
        'trainTypeList': "ALL",
        '_isQryEarlyBirdTrn': "on",
        'query': "查詢"
        }
data['rideDate'] = day
data['startTime'] = time
data['endTime'] = end
#print(data)

'''wab crawler'''
url = 'https://tip.railway.gov.tw//tra-tip-web/tip/tip001/tip112/querybytime'
session = requests.Session()

s = session.get(url)
bs = BS(s.text, 'html.parser')

token = bs.find('form', {'id':"queryForm"}).input
#print(token['value'])

data['_csrf']=token['value']

r = session.post(url, data=data)
bs = BS(r.text, 'html.parser')

trains= bs.find('div', {'class':"search-trip"}).find_all('tr', {'class':"trip-column"})

spendtime = []
for train in trains:
    result = train.find_all('td', text=re.compile('\d{2}.*'))
    departure_time = result[0].get_text()
    arrival_time =  result[1].get_text()
    tarvel_time = result[2].get_text()
    print('出發時間: ' + departure_time,
          '抵達時間: ' + arrival_time,
          '行駛時間: ' + tarvel_time,
          sep=' ', end='\n')

    #can get arrive, departure and interval time.

    