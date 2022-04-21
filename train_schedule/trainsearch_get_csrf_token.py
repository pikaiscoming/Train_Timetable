# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 11:22:25 2021

@author: 皮皮卡卡
"""
import requests
from bs4 import BeautifulSoup as BS
import pprint
url = 'https://tip.railway.gov.tw//tra-tip-web/tip/tip001/tip112/querybytime'


data = { '_csrf':'',
        'startStation': "1000-臺北",
        'endStation': "1100-中壢",
        'transfer': "ONE",
        'rideDate': "2021/12/09",
        'startOrEndTime': "true",
        'startTime': "00:00",
        'endTime': "23:59",
        'trainTypeList': "ALL",
        '_isQryEarlyBirdTrn': "on",
        'query': "查詢"
        }
session = requests.Session()

s = session.get(url)
bs = BS(s.text, 'html.parser')

token = bs.find('form', {'id':"queryForm"}).input
print(token['value'])

data['_csrf']=token['value']

r = session.post(url, data=data)
bs = BS(r.text, 'html.parser')
r = bs.find('form', {'id':"queryForm"}).input
test = bs.find('div', {'id':'content'})
#print(r['value'])
#pprint.pprint(test)
print(data)



