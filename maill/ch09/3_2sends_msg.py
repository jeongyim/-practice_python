#3_2sends_msg.py
import smtplib
from account import*
from email.message import EmailMessage

msg=EmailMessage()
msg["subject"] = "여러 곳 발송 메일입니다."#제목
msg["From"]=EMAIL_ADDRESS#보내는 사람
#방법1:받는사람 주소부분에 본인이 확인할수 있는 여러 주소를 적으면 된다. 
#msg["To"] = "leejungyim3349@gmail.com","wjddla3349@naver.com"
#방법 2: 받는 사람 주소를 리스트로 작성하여 조인하여 넣으면 된다. 
address_list=["leejungyim3349@gmail.com","wjddla3349@naver.com"]
msg["To"]=", ".join(address_list) #리스트에 있는 값들을 합치는데 “, ”로 구분하겠다.
msg.set_content("테스트 본문입니다. ")#본문

with smtplib.SMTP("smtp.gmail.com",587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
    smtp.send_message(msg)
