import smtplib
import ssl
import os

def send_email(message, receiver='adamtemplin92@gmail.com'):

    host = 'smtp.gmail.com'
    port = 465

    username = 'adamtemplin92@gmail.com'
    password = os.getenv('PASSWORD')

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
