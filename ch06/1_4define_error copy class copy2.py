#<BignumberError를 우리가 클래스로 만들어서  사용해 본다.

class BignumberError(Exception):#Exception을 상속받음
    pass
try:
    print("100 이하숫자 사칙연산 계산기 입니다.")
    num1=int(input("첫번째 숫자를 입력하세요 :"))
    num2=int(input("두번째 숫자를 입력하세요 :"))
    if num1>100 or num2>100:
        raise BignumberError
    print("두수의 합 : {0}, 차:{1}, 곱한값:{2},나누값:{3} 입니다"\
        .format(num1+num2,num1-num2,num1*num2,num1/num2))
except ValueError:
    print("잘못된 값을 입력하였습니다.")
except BignumberError:
    print("100보다 큰 수를 입력하였습니다. ")
