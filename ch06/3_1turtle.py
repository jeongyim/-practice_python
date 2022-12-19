#turtle와 for구문을 활용하여 원 그리기

#import time
import turtle as t #turtle모듈을 t라는 이름으로 사용하겠다.
#t.setheading(90)
for i in  range (1, 11):
    t.color("red")
    t.circle(10*i)#반지름이 10*i인 원을 생성
    
#t.setheading(90)   
for i in  range (1, 11):
    t.color("blue")
    t.circle(10*i+5)#반지름이 10*i+5 인 원을 생성

#time.sleep(5) #5초간 멈춤
 
t.done() #turtle모듈을 끝냄
