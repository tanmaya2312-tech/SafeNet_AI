import streamlit as st
from core.session import initialize_session

initialize_session()

st.set_page_config(
    page_title="SafeNet AI",
    page_icon="🛡️",
    layout="wide"
)

st.switch_page("pages/1_Home.py")