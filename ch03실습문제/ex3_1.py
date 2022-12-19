# num = [[11,33,22,7],[77,2,90],[3,66,44,9,8]]

# for j in range(len(num)):
#     sum=0
#     for i in range(len(num[j])):
#         sum=sum+num[j][i] 
#     print(j+1,"번째 줄의 합:",sum,"최소값:",min(num[j]))

a = [[11,33,22,7],[77,2,90],[3,66,44,9,8]]
for i in range(len(a)):
    print(i+1,"번째 리스트 합인: ", sum(a[i]), "최소값:",min(a[i]))