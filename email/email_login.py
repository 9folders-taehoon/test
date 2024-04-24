import smtplib
import os
import ssl

# 이메일 메시지에 다양한 형식을 중첩하여 담기 위한 객체
from email.mime.multipart import MIMEMultipart
from email.message import EmailMessage

# 이메일 메시지를 이진 데이터로 바꿔주는 인코더
from email import encoders

from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio


# 위의 모든 객체들을 생성할 수 있는 기본 객체
from email.mime.base import MIMEBase

# MIMEBase(_maintype, _subtype)
from datetime import datetime

now = datetime.today()
file_date = now.strftime("%Y-%m-%d")

smtp_info = dict(
    {
        "smtp_server": "smtp.naver.com",
        "smtp_user_id": "djwrktls@naver.com",
        "smtp_user_pw": "rlaxognsWkd1234",
        "smtp_port": 587,
    }
)

msg_dict = {
    "text": {
        "maintype": "text",
        "subtype": "plain",
        "filename": "res/email_sending/test.txt",
    },  # 텍스트 첨부파일
    "image": {
        "maintype": "image",
        "subtype": "jpg",
        "filename": "res/email_sending/test.jpg",
    },  # 이미지 첨부파일
    "audio": {
        "maintype": "audio",
        "subtype": "mp3",
        "filename": "res/email_sending/test.mp3",
    },  # 오디오 첨부파일
    "video": {
        "maintype": "video",
        "subtype": "mp4",
        "filename": "res/email_sending/test.mp4",
    },  # 비디오 첨부파일
    "application": {
        "maintype": "application",
        "subtype": "octect-stream",
        "filename": "res/email_sending/test.pdf",
    },  # 그외 첨부파일
}

context = ssl.create_default_context()


def send_email(smtp_info, msg):
    try:
        server = smtplib.SMTP(
            host=smtp_info["smtp_server"], port=smtp_info["smtp_port"]
        )
        server.starttls(context=context)
        print("starttls clear")
        server.login(smtp_info["smtp_user_id"], smtp_info["smtp_user_pw"])
        print("login clear")
        server.set_debuglevel(1)
        a = server.send_message(msg)
        print(a)
    except Exception as e:
        with open("/Users/taehoon/hello.txt", "w") as f:
            f.write(str(e))


def make_multimsg(msg_dict):
    multi = MIMEMultipart(_subtype="mixed")

    for key, value in msg_dict.items():
        # 각 타입에 적절한 MIMExxx() 함수를 호출하여 msg 객체를 생성한다.
        if key == "text":
            with open(value["filename"], encoding="utf-8") as fp:
                msg = MIMEText(fp.read(), _subtype=value["subtype"])
        elif key == "image":
            with open(value["filename"], "rb") as fp:
                msg = MIMEImage(fp.read(), _subtype=value["subtype"])
        else:
            with open(value["filename"], "rb") as fp:
                msg = MIMEBase(value["maintype"], _subtype=value["subtype"])
                msg.set_payload(fp.read())
                encoders.encode_base64(msg)

        # 파일 이름을 첨부파일 제목으로 추가
        msg.add_header(
            "Content-Disposition",
            "attachment",
            filename=os.path.basename(value["filename"]),
        )

        # 첨부 파일 추가
        multi.attach(msg)
    return multi


title = f"NSE Sync 테스트용 메일 입니다. {now}"
content = "메일 입니다"
sender = smtp_info["smtp_user_id"]
receiver = [
    "bruce.wayne@okestra.io",
    "djwrktls@naver.com",
]
msg = EmailMessage()
msg.set_content(content)
msg["Subject"] = title
msg["From"] = sender
msg["To"] = ", ".join(receiver)

send_email(smtp_info, msg)
