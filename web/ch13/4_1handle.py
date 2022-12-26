from selenium import webdriver
import time
from selenium.webdriver.common.by import By
br=webdriver.Chrome()
br.maximize_window()

br.get('https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%82%AC%EC%A0%84')
ch=br.current_window_handle #현재 창의 핸들 정보를 가지고 온다
time.sleep(3)
print('-------------------')
print(ch)
br.find_element(By.XPATH,'//*[@id="web_1"]/div[1]/div[2]/div[2]/a').click()
handls=br.window_handles #모든 핸들 정보 를 가지고 온다.
print("-------------------")
print(handls)
#각 핸들로 이동해서 해당 브라우저의 title출력해보기
for handle in handls:
    print(handle)
    br.switch_to.window(handle)
    print(br.title)
    print('------------------------')
# 네이버 사전 브라우저 화면 닫고 처음 브라우저로 돌아오기
print("핸들닫기")
time.sleep(3)
br.close()
print("처음 핸들로 돌아오기")
time.sleep(3)
br.switch_to.window(ch)
print(br.title)
print("daum브라우저로 이동해보기")
time.sleep(3)
br.get("http://daum.net")
time.sleep(5)
br.quit()

