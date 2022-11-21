import requests
from bs4 import BeautifulSoup

#구글뉴스 검색 ( robots.txt 내용에 따라 검색어를 통한 결과 크롤링은 deny됨 )
base_url = "https://news.google.com"
topic_url = base_url + "/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx6TVdZU0FtdHZHZ0pMVWlnQVAB?hl=ko&gl=KR&ceid=KR%3Ako"

resp = requests.get(topic_url, verify=False)
html_src = resp.text

soup = BeautifulSoup(html_src, 'html.parser')

print(soup)