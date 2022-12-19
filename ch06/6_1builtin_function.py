#dir :어떤 객체를 넘겨 줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
print(dir()) #random모듈을 임포트 하기전에 가지고 있는 함수를 볼수있다. 
import random #외장함수 추가
print(dir())#위 실행결과에서 'random’추가
print()
import turtle
print(dir()) #위 실험결과에서 'turtle’추가
print()
#특정 모듈에서 사용할수있는 변수 함수 알기
print(dir(random)) # 'randint', 'random', 'randrange',이외에 엄청 많음
print()
lis = [1,2,3]
print(dir(lis))
print()
tup = (1,2,3)
print(dir(tup))
print()
ch = "나랄"
print(dir(ch))
print()
a=eval("12+4+6")
print(a)
print()
heroes = '"윤봉길","이화영","안중근","김구"'
for i , name in enumerate(heroes):
    print(i,name)

print()
print(len("python"))
print(len("python is good."))
print(len([1,2,3,4,5]))
print(len((1,'a',[1,2,3]))) #결과 :3

list1 = ["한국","영국","프랃스"]
list2 = ["서울","런던","파리"]
for i , w in zip(list1,list2):
    print(i,w)
list1 = ["한국","영국","프랃스"]
list2 = ["서울","런던","파리"]
zip_list = list([x,y] for x,y in zip(list1,list2))
print(list(zip_list))

