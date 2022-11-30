sum = 0
while True:
    num = int(input("더할 숫자를 입력하세요 : "))
    sum += num
    if sum >30:
        print("총합이 30을 넘었음으로 종료합니다.")
        break
    else:
        continue
    print(sum)
print(f"총 합의 결과는 {sum}입니다.")