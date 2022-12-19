num = int(input("배수 숫자 입력 : "))
i = 0
sum = 0
while i<100:
    i = i+1
    if(i%num) !=0 :
        continue
    sum = sum +i
print("1부터 100까지의 {}의 배수의 합 : {}".format(num,sum))

