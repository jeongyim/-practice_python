import smtplib #mail을 사용하기 위해 임포트
from account import * #우리가 저장해 놓은 EMAIL주소와 앱 비밀번호를 사용하기위해 임포트

with smtplib.SMTP("smtp.gmail.com",587) as smtp: #587은 구글 포트 번호
    smtp.ehlo() #연결이 잘 수립되는지 확인
    smtp.starttls() #모든 내용이 암호화 되어 전송
    smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD) #로그인

    subject = " test mail"#메일 제목(한글사용시 에러 남)

    body = "mail body"
    msg=f"Subject: {subject}\{body}" #메세지는 이와 같은 정해진형식으로 작성한다..  
   #그래야 이부분이 제목이구나, 본문이구나 하고 구분을 한다. 
   #smtp.sendmail(보내는 사람주소, 받는 사람 주소,정해진형식의 메세지)
    smtp.sendmail(EMAIL_ADDRESS,EMAIL_ADDRESS,msg)

