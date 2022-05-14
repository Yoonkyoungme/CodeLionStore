# 메일보내기
import smtplib
from email.message import EmailMessage      # 이메일 내용을 MINE 형태로 전환
import re

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465

def sendEmail(addr):
    reg = "^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$"
    if bool(re.match(reg,addr)):
        smtp.send_message(message)
        print("정상적으로 메일이 발송되었습니다.")
    else:
        print("유효한 이메일 주소가 아닙니다.")


message = EmailMessage()
message.set_content("메일을 보냅니다.")

message["Subject"] = "메일보내기"
message["From"] = "gmail 주소"      # 메일주소 입력    
message["To"] = "gmail 주소"        # 메일주소 입력


smtp = smtplib.SMTP_SSL(SMTP_SERVER,SMTP_PORT)
smtp.login("gmail주소","비밀번호")      # 메일주소, 비밀번호 입력
smtp.send_message(message)

sendEmail("gmail 주소")     # 메일주소 입력
smtp.quit()

