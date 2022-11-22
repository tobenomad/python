from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("/Users/haku/Downloads/chromdrver")
driver.implicitly_wait(3)
driver.get("https://partnerplus.lgcns.com/")

user_id = 'dev2018788'
user_pw = 'from041003!'

driver.implicitly_wait(3)

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
driver.switch_to.window(tabs[1])
driver.close()

# main창으로 반드시 돌아와야 함
driver.switch_to.window(tabs[0])

# 정해진 시간동안 pause
driver.implicitly_wait(10)

# 메뉴 항목 중 
driver.find_element(By.LINK_TEXT, '계약체결/조회').click()