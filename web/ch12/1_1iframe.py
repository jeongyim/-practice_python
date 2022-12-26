import time
from selenium import webdriver
br = webdriver.Chrome()
br.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_radio')
br.switch_to.frame('iframeResult')
time.sleep(3)
from selenium.webdriver.common.by import By
el = br.find_element(By.XPATH,'//*[@id="html"]')
el.click()
br.switch_to.default_content()
time.sleep(3)
br.quit()