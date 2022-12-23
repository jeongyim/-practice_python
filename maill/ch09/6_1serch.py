#6_1search.py
from imap_tools import MailBox
from account import*
# mailbox = MailBox("imap.gmail.com",993)
# mailbox.login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX")
#mailbox.logout()
#위 세 줄의 명령을 with를 사용하여 해 본다.
with MailBox("imap.gmail.com",993).login(EMAIL_ADDRESS, EMAIL_PASSWORD, \
    initial_folder="INBOX")as mailbox:
    #최근 메일 5개 검색해서 [발신자]제목 형식으로 출력
    for msg in mailbox.fetch(limit=5, reverse=True):
        print("[{}] {}".format(msg.from_,msg.subject))
   #print("*"*50)
    #읽지 않은 메일 5개 검색
    for msg in mailbox.fetch("(UNSEEN)",limit=5,reverse=True):
        print("[{}] {}".format(msg.from_,msg.subject))
   #print("*"*50)
    #특정인이 보낸 메일 검색
    for msg in mailbox.fetch('(leejungyim3349@gmail.com)',limit=5,reverse=True):
        print("[{}] {}".format(msg.from_,msg.subject))
    #어떤 글자를 포함하는 메일(제목, 본문)검색
    #검색 부분은 항상 작은 따옴표로 밖을 감싸고, 큰따옴표로 검색할 단어를 감싸도록 한다.
    for msg in mailbox.fetch('(TEXT "test")'):
        print("[{}] {}".format(msg.from_, msg.subject))
    #어떤 글자를 포함하는 메일(제목만) 검색
    for msg in mailbox.fetch('(SUBJECT "test")'):
        print("[{}] {}".format(msg.from_, msg.subject))
    #한글 검색
    for msg in mailbox.fetch(limit=10, reverse=True):
        if "테스트" in msg.subject: #제목 검색, 본문은 msg.text
            print("[{}] {}".format(msg.from_, msg.subject))
    #특정 날짜이후 메일 검색
    for msg in mailbox.fetch('(SENTSINCE 07-May-2022)',reverse=True, limit=5):
        print("[{}] {}".format(msg.from_, msg.subject))
    #특정 날짜 메일 검색
    for msg in mailbox.fetch('(ON 17-Jun-2022)',reverse=True, limit=5):
        print("[{}] {}".format(msg.from_, msg.subject))
    #두개 이상의 조건이 모두 만족되는 것 검색(조건 뒤에 한 칸 띄우고 계속 조건을 적으면 된다. )
    for msg in mailbox.fetch('(ON 17-Jun-2022 SUBJECT "test")',reverse=True, limit=5):
        print("[{}] {}".format(msg.from_,msg.subject))
    #두개 이상의 조건 중 하나라고 만족되는 것 검색(OR 조건 )
    for msg in mailbox.fetch('(OR ON 17-Jun-2022 SUBJECT "test")',reverse=True, limit=5):
        print("[{}] {}".format(msg.from_,msg.subject))
