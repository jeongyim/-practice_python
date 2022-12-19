fro#9_image.py
from openpyxl import Workbook
from openpyxl.drawing.image import Image
wb=Workbook()
ws = wb.active

img = Image("img1.png")
ws.add_image(img, "B2")

wb.save("sample_img.xlsx")
wb.close()

#ImportError ; You must install pillow to fetch image....
#위와 같이 에러 메세지가 나타나면 터미널 창에서
# pip install pillow
# 해서 pillow를 설치 해주면 된다.
