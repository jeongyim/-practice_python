import smtplib
from account import*
from email.message import EmailMessage

msg=EmailMessage()
msg["Subject"] = "파일첨부 메일입니다."
msg["From"] = EMAIL_ADDRESS
msg["TO"] = EMAIL_ADDRESS
msg.set_content("첨부파일이 있습니다. \n 다운로드하세요")
#첨부파일 등록,앞에서 이용했던 이미지 파일을 보내 보도록 하자

with open("img1.png","rb") as f:
    msg.add_attachment(f.read(),maintype="image",subtype="png",filename=f.name)
#MIME Type-구글검색해서 설명
with smtplib.SMTP("smtp.gmail.com",587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
    smtp.send_message(msg)

