#4_1option.py
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
br=webdriver.Chrome()
br.maximize_window()
br.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_option')
br.switch_to.frame('iframeResult')

#car에 해당하는 element를 찾고,  3번째 옵션 선택
el=br.find_element(By.XPATH,'//*[@id="cars"]/option[3]')
# 옵션 중 text가 'Opel'선택
# el=br.find_element(By.XPATH,'//*[@id="cars"]/option[text()="Opel"]')
# 텍스트 값이 부분 일치하는 항목 선택 방법-
#contains(text(),뒤에 한 칸 띄우고 “부분 검색어” 넣기)
# el=br.find_element(By.XPATH,'//*[@id="cars"]/option[contains(text(), "Op")]')
time.sleep(3)
el.click()
time.sleep(3)
br.quit()
