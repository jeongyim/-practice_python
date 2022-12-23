import smtplib
from account import*
from email.message import EmailMessage

msg=EmailMessage()
msg["Subject"] = "파일첨부 메일입니다."
msg["From"]=EMAIL_ADDRESS
msg["To"]=EMAIL_ADDRESS
msg.set_content("첨부파일이 있습니다.\n다운로드 하세요")
#첨부파일 등록,앞에서 저장했던 pdf 파일을 보내 보도록 하자
with open("파이썬 테스트 입니다.pdf","rb") as f:
#MIME Type 전체목록-구글검색해서 maintype와subtype찾기
    msg.add_attachment(f.read(),maintype="application",subtype="pdf",filename=f.name)
with smtplib.SMTP("smtp.gmail.com",587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
    smtp.send_message(msg)
