from openpyxl import Workbook
wb = Workbook() #새 워크북 생성 저장은 되지 않은 상태
ws = wb.active  #현재 활성화된 sheet 가져와서 ws 저장해서 작업한다. 
ws.title = "pySheet" #sheet 의 이름을 변경
wb.save("sample.xlsx")  #excel 파일을 sample.xlsx 로 저장
wb.close()  #excel 파일을 닫아준다.
