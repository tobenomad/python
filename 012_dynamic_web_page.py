import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
browser = webdriver.Chrome(options=options)

driver = webdriver.Chrome("/Users/haku/Downloads/chromdrver")
# driver.implicitly_wait(3)
driver.get("https://partnerplus.lgcns.com/")

user_id = 'dev2018788'
user_pw = 'from041003!'

driver.set_window_position(0, 0)
driver.set_window_size(1920, 1080)

#다나와 메인 화면의 로그인 버튼을 누르는 작업실행
driver.find_element(By.ID, 'empNo').send_keys(user_id)
driver.find_element(By.ID, 'userPw').send_keys(user_pw)

driver.find_element(By.CLASS_NAME, 'btn.btn-primary.btn-login').click()

# By.ID                    태그 id 값으로 추출
# By.NAME                  태그 name 값으로 추출
# By.XPATH                 태그 경로로 추출
# By.LINK_TEXT             링크 텍스트 값으로 추출
# By.PARTIAL_LINK_TEXT     링크 텍스트의 자식 텍스트 값 추출
# By.TAG_NAME              태그 이름으로 추출
# By.CLASS_NAME            태그 클래스명으로 추출
# By.CSS_SELECTOR CSS      선택자로 추출

# print("HTML 요소: ", login)
# print("태그 이름: ", login.tag_name)
# print("문자열: ", login.text)
# print("href 속성: ", login.get_attribute('href'))

# 창 리스트를 담아서
tabs = driver.window_handles

# 0은 main창, 1이상은 팝업창
# driver.switch_to.window(tabs[1])
# driver.close()

# main창으로 반드시 돌아와야 함
driver.switch_to.window(tabs[0])

# 정해진 시간동안 pause
driver.implicitly_wait(10)

# 메뉴 항목 중 계약체결/조회 메뉴 클릭
driver.find_element(By.ID, 'li_LPPSRC').click()     # 견적 및 계약 메뉴 클릭
driver.find_element(By.ID, 'li_LPPSRC020').click()  # 계약체결/조회 메뉴 클릭
#driver.find_element(By.ID, 'searchBtn').click()  # 계약체결/조회 메뉴 클릭

# 정해진 시간동안 pause
# driver.implicitly_wait(10)
# time.sleep(3)

# # 계약상태 클릭 전 iFRAME내로 이동
driver.switch_to.frame('legacy-content-frame')

# # 계약상태 클릭
driver.find_element(By.XPATH, '//*[@id="schForm"]/section/article/div[1]/div[4]/span').click()

# # 계약상태창에 키워드 입력전 대기 ( 드롭다운 데이터 출력 대기)
time.sleep(0.3)

# # 계약상태창에 발주완료 입력
driver.find_element(By.CLASS_NAME, 'select2-search__field').send_keys('발주완료')

# # 발주완료 관련 드롭다운 리스트 출력 대기 
time.sleep(0.3)

# #발주완료 검색을 위한 엔터
driver.find_element(By.CLASS_NAME, 'select2-search__field').send_keys(Keys.ENTER)

# # 검색버튼 클릭
driver.find_element(By.XPATH, '//*[@id="searchBtn"]').click()

# # 계약번호 입력 > 검색
# # elem2 = driver.find_element_by_name('txtContNo')       # 계약번호 선택
# # elem2.send_keys('C000058497-2')                   # 계약번호 입력

# # 정해진 시간동안 pause
# # driver.implicitly_wait(20)

time.sleep(10)