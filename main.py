import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png", width=600)

with col2:
    st.title("Jimmy Broski")
    content = """
    Jimmy Broski was just a boy, until he fell into a vat of radioactive waste. Now he's a boy with cancer. 
    """
    st.info(content)