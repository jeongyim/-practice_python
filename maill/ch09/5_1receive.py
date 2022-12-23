from imap_tools import MailBox
from account import*
mailbox = MailBox("imap.gmail.com",993)#메일을 가져올때는 포트번호를 993번으로 한다.
#initial_folder="INBOx":받은 편지함이 선택된다.

mailbox.login(EMAIL_ADDRESS,EMAIL_PASSWORD, initial_folder="INBOX")
# limit : 최대 메일 개수
# reverse : True 일 경우 최근 메일부터, False 일 경우 과거 메일부터
#limit=1:최대 메일 1개를 가지고 오겠다.
#reverse=True:메일을 최근 순(가장 늦게 도착한 것)부터 가지고 온다.
for msg in mailbox.fetch(limit=1,reverse=True): #전체메일 가져오기:mailbox.fetch()
    print("제목:", msg.subject)
    print("발신자:",msg.from_)
    print("수신자:",msg.to)
    print("날짜:",msg.date)
    print("본문:",msg.text)
    print("Html 메세지:",msg.html)
    print("*"*50)
mailbox.logout
