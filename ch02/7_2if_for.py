a=int(input("한자리 정수를 입력하세요:"))
if a < 10:
    for i in range(a):
        if i>3:
            break
        print(i)
else:
    print("입력된 수는",a,"입니다." )
