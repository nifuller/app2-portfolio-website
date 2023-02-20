import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)
col3 = st.container()

with col1:
    st.image("images/photo.png", width=600)

with col2:
    st.title("Jimmy Broski")
    content = """
    Jimmy Broski was just a boy, until he fell into a vat of radioactive waste. Now he's a boy with cancer. 
    """
    st.info(content)


content2 = """
Here are some python app I have developed. Contact me... or don't... I don't care. 
"""
st.info(content2)

col3, col4 = st.columns(2)

df = pandas.read_csv("data.csv", sep=";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
