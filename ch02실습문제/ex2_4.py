# grade = int(input("점수를 입력하세요 : "))

# if grade >= 60:
#     if grade >=70:
#         if grade >=80:
#             if grade >= 90:
#                 print("A학점입니다.")
#             else:
#                 print("B학점입니다.")
#         else:
#             print("C학점입니다.")
#     else:
#         print("D학점입니다.")
# else:
#     print("F학점입니다.")

score = int(input("점수를 입력하세요 : "))
if 60 <= score:
    if 70 <= score:
        if 80 <= score:
            if 90 <= score:
                print("A학점입니다.")
            else:
                print("B학점입니다.")
        else:        
            print("C학점입니다.")
    else:
        print("D학점입니다.")
else:
    print("F학점입니다.")