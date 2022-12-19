#계산기
try:
    print("사칙연산 계산기 입니다.")
    num1=int(input("첫번째 숫자를 입력하세요 :"))
    num2=int(input("두번재 숫자를 입력하세요 :")) #4라인
    print("두수의 합 : {0}, 차:{1}, 곱한 값:{2},나누값:{3} 입니다"\
        .format(num1+num2,num1-num2,num1*num2,num1/num2))
except ValueError:#숫자가 아닌 값을 입력하였을 경우
    print("잘못된 값을 입력하여 에러가 발생햐였습니다.")
except ZeroDivisionError:#두번째 숫자를 0으로 입력하였을 경우
    print("0으로는 나누기를 할 수 없습니다.")
#다른 에러에 대한 예외처리
#실수로 5라인(num2)을 주석처리 후 실행했을 경우
#except :
#    print("알수 없는 에러가 발생하였습니다.")
except Exception as err:#에러 내용을 알고 싶을 때
    print("알수 없는 에러가 발생하였습니다.")
    print(err)#발생하는 에러 문장을 그대로 출력한다.
print("다음에는 무엇을 할까요?")
