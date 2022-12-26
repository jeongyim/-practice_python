#3_1checkBox.py
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
br=webdriver.Chrome()
br.maximize_window()
br.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_checkbox')
br.switch_to.frame('iframeResult')
el=br.find_element(By.XPATH,'//*[@id="vehicle1"]')
# el=br.find_element_by_xpath('//*[@id="vehicle1"]')
if el.is_selected()==False:
    print("선택하기")
    el.click()
else:
    print("아무것도 안함")
if el.is_selected()==False:
    print("선택하기")
    el.click()
else:
    print("아무것도 안함")
time.sleep(3)
br.quit()
