#5_1cell_line_in.py
from openpyxl import Workbook
from random import*#난수를 발생시켜서 점수를 넣는다.
wb=Workbook()
ws=wb.active

#1줄 씩 데이터 넣기
ws.append(["번호","국어","영어","수학"])
for i in range(1,5):
    ws.append([i, randint(60,100), randint(60,100),randint(60,100)])
wb.save("sample.xlsx")
wb.close()
