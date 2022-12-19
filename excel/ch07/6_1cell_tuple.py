from openpyxl import load_workbook
wb=load_workbook("sample.xlsx")
ws=wb.active
#전체 row정보 가져오기
print(ws.rows)#알수없는 정보 출력:<generator object Worksheet._cells_by_row at 0x0000024E0F8D1230>
print(tuple(ws.rows))#전체 rows에 대한 객체 정보를 한 줄씩 가져옴
print("***********************")
print(tuple(ws.columns))#전체 정보를 한 컬럼씩 가져옴
print("***********************")
#각 row 정보를 출력
for row in tuple(ws.rows):
    print(row)#하나의 튜플씩 출력
for row in tuple(ws.rows):
    print(row[1].value)#각 튜플중 두번째 값만 출력 할 것이다.
print("***********************")
#위와 같이 column에도 접근할 수 있다.
for col in tuple(ws.columns):
    print(col)
for col in tuple(ws.columns):
    print(col[0].value)
