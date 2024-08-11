import smtplib, ssl
import os

def send_email(message):
    host = "smpt.gmail.com"
    port = 465

    username = "stephenwise42@gmail.com"
    password = os.getenv("PASSWORD")

    receiver = "stephenwise42@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

