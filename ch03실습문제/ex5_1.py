from random import *

a=set()
i=0 #난수 발생 횟수를 저장

while True:
    a.add(randint(1,100))
    i=i+1
    if len(a)==10:
        break
print("중복되지 않는 난수 10개 : ",a)
print("중복된 난수 발생 횟수 : ", i-10)