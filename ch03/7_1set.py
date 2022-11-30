#세트(집합) : 중복이 안되고 순서가 없음
my_set={1,2,3,3,3}
print(my_set)

java={"유재석","김태호","양세형"}
python = {"유재석","박명수"}

# & , intersection 교집합
print(java&python)
print(java.intersection(python))

#| , union 합집합:순서는 보장되지 않음
print(java|python)
print(java.union(python))

#-, difference 차집합
print(java-python)
print(java.difference(python))

#add 추가
python.add("김태호")
print(python)

#삭제
java.remove("김태호")
print(java)