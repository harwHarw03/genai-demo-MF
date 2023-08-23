import streamlit as st

def app():
    st.image("logo.png", width=100)
    st.title("About Page")
    st.write("We created this app to provide a user-friendly solution for summarizing legal documents and generating new ones.")
    st.write("Our goal is to make legal document analysis and generation more efficient and accessible.")

app()