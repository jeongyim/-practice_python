# list of python modules로 검색
#외장함수를 turtle를 import하여 실행해본다.
from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()
