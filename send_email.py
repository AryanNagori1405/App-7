import smtplib, ssl
import os


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = 'aryanadu0714@gmail.com'
    password = os.getenv("Password_App-7[API]")

    receiver = 'aryanadu0714@gmail.com'
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)


# Pythonanywhere by ANACONDA