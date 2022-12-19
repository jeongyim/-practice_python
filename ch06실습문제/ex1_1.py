# print("구구단을 출력")
# try:

#     num=int(input("2~9단중 출력하고 싶은 단을 입력하세요 : "))
#     i = 2
#     while i<=9:
#         print(num,"*",i,"=",num*i)
#         i = i + 1
# except ValueError:
#     print("에러가 발생하였습니다. 2~9단 까지만 입력하세요")
# print("이용해 주셔서 감사합니다")

class GuguDanError(Exception):
    def __init__(self,msg):
        self.msg=msg
    def __str__(self):#해당 에러 발생시 msg값을 err 값으로 돌려 준다.
        return self.msg

try:

    print("구구단을 출력")
    num1=int(input("2~9단중 출력하고 싶은 단을 입력하세요 :"))
    
    if num1 < 2 or num1>9:
        raise GuguDanError("입력값 : {0}".format(num1))
    else:    
        for i in range(1,10):
            a=num1*i
            print("{0} X {1} = {2}".format(num1,i,a))
except ValueError:
    print("잘못된 값을 입력하였습니다.")
except GuguDanError as err:
    print("에러가 발생하였습니다. 2~9단 까지만 입력하세요")
    print(err)
finally:\
    print("이용해 주셔서 감사합니다.")
