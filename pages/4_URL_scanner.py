from phishing_checker import check_url
from report_generator import generate_report
from datetime import datetime
import streamlit as st
from core.session import initialize_session

initialize_session()

# ---------- Load CSS ----------
def load_css():
    with open("assets/data/style.css", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()


# ---------- Initialize Session ----------
if "password_checks" not in st.session_state:
    st.session_state.password_checks = 0

if "url_scans" not in st.session_state:
    st.session_state.url_scans = 0

if "scam_checks" not in st.session_state:
    st.session_state.scam_checks = 0

if "ai_queries" not in st.session_state:
    st.session_state.ai_queries = 0

if "activity_log" not in st.session_state:
    st.session_state.activity_log = []

    st.title("🌐 AI Website Safety Scanner")

url = st.text_input("Enter Website URL")

if url:

    score, status, issues = check_url(url)

    st.session_state.url_scans += 1

    st.session_state.activity_log.append({
        "time": datetime.now().strftime("%d-%m-%Y %I:%M %p"),
        "tool": "URL Scanner",
        "status": status,
        "score": score
    })

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

    # Generate PDF
    pdf = generate_report(
        "Website URL Analysis",
        score,
        status,
        issues
    )

    # Download button
    st.download_button(
        "📄 Download URL Report",
        data=pdf,
        file_name="URL_Report.pdf",
        mime="application/pdf",
        use_container_width=True
    )