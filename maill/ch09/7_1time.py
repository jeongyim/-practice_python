import time
print(time.strftime('%d-%a-%Y'))#현재날짜를 일-요일-년도로 가져옴
print(time.strftime('%d-%m-%Y'))# 일-월-년도로 가져옴
print(time.strftime('%d-%b-%Y')) # 일-월(영어)-년도로 가져옴

import datetime #특정 날짜를 변수에 저장하여 가져오기
dt=datetime.datetime.strptime("2020-10-1","%Y-%m-%d")#날짜를 년월일순으로 가져옴
print(type(dt))
print(dt)
print(dt.strftime('%Y-%b-%d'))
