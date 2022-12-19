#100보다 큰수 입력시 발생하는 에러는 없음으로 직접 에러를 발생 시켜 본다.
try:
    print("100 이하숫자 사칙연산 계산기 입니다.")
    num1=int(input("첫번째 숫자를 입력하세요 :"))
    num2=int(input("두번째 숫자를 입력하세요 :"))
    if num1>100 or num2>100:
        raise ValueError#에러를 발생시킨다.
    print("두수의 합 : {0}, 차:{1}, 곱:{2},나눈값:{3} 입니다"\
        .format(num1+num2,num1-num2,num1*num2,num1/num2))
except ValueError:#에러 처리를 한다.
    print("100보다 큰수를 입력하였습니다.")
