from random import *
nums=list()
i=1
while True:
    nums.append(randint(1,100))
    i = i+1
    if i <= 15:
        continue
    else:
        print("값 : ",nums)
        break
print("3의 배수", end=":")
for num in nums:
    if (num %3)==0:
        print(num,end=" ")