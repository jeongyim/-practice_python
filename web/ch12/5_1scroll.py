#5_1scroll.py
#자동으로 스크롤을 내려주는 동작을 할 것이다.
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
br=webdriver.Chrome()
br.maximize_window()
br.get('https://www.amazon.com/')#아마존 접속
time.sleep(3)#화면을 다 불러 오기전에 엘리먼트를 찾으라고 할경우 에러 발생 할수 있음으로 3초정도  여유시간을 준다
#검색어 청소기 입력
el = br.find_element(By.XPATH,'//*[@id="twotabsearchtextbox"]')
el.send_keys('청소기')
time.sleep(3)#검색어를 입력하고 바로 검색을 하면 검색이 안되는 경우도 있음
#검색버튼 클릭
el = br.find_element(By.XPATH,'//*[@id="nav-search-submit-text"]').click()
#검색버튼을 이용하지 않고 바로 enter키 입력
# from selenium.webdriver.common.keys import Keys
# el.send_keys(Keys.ENTER)
time.sleep(3)
#br.quit()#<스크롤>
#지정한 위치로 스크롤 내리기
#세로로 해당 문서높이 만큼 스크롤 내리기 (바탕화면에 대고 마우스 오른쪽 버튼을 클릭하면 열리는 메뉴에서 [디스플레이 설정(D)]를 클릭합니다. 2. 열리는 창 우측에서 [디스플레이 해상도] 항목을 확인- 화면 세로크기 입력)
br.execute_script('window.scrollTo(0, 1000)')#가로,세로
time.sleep(3) 
br.execute_script('window.scrollTo(0, 2000)')#가로,세로 
time.sleep(3)
#화면 가장 아래로 스크롤 내리기
br.execute_script('window.scrollTo(0, document.body.scrollHeight)')
time.sleep(3)
br.quit()
