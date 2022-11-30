#딕셔너리 자료 생성
person1 = {"name":"박찬성","age":35,"gender":"남"}
person2 = {"name":"최미영","age":31,"gender":"여"}
person3 = {"name":"박다경","age":3,"gender":"여"}
#중첩된 딕셔너리 자료 생성
family={"아빠":person1,"엄마":person2, "딸":person3}

# 딕셔너리 변수에 담긴 '아빠'라는 키에 매핑된 값을 출력
print(family["아빠"])

#딕셔너리 변수에 담긴 '아빠'라는 키에 매핑된 값(딕셔너리)로부터
#'name' 이라는 키에 매핑된 값을 출력
print(family["아빠"]["name"])
#family 딕셔너리의 모든 키를 순회하여 방문
for member in family:
  print(member + ': ' + str(family[member]))

#딕셔너리에 특정 키가 존재하는지 체크
print("아빠" in family)
print("언니" in family)


#새로운 딕셔너리형 변수인 person4를 정의
person4 = {
    "name": "가상의 언니",
    "age": 5,
    "gender": "여",
    "married": False
}

#기존 family 딕셔너리에 새로운 키인 "언니"를 추가하고
#매핑된 값으로 person4를 대입
family["언니"] = person4
print(family["언니"])

#기존에 존재하는 키인 "아빠"에 새로운 값을 매핑
family["아빠"] = person4
print(family["아빠"])

#"아빠" 라는 키와 매핑된 값을 fanily 딕셔너리로 부터 삭제
del family["아빠"]

for member in family:
    print(member , ":",family[member]) 

