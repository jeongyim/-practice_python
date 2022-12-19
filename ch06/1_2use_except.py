#계산기
try:
    print("사칙연산 계산기 입니다.")
    num1=int(input("첫번째 숫자를 입력하세요 : "))
    num2=int(input("두번째 숫자를 입력하세요 : "))
    print("두 수의 합 : {}, 차:{}, 곱:{}, 나눈값:{}입니다."\
     .format(num1+num2, num1-num2, num1*num2, num1/num2))
except ValueError:
    print("잘못된 값을 입력하였습니다.")
print("다음에는 무엇을 할까요?")
