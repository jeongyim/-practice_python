#지역변수와 전역 변수

def func1(a,b):
    c=0           # a,b는 지역변수
    c=a+b                 #c는 지역변수
    print("함수내 전역변수 x,y의 값 :",x,y)#전역변수는 함수안에서도 사용가능

def func2(x,y): #전역 변수와 동일한 이름을 사용. x,y는 지역변수
    x=x*2
    y=y*2
    print("함수내 지역변수 x,y의 값: ",x,y)#지역변수 x,y값으로 20과 40 출력
    global z #전역변수 선언
    z=x+y #두값의 합을 전역변수에 저장

x=10
y=20
func1(x,y)
#print(c) #지역변수는 함수 안에서만 사용가능
print("메인프로그램의 x,y값:  ",x,y)
func2(x,y)
print("메인프로그램의 x,y값: ",x,y)
print("함수내에서 선언된 전역변수 z값:",z)
