#3_1send_msg.py
import smtplib
from account import*
#한글사용가능, 정해진 메시지 형태로 보내지 않아도 되게 아래를 임포트
from email.message import EmailMessage

msg=EmailMessage() #객체생성
msg["subject"] = "테스트 메일입니다."#제목
msg["From"]=EMAIL_ADDRESS#보내는 사람
#아래는 강사 메일 주소임으로 본인이 확인할수 있는 메일 주소로 보내고 확인합니다. 
msg["To"] = EMAIL_ADDRESS # 수신 메일 주소 :phok710@gmail.com과 같이 보내고 싶은 주소를 직접 적어도 됌
msg.set_content("테스트 본문입니다. ")#본문

with smtplib.SMTP("smtp.gmail.com",587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
    smtp.send_message(msg)
