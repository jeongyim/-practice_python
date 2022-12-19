#가변자료형을 매개변수로 사용할 경우

def changeData1(a,b):
    a = a+b
    print("함수내 a 값 : ",a)

def changeData2(nums):
    nums[0] = nums[0]+nums[1]+nums[2]
    print("함수내 리스트 값:",nums)

a=10
b=20
changeData1(a,b)
print("a의 값:",a)

list1=[10,20,30]
changeData2(list1)
print("리스트 값 : ",list1)
