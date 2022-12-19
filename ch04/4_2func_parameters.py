#기본값::매개변수가 기본적으로 값을 가지고 있음
#우리집에 바나나가 항상 있는 경우 우리집 과일을 출력
def myFruit(a,b,c="바나나"):
    print("우리집 과일 3가지: {}{}{}".format(a,b,c))
myFruit("배","딸기")

#키워드 값 :같은 변수이름에 값 할당
def yourFruit(a,b,c):
    print("너거집 과일 : {}{}{}".format(a,b,c))
yourFruit(c="수박",a="배",b="산딸기")

#가변인자 사용:매개변수의 갯수가 가변적일때
def fruit(name,*a):
    print("{}의 집 과일: ".format(name),end="") #줄바꿈 방지
    for i in a:
        print(i,end="")
    print() #줄바꿈을 위해 넣어둠

fruit("유재석","사과","바나나")
fruit("송지효","딸기")
fruit("김종국","바나나","배", "수박")
