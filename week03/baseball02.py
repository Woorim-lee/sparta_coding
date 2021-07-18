import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://sports.news.naver.com/kbaseball/record/index.nhn?category=kbo', headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

kbos = soup.select('#regularTeamRecordList_table > tr')

for kbo in kbos:
    rank = kbo.select_one('th > strong').text
    name = kbo.select_one('td.tm > div > span').text
    wining = kbo.select_one('td > strong').text

    if wining > '0.5':
        print(rank, name, wining)