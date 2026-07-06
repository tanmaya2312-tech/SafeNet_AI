import streamlit as st

def initialize_session():
    defaults = {
        "password_checks": 0,
        "url_scans": 0,
        "scam_checks": 0,
        "ai_queries": 0,
        "activity_log": []
    }

    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value