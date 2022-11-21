import requests
from bs4 import BeautifulSoup

#구글뉴스 검색 ( robots.txt 내용에 따라 검색어를 통한 결과 크롤링은 deny됨 )
base_url = "https://news.google.com"
topic_url = base_url + "/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx6TVdZU0FtdHZHZ0pMVWlnQVAB?hl=ko&gl=KR&ceid=KR%3Ako"

resp = requests.get(topic_url, verify=False)
html_src = resp.text

soup = BeautifulSoup(html_src, 'html.parser')

# 뉴스 아이템 블록을 선택
news_items = soup.select('div[class="XlKvRb"]')
# print(len(news_items))
# print(news_items[0])
# print("\n")

# 각 뉴스 아이템에서 "링크, 제목, 내용, 출처, 등록일시" 데이터를 파싱(BeautifulSoup)
for item in news_items[:3]:
    link = item.find('a', attrs={'class':'WwrzSb'}).get('href')
    news_link = base_url + link[1:]
    print(news_link)
    
    news_title = item.find('hr4', attrs={'class':'gPFEn'}).getText()
    print(news_title)
    
    news_content = item.find('span', attrs={'class':'xBbh9'}).text
    print(news_content)