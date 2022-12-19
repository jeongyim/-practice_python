def std_weight(gender,height):
    if gender == "남자":
        return height*height*22
    else:
        return height*height*21

gender = input("'남자'또는 '여자'로 성별을 입력하세요 :") 
height = int(input("키를 입력하세요 .:"))/100 #cm를 m로 변경
weight=std_weight(gender,height)
print("당신의 표준 체중은 {}kg 입니다. ".format(round(weight)))
