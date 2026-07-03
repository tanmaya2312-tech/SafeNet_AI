import streamlit as st
from password_checker import check_password_strength
from phishing_checker import check_url
from scam_detector import analyze_message

st.set_page_config(
    page_title="SafeNet AI",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ SafeNet AI")
st.subheader("Your Personal AI Cybersecurity Assistant")

st.divider()

st.header("🔐 Password Strength Analyzer")

password = st.text_input(
    "Enter your password",
    type="password"
)

if password:

    score, strength, suggestions = check_password_strength(password)

    # Display password strength
    if strength == "Weak":
        st.markdown(
            "<h3 style='color:#ff4b4b;'>🔴 Strength: Weak</h3>",
            unsafe_allow_html=True
        )

    elif strength == "Medium":
        st.markdown(
            "<h3 style='color:#FFA500;'>🟡 Strength: Medium</h3>",
            unsafe_allow_html=True
        )

    else:
        st.markdown(
            "<h3 style='color:#00C853;'>🟢 Strength: Strong</h3>",
            unsafe_allow_html=True
        )

    # Display score
    st.metric(
        label="Password Score",
        value=f"{score}/100"
    )

    st.progress(score / 100)

    # Suggestions
    if suggestions:
        st.warning("Suggestions to improve your password:")
        for item in suggestions:
            st.write(f"⚠️ {item}")
    else:
        st.success("Excellent! Your password is very strong.")

# Sidebar
with st.sidebar:
    st.title("🛡️ SafeNet AI")
    st.write("Cybersecurity Toolkit")
st.divider()

st.header("🌐 AI Website Safety Scanner")

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
        st.warning("Issues Found:")
        for issue in issues:
            st.write(f"⚠️ {issue}")
    else:
        st.success("No issues detected.")
st.divider()

st.header("📧 AI Scam Message Detector")

message = st.text_area(
    "Paste an SMS, Email or WhatsApp message"
)

if message:

    score, level, reasons = analyze_message(message)

    if level == "High Risk":
        st.error("🔴 High Risk Scam")
        st.markdown(
    """
    <h3 style='color:#ff4b4b;'>
    🚨 HIGH RISK PHISHING DETECTED
    </h3>
    """,
    unsafe_allow_html=True
)

    elif level == "Medium Risk":
        st.markdown(
    """
    <h3 style='color:#FFA500;'>
    ⚠️ MEDIUM RISK
    </h3>
    """,
    unsafe_allow_html=True
)

    else:
       st.markdown(
    """
    <h3 style='color:#00C853;'>
    ✅ LOW RISK
    </h3>
    """,
    unsafe_allow_html=True
)

    st.metric("Safety Score", f"{score}/100")
    

    st.progress(score / 100)

    st.subheader("Analysis")

    if reasons:
        for reason in reasons:
            st.write(f"⚠️ {reason}")

    st.subheader("Recommendation")

    if level == "High Risk":
        st.error("""🚫 Do NOT click any links.

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
