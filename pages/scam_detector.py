import streamlit as st
from scam_detector import analyze_message

st.set_page_config(
    page_title="Scam Detector",
    page_icon="📩",
    layout="wide"
)

st.title("📩 AI Scam Message Detector")

message = st.text_area(
    "Paste an SMS, Email or WhatsApp message"
)

if message:

    score, level, reasons = analyze_message(message)

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

    else:
        st.success("""
✅ No major phishing signs detected.

🔐 Continue using safe browsing practices.
""")