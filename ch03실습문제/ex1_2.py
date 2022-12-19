# from random import *

# a = randint(1,10)
# b = randint(1,10)
# print("첫번째 숫자 ", a)
# print("두번째 숫자 ", b)


# print("두수의 합 : " , a+b, "두수의 차 : ", a-b, "두수의 곱 : ", a*b, "두 수의 평균 :", (a+b)/2, "입니다." )
# if a>b:
#     print("두수 중 작은수 :",b ,", 큰 수 :", a,"입니다.")
# elif a <b :
#      print("두수 중 작은수 :",a ,", 큰 수 :", b,"입니다.")
# else:
#     print("잘못입력하였습니다.")

from random import*
num1=randrange(1,11)
num2=randrange(1,11)
print("첫번째 숫자 : {}".format(num1))
print("두번재 숙자 : {}".format(num2))
print("두수의 합:{},두수의 차:{},두수의 곱:{},두수의 평균:{}입니다."\
    .format(num1+num2,num1-num2,num1*num2,(num1+num2)/2))
print("두수중 작은수: {},큰수: {}입니다.".format(min(num1,num2),max(num1,num2)))
