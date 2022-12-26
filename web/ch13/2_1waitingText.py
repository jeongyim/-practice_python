from selenium import webdriver
import time
from selenium.webdriver.common.by import By

br = webdriver.Chrome()
br.maximize_window()
br.get('http://air.auction.co.kr/au/init/lp/lpMain.do')
time.sleep(3)
br.find_element(By.LINK_TEXT, '검색하기').click()
#<로딩 대기시간 처리>
#time.sleep(10)#로딩 대기시간을 10초로 오래 동안 기다린 후 실행
# 실행이 잘 안될 경우 터미널창 쓰레기 통을 비우고 다시 실행

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
#실패일 경우 터미널창 쓰레기 통을 비우고 다시 실행
try:
    #최대10초(br, 10)동안 기다리지만 특정 엘리먼트가 나타나면 바로 실행한다.
    #특정 엘리멘트 경로는 튜플로 감싼다.
    #가는편 시간 정보 출력
    el=WebDriverWait(br, 10).until(ec.presence_of_element_located(\
        (By.XPATH,'//*[@id="tour_wrap"]/div[4]/ul/li[1]/div[1]/table/tbody/tr/td[2]/ul/li[1]')))
    print(el.text)
except:
    print("실패했어요")
#왕복 시간 정보 출력
    # el=WebDriverWait(br, 10).until(ec.presence_of_element_located(\
    #     (By.XPATH,'//*[@id="tour_wrap"]/div[4]/ul/li[1]/div[1]/table/tbody/tr/td[2]/ul')))
    #왕복 모든 정보 출력
    el=WebDriverWait(br, 10).until(ec.presence_of_element_located(\
        (By.XPATH,'//*[@id="tour_wrap"]/div[4]/ul/li[1]/div[1]/table/tbody/tr')))





# #가는편 시간
# el=br.find_element(By.XPATH,\
#     '//*[@id="tour_wrap"]/div[4]/ul/li[1]/div[1]/table/tbody/tr/td[2]/ul/li[1]')
# print(el.text)#엘리먼트 안의 있는 텍스트 출력
# # 특정 엘리먼트가 도착할 때까지 기다림 
time.sleep(5)
br.quit()