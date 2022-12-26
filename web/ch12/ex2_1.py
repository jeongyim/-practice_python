import time
from selenium import webdriver
from selenium.webdriver.common.by import By
br=webdriver.Chrome()
br.maximize_window()
br.get('https://www.naver.com/')
time.sleep(3)
# br.find_element_by_link_text('쇼핑').click()
br.find_element(By.LINK_TEXT, '쇼핑').click()
time.sleep(3)
el=br.find_element(By.XPATH,'//*[@id="content"]/div/div[1]/div/div[1]/div/div/div[1]/ul/li[11]/button').click()
#혹시 위위 방법이 안될 경우 아래와같이 한다.
# els=[] # 가전의 xpath를 가져와서 리스트에 넣는다.(같은 xpath가 많이 존재함으로)
# els=br.find_elements(By.XPATH,'//*[@id="rootCategoryList"]/button’)
# els[11].click()#11번지 가전 클릭
time.sleep(3)
#<마우스 오버>
from selenium.webdriver.common.action_chains import ActionChains
# el=br.find_element_by_link_text('계절가전')
el=br.find_element(By.LINK_TEXT,'계절가전')
mov=ActionChains(br).move_to_element(el)
mov.perform()
time.sleep(3)

br.find_element(By.LINK_TEXT,'에어컨').click()
time.sleep(5)
i=2000
ph=br.execute_script('return document.body.scrollHeight')
while True:
    br.execute_script('window.scrollTo(0,'+str(i)+')')
    time.sleep(5)
    ch=br.execute_script('return document.body.scrollHeight')
    if ch==ph:
        break
    ph=ch
    i += 2000
br.execute_script('window.scrollTo(0,0)')
#검색란 XPATH가져오기
el=br.find_element(By.XPATH, \
    '//*[@id="__next"]/div/div[1]/div/div[2]/div/div[2]/form/fieldset/div[1]/input')
el.send_keys('제습기')
el=br.find_element(By.XPATH, \
    '//*[@id="__next"]/div/div[1]/div/div[2]/div/div[2]/form/fieldset/div[1]/button[2]')

time.sleep(3)
el.click()
time.sleep(5)
br.quit()

