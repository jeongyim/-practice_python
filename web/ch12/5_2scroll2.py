#5_2scroll2.py
#2초에 한번씩 스크롤을 내려서 마지막 페이지 까지 이동
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
br=webdriver.Chrome()
br.maximize_window()
br.get('https://shopping.naver.com/home')
time.sleep(3)
#검색어:마우스 입력
el =br.find_element(By.XPATH,'//*[@id="__next"]/div/div[1]/div/div/div[2]/div/div[2]/div/div[2]/form/fieldset/div[1]/div/input')
el.send_keys('마우스')
time.sleep(3)
# #검색버튼 클릭
br.find_element(By.XPATH,'//*[@id="_verticalGnbModule"]/div/div[2]/div/div[2]/div/div[2]/form/fieldset/div/button[2]').click()
#엔터키 처리
#from selenium.webdriver.common.keys import Keys
#el.send_keys(Keys.ENTER)
time.sleep(3)
#2초에 한번씩 스크롤을 내려서 마지막 페이지 까지 이동
interval = 2
ph=br.execute_script('return document.body.scrollHeight')#처음 문서 높이 저장
#반복수행
while True:
    br.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    #페이지 로딩 대기
    time.sleep(interval)
    #변경 후 현재 문서 높이 저장
    ch=br.execute_script('return document.body.scrollHeight')
    print(ph)
    print(ch)
    print("---------")
    if ch==ph:
        break
    ph=ch
#맨 위로 올리기
br.execute_script('window.scrollTo(0, 0)')
time.sleep(3)
br.quit()
