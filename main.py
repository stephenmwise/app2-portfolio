import streamlit as st
import pandas

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)


with col1:
    st.image("images/photo.png")

with col2:
    st.title("Stephen Wise")
    content = """
    Hi, I'm Stephen! I'm a Python programmer, and here's a portfolio showcasing my featured projects.
    I spent 10+ years as a digital marketer, designer, and web developer. I have worked at Apple Design-winning app studios,
    NASCAR's video game studio, Ecommerce sites, Devops agencies, and AI startups.
    In 2023 I decided to do a career change into focusing on Python development, learning Machine Learning, AI, Data Science, and Web App Development,
    which my design and marketing experience and perspective will enhance my future projects.
    """
    st.info(content)


row_additional_info = """Below, you'll find my recent featured apps I've created as a showcase of my projects.
                        My goal is to provide proof of my Python abilities and real-world work by sharing this publicly with you.
                        This portfolio page was also developed using Python with Streamlit.
                        I've provided the source code for each project with a link to GitHub."""
st.write(row_additional_info)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.link_button("Open web app", row["url"])
        st.write(f"[View Source Code on GitHub]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.link_button("Open web app", row["url"])
        st.write(f"[View Source Code on GitHub]({row['url']})")

