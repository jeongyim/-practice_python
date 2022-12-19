#ex ) 우리가 예외 처리하지 않은 ZeroDivisionError가 발생할 때도 실행된다.
class BignumberError(Exception):
    def __init__(self,msg):
        self.msg=msg
    def __str__(self):#해당 에러 발생시 msg값을 err 값으로 돌려 준다.
        return self.msg

try:
    print("100 이하숫자 사칙연산 계산기 입니다.")
    num1=int(input("첫번재 숫자를 입력하세요 :"))
    num2=int(input("두번째 숫자를 입력하세요 :"))
    if num1>100 or num2>100:
        raise BignumberError("입력값 : {0},{1}".format(num1, num2))
    print("두수의 합 : {0}, 차:{1}, 곱한값:{2},나누값:{3} 입니다"\
        .format(num1+num2,num1-num2,num1*num2,num1/num2))
except ValueError:
    print("잘못된 값을 입력하였습니다.")
except BignumberError as err:
    print("에러가 밣생하였습니다. 한 자리 숫자만 입력하세요")
    print(err)
finally:
    print("에러 발생유무와 관계없이 무조건 실행")
print("다음에는 무엇을 할까요?")
