#glob:경로 내의 폴더 /파일 목록 조회(윈도우 dir)

#import glob
#print(glob.glob("*.txt"))
#print(glob.glob("b*"))
#print(glob.glob("**/*.py"))
#print(glob.glob("**/**/*.py"))
#os:운영 체제에서 제공하는 기본기능
# import os
# print(os.getcwd())#현재 디렉토리 경로 가져오기
# fol="sample_folder"
# if os.path.exists(fol):#경로에 fol이라는 폴더가 있으면
#     print("이미 존재하는 폴더입니다.")
#     os.rmdir(fol)#폴더 삭제
#     print(fol,"폴더를 삭제하였습니다.")


# else:
#     os.makedirs(fol) #sample_folder생성
#     print(fol,"폴더생성완료")

import time

print(time.localtime())
#time.sleep(5)#5초후에 아래 문장 실행
print(time.strftime("%Y-%m-%d %H:%M:%S"))

#오늘 날짜 출력
import datetime
print("오늘은", datetime.date.today(),"일입니다.")

#timedelta : 두 날짜 사이의 간격
today =datetime.date.today()#오늘 날짜 저장
td=datetime.timedelta(days=100)#100일 저장
print("오늘 부터 100일 후의 날짜:",today + td)

meetday = datetime.datetime(2022,1,1)
print("우리가 만난 날: ",meetday)
print("우리가 만난지 100일 후의 날짜:",meetday+td)