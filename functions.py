import os
import re
import smtplib
import ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "dr.maziarz@gmail.com"
    # password = os.getenv("PASSWORD")

    receiver = "dr.maziarz@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)


def validate_email(user_email):
    email_regex = r"[^@]+@[^@]+\.[^@]+"
    return re.match(email_regex, user_email)
