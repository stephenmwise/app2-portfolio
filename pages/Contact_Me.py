import streamlit as st
from send_email import send_email
st.set_page_config("Stephen Wise | Portfolio - Contact")
st.header("Contact Me")

with st.form(key="contact_form", border=True):
    user_email = st.text_input("Your email address:")
    raw_message = st.text_area("Write your message:")
    message = f"""
    Subject: New email From {user_email}
    From: {user_email}
    {raw_message}
    """

    button = st.form_submit_button(label="Submit")
    if button:
        send_email(message)
        st.info("Your email was successfully sent.")
