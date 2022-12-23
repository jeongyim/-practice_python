from imap_tools import MailBox
from account import*
mailbox = MailBox("imap.gmail.com",993)
mailbox.login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX")

for msg in mailbox.fetch(limit=1,reverse=True):
    print("제목",msg.subject)
    for att in msg.attachments: #첨부파일들 중에서 하나씩 가져와서 att에 넣는다.
        print("첨부파일 이름", att.filename)
        print("타입", att.content_type)
        print("크기", att.size)
        #파일 다운로드 –파일이름을 download_첨부파일이름 으로 다운로드 한다.
        with open("download_"+att.filename, "wb") as f:
            f.write(att.payload) #payload 로 첨부파일(att)에 있는 내용을 가져와서 f에 쓴다.
            print("첨부파일 {}다운로드 완료".format(att.filename))
         #print("*"*50)	
mailbox.logout
