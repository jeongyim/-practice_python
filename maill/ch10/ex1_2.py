from account import *
from imap_tools import MailBox 
sender_list =[]
with MailBox("imap.gmail.com", 993).login(EMAIL_ADDRESS,EMAIL_PASSWORD,\
    initial_folder="INBOX") as mailbox:
    i=0 
    for msg in mailbox.fetch('(SENTSINCE 19-Dec-2022)'):
        if "상품권신청_" in msg.subject :
            subject, name = msg.subject.split("_")
            i=i+1
            print("순번 :{} 이름:{} 전화번호" .format(i, name))
