#2_1selenium.py
from selenium import webdriver
#아래 명령어로 우리가 설치한 크롬드라이버를 제어 할수있게 된다.
browser=webdriver.Chrome()
#우리가 설치한 브라우저로 아래의 url에 접속 한다.
browser.get("https://www.daum.net/")
