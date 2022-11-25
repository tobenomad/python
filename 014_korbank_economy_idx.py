#다른곳에 화면가져갈때 깨지지 않게 방지하는 코드
from IPython.core.display import display, HTML
display(HTML("<style> .container{width:90% !important;}</style>"))

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#100대 통계지표 엑셀 다운로드
def download_bok_statistics():
    driver = webdriver.Chrome("/Users/haku/Downloads/chromdrver")
    driver.implicitly_wait(3)
    driver.get("https://ecos.bok.or.kr/jsp/vis/keystat/#/key")
    
    excel_download = driver.find_element(By.CSS_SELECTOR, 'img[alt=download"]')
    driver.implicitly_wait(3)
    
    excel_download.click()
    time.sleep(5)
    
    driver.close()
    print("파일 다운로드 실행... ")
    
    return None

# 함수 실행
download_bok_statistics()