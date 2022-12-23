#1_1testSendmail.py
import smtplib
from account import*
from email.message import EmailMessage
from random import *
names =["유재석","송지효","김종국","하하","전소민","지석진"]
with smtplib.SMTP("smtp.gmail.com",587) as smtp:
     smtp.ehlo()
     smtp.starttls()
     smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD )
     for name in names:
        msg=EmailMessage()
        msg["Subject"]="실습메일2-"+name
        msg["From"]=EMAIL_ADDRESS
        msg["To"]=EMAIL_ADDRESS
        content=name+":"+str(randint(1111,9999))#본문내용 작성
        msg.set_content(content)
        with open("sample.xlsx","rb") as f:#엑셀파일 첨부
            msg.add_attachment(f.read(),maintype="applicaion",subtype="oct-stream",\
                filename=f.name)
        smtp.send_message(msg)
        print(name+"으로부터 메일 도착")
