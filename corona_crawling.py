from bs4 import BeautifulSoup
#import telegram
import requests
import time
import os
from datetime import datetime

hdr = {'Accept-Language': 'ko_KR,en;q=0.8', 'User-Agent': (
    'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Mobile Safari/537.36')}
latestVal = ''


def coronaMap():
    global latestVal
    res = requests.get('https://coronamap.site/', headers=hdr)
    soup = BeautifulSoup(res.content, 'html.parser')
    data1 = soup.findAll('div', 'content')
    data2 = soup.findAll('div', 'content1 clear')

    data1_list = []
    data2_list = []
    for item in data1:
        data1_list.append(item.get_text().replace('\n', '').replace(' ', ''))
    for item in data2:
        data2_list.append(item.get_text().replace('\n', '').replace(' ', ''))

    print(data1_list, data2_list)
    confirmedPatient = data1_list[0]

    if latestVal == confirmedPatient and datetime.now().hour() != 0:
        return
    latestVal = confirmedPatient
    x = data2_list[0].find('사망')
    curedPatient = data2_list[0][2:x]
    diedPatient = data2_list[0][x + 2:]

    message = '<🚨코로나 알림🚨>\n'
    message += f'√ 확진 %s명\n√ 완치 %s명\n√ 사망 %s명\n' % (confirmedPatient,curedPatient, diedPatient)
    message += f'\n[관련 뉴스](https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%EC%BD%94%EB%A1%9C%EB%82%98)'
    print(message)
    return

coronaMap()