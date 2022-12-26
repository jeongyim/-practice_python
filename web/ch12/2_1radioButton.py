import time
from selenium import webdriver
br = webdriver.Chrome()
br.maximize_window()
br.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_radio')
br.switch_to.frame('iframeResult')
time.sleep(3)
from selenium.webdriver.common.by import By
el = br.find_element(By.XPATH,'//*[@id="html"]')
if el.is_selected()==False:
    print("선택이 안되어 있음으로 선택하기")
    el.click()
else:
    print("선택이 되어 있음으로 아무것도 안함")
    
el.click()
br.switch_to.default_content()
time.sleep(3)
br.quit()