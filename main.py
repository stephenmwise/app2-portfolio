import streamlit as st

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)
row_additional_info = st.columns(1)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Stephen Wise")
    content = """
    Hi, I'm Stephen! I'm a Python programmer, and here's a portfolio showcasing my featured projects.
    I spent 10+ years as a digital marketer, designer, and web developerIn. I have worked at Apple Design-winning app studios,
    NASCAR's video game studio, Ecommerce sites, Devops agencies, and AI startups.
    In 2023 I decided to do a career change into focusing on Python development, learning machine learning, data science, and web app development.
    """
    st.info(content)


with row_additional_info:
    textwrap("Below, you'll find my recent featured apps I've created as a showcase of my projects.")