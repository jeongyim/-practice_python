#3_1airlineTicket.py
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
br=webdriver.Chrome()
br.maximize_window()
br.get('http://air.auction.co.kr/au/init/lp/lpMain.do')
time.sleep(5)
#출발지 선택
el=br.find_element(By.XPATH,\
    '//*[@id="global_fromkr_ddesc_val"]')
el.click()#출발지 선택
time.sleep(3)#부산선택
br.find_element(By.XPATH,\
    '//*[@id="tour_wrap"]/div[1]/div[4]/div[2]/div[4]/div[1]/div[1]/div/a[6]').click()
time.sleep(3)#도착지 선택
br.find_element(By.XPATH,\
    '//*[@id="global_fromkr_adesc_val"]').click()
time.sleep(3)#다낭 선택
br.find_element(By.XPATH,\
    '//*[@id="layer_city_search"]/div[1]/div/div[2]/div/table/tbody/tr[1]/td/ul/li[4]/a').click()
time.sleep(3)#출발일 선택
br.find_element(By.XPATH,\
    '//*[@id="datapicker_A_1').click()
time.sleep(3)#날짜선택
br.find_element(By.XPATH,\
    '//*[@id="ui-datepicker-div"]/div[1]/table/tbody/tr[4]/td[7]/a').click()
time.sleep(3)#귀국일 선택
br.find_element(By.XPATH,\
    '//*[@id="datapicker_A_2').click()
time.sleep(3)#날짜 선택
br.find_element(By.XPATH,\
    '//*[@id="ui-datepicker-div"]/div[2]/table/tbody/tr[4]/td[2]/a').click()
time.sleep(3)#검색버튼 클릭
# br.find_element_by_xpath('//*[@id="tour_wrap"]/div[1]/div[4]/div[4]/a').click()
br.find_element(By.LINK_TEXT,'검색하기').click()
time.sleep(3)
#<로딩 대기시간 처리>
#특정 엘리먼트가 도착할 때까지 기다림 

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
try:
    #(br, 10)#브라우저를 10초 동안 기다린다.
    # 가는편 시간 정보
    # el=WebDriverWait(br, 15).until(ec.presence_of_element_located(\
    #     (By.XPATH,'//*[@id="tour_wrap"]/div[4]/ul/li[1]/div[1]/table/tbody/tr/td[2]/ul/li[1]')))
    #왕복 전체 정보 
    el=WebDriverWait(br, 10).until(ec.presence_of_element_located(\
    (By.XPATH,'//*[@id="tour_wrap"]/div[4]/ul/li[1]/div[1]/table/tbody/tr')))
    print(el.text)
except:
    print("실패했어요")
time.sleep(5)
br.quit()
