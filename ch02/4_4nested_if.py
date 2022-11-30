score=int(input("당신의 성적을 입력하세요 : "))

if score >=60:
    if score >=70:
        if score>80:
            print("좋은 성적 80점이상입니다.")
        else:
            print("성적이 70점 이상 80점 미만입니다.")
    else:
        print("60점 이상 70점 미만입니다.")
else:
    print("성적이 60점 미만입니다.")