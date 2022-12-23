import smtplib
from account import*
from email.message import EmailMessage
from random import *
names =["이름1","이름2","이름3","이름4","이름5","이름6"]
with smtplib.SMTP("smtp.gmail.com",587) as smtp:
     smtp.ehlo()
     smtp.starttls()
     smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD )
     for name in names:
        msg=EmailMessage()
        msg["Subject"]="상품권신청_"+name
        msg["From"]=EMAIL_ADDRESS
        msg["To"]=EMAIL_ADDRESS
        content=name+":"+str(randint(1111,9999))
        msg.set_content(content)
        smtp.send_message(msg)
        print(name+"에게 메일 발송 완료")
