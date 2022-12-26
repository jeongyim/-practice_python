#6_1scrollFixed.py
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
br=webdriver.Chrome()
br.get('https://www.w3schools.com/TAgs/default.asp')
br.maximize_window()
time.sleep(3)#화면을 가져올 때까지 잠시 대기
#<<head> xpath가져오기>
el = br.find_element(By.XPATH,'//*[@id="leftmenuinnerinner"]/div/a[51]')
#el=br.find_element (By.XPATH,'//*[@ id="leftmenuinnerinner"]/div/a[text()="<head>"]')
#실행이 잘 안될 경우 VSCode를 종료 후 다시 켠다.  
#ActionChain를 통해서 <html>까지 이동
# from selenium.webdriver.common.action_chains import ActionChains          
# ac=ActionChains(br)#화면을 가져와서
# ac.move_to_element(el).perform() #해당 엘리먼트까지 이동
# time.sleep(3)
# br.quit()
#엘리먼트 좌표정보를 이용해 이동
xy=el.location_once_scrolled_into_view #head가 제일 위에 위치
print("type: ",type(xy))
print("value:",xy)
print(xy["y"])
time.sleep(3)
el.click() #스크롤 하지 않아 화면에 보이지 않아도 클릭은 가능
time.sleep(3)
br.quit()
