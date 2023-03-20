import streamlit as st

from functions import send_email, validate_email

st.set_page_config(layout="wide",
                   page_title='PyFolio | Contact me',
                   page_icon='✉',
                   menu_items={
                       'Get Help': 'mailto:dr.maziarz@gmail.com',
                       'Report a bug': 'mailto:dr.maziarz@gmail.com',
                       'About': None
                   })

st.title("Contact me")

with st.form(key="email_forms"):
    user_email = st.text_input("Your email address")
    raw_message = st.text_area("Your message").encode()
    message = f"""\
Subject: PYFOLIO: New email from {user_email}

From: {user_email}
{raw_message}"""
    button = st.form_submit_button("Submit")
    if button:
        if validate_email(user_email):
            if raw_message == '':
                st.warning("Please, enter your message!")
            else:
                send_email(message)
                st.success("Your email was sent successfully")
        else:
            st.error("Please enter a valid email address.")
