import streamlit as st

st.set_page_config(layout="wide")
col1, col2 = st.comumns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Stephen Wise")
    content = """
    Hi, I'm Stephen! I'm a Python programmer, and here's a portfolio showcasing my featured projects.
    I spent 10+ years as a digital marketer, designer, and web developer, and in 2023 I decided to do a career change
    into focusing on Python development, learning machine learning, data science, and web app development.
    """
    st.info(content)