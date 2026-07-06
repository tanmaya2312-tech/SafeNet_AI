import streamlit as st

def hide_sidebar():
    with open("assets/data/hide_sidebar.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)