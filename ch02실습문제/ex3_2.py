num=int(input("출력을 원하는 단을 입력 : "))
print("***",num,"***")
print("for문을 이용한 구구단")
for i in range(1,10):
    print(num,"*",i,"=",num*i)
print("while문을 이용한 구구단")
i = 1
while i<=9:
    print(num,"*",i,"=",num*i)
    i = i + 1
