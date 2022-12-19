#문제1
phone={}
for i in range(3):
    id = input("학생의 학번을 입력하세요 : ")
    ponNum = input("전화번호를 입력하세요 : ")
    phone[id]=ponNum
print("학생전화번호부 완성")


for i in phone:
    print(i,":",phone[i])
 
#전화번호 검색
while True:
    
    id = input("검색을 원하는 학생의 학번을 입력하세요(검색종료:0000) : ")
    if id == "0000":
        break
    if id in phone:
        print("입력한 학생의 전화번호는" ,phone[id])
    else:
        print("입력한 학생의 전호번호가 없습니다. ") 
