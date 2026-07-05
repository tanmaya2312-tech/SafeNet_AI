import streamlit as st
from phishing_checker import check_url

st.set_page_config(
    page_title="URL Scanner",
    page_icon="🌐",
    layout="wide"
)

st.title("🌐 AI Website Safety Scanner")

url = st.text_input("Enter Website URL")

if url:

    score, status, issues = check_url(url)

    if status == "Safe":
        st.success("🟢 Safe Website")

    elif status == "Suspicious":
        st.warning("🟡 Suspicious Website")

    else:
        st.error("🔴 Dangerous Website")

    st.metric("Safety Score", f"{score}/100")

    risk = 100 - score

    st.metric("Risk Percentage", f"{risk}%")

    st.progress(score / 100)

    if issues:
        st.subheader("Issues Found")
        for issue in issues:
            st.write("⚠️", issue)
    else:
        st.success("No issues detected.")