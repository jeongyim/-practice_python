# num= int(input("첫 번째 숫자 입력 : "))
# num2= int(input("두 번째 숫자 입력 : "))

# if num > num2:
#     print("두 수 중에 큰수는 {}이고 작은 수는 {}입니다.".format(num,num2))
# elif num == num2:
#     print("두 수는 같습니다.")

# else:
#     print("두 수 중에 큰수는 {}이고 작은 수는 {}입니다.".format(num2,num))


num1 = int(input("첫번째 숫자 입력 : "))
num2 = int(input("두번째 숫자 입력 : "))
if num1 > num2:
    print("두 수 중에 큰수는 ", num1,"이고, 작은 수는", num2,"이다.")
else:
    print("두 수 중에 큰수는 ", num2,"이고, 작은 수는", num1,"이다.")