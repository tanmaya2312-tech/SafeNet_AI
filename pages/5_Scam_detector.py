import streamlit as st
from scam_detector_engine import analyze_message
from report_generator import generate_report
from datetime import datetime
from core.session import initialize_session

initialize_session()
st.set_page_config(
    page_title="Scam Detector",
    page_icon="📩",
    layout="wide"
)


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

st.title("📩 AI Scam Message Detector")

message = st.text_area(
    "Paste an SMS, Email or WhatsApp message"
)

if message:

    score, level, reasons = analyze_message(message)
    st.session_state.scam_checks += 1

    st.session_state.activity_log.append({
    "time": datetime.now().strftime("%d-%m-%Y %I:%M %p"),
    "tool": "Scam Detector",
    "status": level,
    "score": score
})


    if level == "High Risk":
        st.error("🚨 HIGH RISK PHISHING DETECTED")

    elif level == "Medium Risk":
        st.warning("⚠️ MEDIUM RISK")

    else:
        st.success("✅ LOW RISK")

    st.metric("Safety Score", f"{score}/100")
    st.progress(score / 100)

    st.subheader("Analysis")

    if reasons:
        for reason in reasons:
            st.write(f"⚠️ {reason}")

    st.subheader("Recommendation")

    if level == "High Risk":
        st.error("""
🚫 Do NOT click any links.

🚫 Never share OTP or Password.

☎ Contact the official company directly.

🛡 Delete the message if unsure.
""")

    elif level == "Medium Risk":
        st.warning("""
⚠ Verify the sender.

🔍 Check the website URL.

📞 Contact customer care before responding.
""")

    pdf = generate_report(
    "Scam Message Analysis",
    score,
    level,
    reasons
)

    st.download_button(
    "📄 Download Scam Report",
    data=pdf,
    file_name="Scam_Report.pdf",
    mime="application/pdf",
    use_container_width=True
)