from account import *
from imap_tools import MailBox #메일을 가져오기 위해 임포트
sender_list =[]#가져온 메일을 보관 할 변수
with MailBox("imap.gmail.com", 993).login(EMAIL_ADDRESS,EMAIL_PASSWORD,\
    initial_folder="INBOX") as mailbox:
    i=0 #도착 순번 체크
    for msg in mailbox.fetch('(SENTSINCE 13-Dec-2022)'):

    #제목이 "실습메일2-"도착한 메일을 검색한다.
        if "실습메일2-" in msg.subject :
            subject, name = msg.subject.split("-")#”-”문자를 구분자로하여 문자를 나눔
            date=msg.date
	        #내용을 잘 가져오는지 확인하고 주석 처리한다
            #i=i+1
            #print("순번 :{} 이름:{} 도착일시:{}" .format(i, name,date))
            # 엑셀 첨부파일이 있는 것을 검색한다. 앞 페이지의 if문 안에 코딩한다. 
            for att in msg.attachments:
                if ".xlsx" in att.filename:
                    i=i+1
                    print("순번 :{} 이름:{} 도착일시:{} 첨부파일:{}" .format(i, name,date,att.filename))
                    sender_list.append((msg, i, name))
# #메세지 객체와 순번 이름이 리스트에 잘 들어 간것을 확인하고 주석처리한다.
#for sender in sender_list:
#    print(sender)
print("선정 탈락 메일 발송")
import smtplib
from email.message import EmailMessage
maxPeople=3 #최대 축하메일 발송 수
with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)

    for sender in sender_list:
        to_address =sender[0].from_ #메세지 객체에서 보낸 사람의 메일 주소를 가져온다.
        # index = sender[1]#도착 순번을 가지고 온다. 
        # name=sender[2]#이름을 가지고 온다.
        #위 두줄을 아래 한줄로 나타낼 수 있다.
        index, name = sender[1:]
    if index <= maxPeople:
        title = "축하축하"
        content="{}님 축하드립니다. 선착순 3위안에 메일이 도착했습니다. (도착순번:{})"\
            .format(name, index)
    else:
        title = "잘하셨습니다. "
        content="{}님 아쉽게도 3위안에 도착하지 못하였습니다.\n\
            참여해 주셔서 감사합니다. (도착순번:{})".format(name, index)

        msg =EmailMessage()
        msg["Subject"]=title
        msg["From"] = EMAIL_ADDRESS
        msg["To"]=to_address
        msg.set_content(content)
        smtp.send_message(msg)
        print(name,"님에게 메일 발송 완료")

print("3. 명단 엑셀 파일 생성")
from openpyxl import Workbook
wb=Workbook() #엑셀의 워크북 객체 생성
ws=wb.active #현재 활성화 되어있는 sheet를 사용

ws.append(["<참석자 명단>"])
ws.append(["순번", "이름","메일주소"])
for sender in sender_list:
    index,name=sender[1:]
    address = sender[0].from_
    ws.append([index, name, address])
ws.append(["<당첨자 명단>"])
ws.append(["순번", "이름"])
for sender in sender_list[:maxPeople]:
    # index = sender[1]
    # name=sender[2]
    # ws.append([index, name])
    ws.append(sender[1:]) #위 세줄을 한 줄로 표현
wb.save("sendPeople.xlsx") ; wb.close()
print("엑셀파일 생성 완료")

