from bs4 import BeautifulSoup
from selenium import webdriver
import time
import dload

driver = webdriver.Chrome('chromedriver')
driver.get("https://search.daum.net/search?w=img&q=%EB%B0%95%EC%84%9C%EC%A4%80") # 여기에 URL을 넣어주세요
time.sleep(5)

req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')
thumbnails = soup.select('#imgList > div > a > img')

i = 1
for thumbnail in thumbnails:
    img = thumbnail['src']
    dload.save(img, f'imgs_homework/{i}.jpg')
    i += 1

driver.quit() # 끝나면 닫아주기