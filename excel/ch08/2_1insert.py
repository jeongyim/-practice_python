from openpyxl import load_workbook
wb=load_workbook("sample.xlsx")
ws=wb.active
#빈 줄 삽입하기
ws.insert_rows(3)#3번째 줄에 한 줄 빈줄 삽입
ws.insert_rows(2,3)#2번째 줄에 3줄 빈 줄 삽입
ws.insert_cols(2)#B열에 빈 열 추가
ws.insert_cols(1,3)#A열에 빈 열 3개 추가

wb.save("sample_inster.xlsx")
wb.close()
