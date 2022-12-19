#함수는 호출되지 않으면 실행되지 않는다
def test():
    print("큰수와 작은수")
#bigSmall()

def bigSmall(a,b):
    if a > b:
        big=a
        small=b
    else:
        big=b
        small=a
    return big, small
def sum(a,b):
    c=a+b
    return c
def minus(a,b):
    c=a-b
    return c

a = int(input("첫번째 숫자 입력: "))
b = int(input("두번째 숫자 입력: "))
x,y=bigSmall(a,b)
print("큰 값:{}, 작은값:{}".format(x,y))
c=sum(x,y)
d=minus(x,y)
print("합:{}, 차{}".format(c,d))