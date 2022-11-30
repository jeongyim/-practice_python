# 딕셔너리 자료형 변수 선언
a = {
    "name": "박찬성",
    "age": 35,
    "gender": "남",
    "married": True
}

#a딕셔너리를 복사하여 반환
b=a.copy()
print(a)
print(b)
#a 딕셔너리의 엘리먼트릴를 삭제
a.clear()
print(a)
#b딕셔너리의 키와 값을 요소로하는 튜플목록을 리스트형 데이터로 반환
print(b.items())
#b 딕셔너리의 키의 목록을 리스트 형태로 반환
print(b.keys())

#b딕셔너리의 키를 제외한 값의 목록 리스트를 리스트형 데이터로 반환한다. 
print(b.values())

#b딕셔너리의 age키에 해당하는 엘리먼트리를 삭제하고 삭제된 엘리멘터리 값을 반환
print(b.pop("age"))
print(b)

#딕셔너리의 가장 마지막 엘리먼트리를 삭제하고 , 삭제된 엘리먼 트리를 반환 한다. 
print(b.popitem())
print(b)
