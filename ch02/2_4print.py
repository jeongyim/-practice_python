a=9
b=99

print(a)
print(b)

print(str(a).ljust(5))#5만큼 공간을 확보하고 왼쪽으로 정렬
print(str(b).ljust(5))
print(str(a).rjust(5))#5만큼 공간을 확보하고 오른쪽으로 정렬
print(str(b).rjust(5))
print(str(a).zfill(5))#5만큼 공간을 확보하고 빈공간은 0으로 채움
print(str(b).zfill(5))


for num in range(1, 30):
    print("순번 : "+str(num).zfill(3))
