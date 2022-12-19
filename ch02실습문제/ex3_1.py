
# i=1
# while i <= num:
#     num = int(input("합계를 원하는 숫자 입력 : "))

#     i+i

# print("1부터 {}까지의 합은 : {}".format(num,i))
# i=i+1

num = int(input("합계를 원하는 숫자 입력 : "))
i = 1
hap = 0
while i <=num:
    hap = hap + i
    i = i+1
print("1부터 {}까지의 합 : {}이다".format(num, hap))
