#1_1 download.py
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
#<다운로드 폴더로 다운로드하기>
# br=webdriver.Chrome()
# br.maximize_window()
# br.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_a_download')
# br.switch_to.frame('iframeResult')
#download클릭-다운로드 디렉토리에 다운로드
# br.find_element(By.XPATH,'/html/body/p[2]/a/img').click()
#우리의 작업 공간인 test폴더안에 다운로드 받기
from selenium.webdriver.chrome.options import Options
co=Options()#co는 chrome option을 줄여서 사용
#다운로드 기본경로를 변경해 준다.
co.add_experimental_option('prefs', \
    {'download.default_directory':r'C:\Users\박해옥\Desktop\test'})
br=webdriver.Chrome(options=co)
br.maximize_window()
br.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_a_download')
br.switch_to.frame('iframeResult')
#download클릭
br.find_element(By.XPATH,'/html/body/p[2]/a/img').click()
time.sleep(5)
br.quit()
