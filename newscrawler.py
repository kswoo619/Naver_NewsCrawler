from selenium import webdriver
from bs4 import BeautifulSoup as bs
import time

def infinite_loop():
    #스크롤 내리기
    last_page_height = driver.execute_script("return document.documentElement.scrollHeight")

    while True:
        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
        time.sleep(1.0)
        new_page_height = driver.execute_script("return document.documentElement.scrollHeight")
        if new_page_height == last_page_height:
            time.sleep(1.0)
            if new_page_height == driver.execute_script("return document.documentElement.scrollHeight"):
                break
        else:
            last_page_height = new_page_height

driver = webdriver.Chrome()
url = 'https://search.naver.com/search.naver?ssc=tab.news.all&where=news&sm=tab_jum&query=%ED%83%84%EB%B2%8C%EB%8F%99'
response = driver.get(url)


infinite_loop()

html = driver.page_source
soup = bs(html, 'html.parser')

newslink = []
newstitle = []

ll = soup.select('a.news_tit')
for i in range(len(ll)):
    newstitle.append(ll[i].text)
    newslink.append(ll[i]['href'])

print(newstitle)
