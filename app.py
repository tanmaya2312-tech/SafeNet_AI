import streamlit as st
from core.session import initialize_session

initialize_session()

st.set_page_config(
    page_title="SafeNet AI",
    page_icon="🛡️",
    layout="wide"
)

st.switch_page("pages/1_home.py")
st.subheader("AI Powered Cybersecurity Platform")

st.write("""
Welcome to **SafeNet AI**.

Use the **sidebar** to navigate through the application:

- 🏠 Home
- 📊 Dashboard
- 🔐 Password Checker
- 🌐 URL Scanner
- 📩 Scam Detector
- 🤖 AI Assistant
- ℹ️ About
""")

st.success("Select a page from the sidebar to get started.")