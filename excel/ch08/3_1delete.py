from openpyxl import load_workbook
wb=load_workbook("sample.xlsx")
ws=wb.active

ws.delete_rows(3)#3번째 줄 삭제
ws.delete_rows(1,2)#1번째줄로 부터 2줄 삭제
ws.delete_cols(2)#2번째칼럼 국어 열 삭제
ws.delete_cols(1,2)#1번째 칼럼부터 2칼럼(번호,영어칼럼 삭제)

wb.save("sample_delete.xlsx")
wb.close()
