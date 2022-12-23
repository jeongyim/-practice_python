
import smtplib
from account import*
from email.message import EmailMessage

msg=EmailMessage()
msg["Subject"] = "실습메일-이정임"
msg["From"]=EMAIL_ADDRESS
msg["To"]="phok710@gmail.com"
msg.set_content("엑셀 파일을 첨부해서 보내는 실습용 메일입니다")
with open("sample.xlsx","rb") as f:
    msg.add_attachment(f.read(),maintype="application",subtype="vnd.ms-excel",filename=f.name)
with smtplib.SMTP("smtp.gmail.com",587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
    smtp.send_message(msg)
