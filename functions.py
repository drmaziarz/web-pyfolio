import os
import re
import smtplib
import ssl
import streamlit as st

# from dotenv import load_dotenv
#
#
# def configure():
#     load_dotenv()
#
#
# configure()


def send_email(message):
    """Send mail to box hosted on gmail.com"""
    host = "smtp.gmail.com"
    port = 465

    # To run app locally, uncomment below lines and set environmental variable, and comment / delete lines 26-28
    # username = os.getenv("username")
    # receiver = os.getenv("receiver")
    # password = os.getenv("PASSWORD")

    password = st.secrets["password"]
    username = st.secrets["username"]
    receiver = st.secrets["receiver"]

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)


def validate_email(user_email):
    """Check if the user email is valid """
    email_regex = r"[^@]+@[^@]+\.[^@]+"
    return re.match(email_regex, user_email)
