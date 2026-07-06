import streamlit as st
from password_checker import check_password_strength
from report_generator import generate_report
from datetime import datetime


# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Password Checker",
    page_icon="🔐",
    layout="wide"
)


# ---------------- LOAD CSS ----------------
def load_css():
    with open("assets/data/style.css", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()


# ---------------- SESSION ----------------
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


# ---------------- HEADER ----------------

st.markdown(
    "<p class='hero-subtitle'>AI Powered Password Security Analysis</p>",
    unsafe_allow_html=True
)
st.divider()

# ---------------- INPUT ----------------

st.markdown("### 🔐 Enter Password")

password = st.text_input(
    "",
    type="password",
    placeholder="Enter a secure password...",
    label_visibility="collapsed"
)

analyze = st.button(
    "🚀 Analyze Password",
    use_container_width=True,
    type="primary"
)

# ---------------- RESULT ----------------

if analyze and password:

    score, strength, suggestions = check_password_strength(password)

    # Update session
    from datetime import datetime

    st.session_state.password_checks += 1

    st.session_state.activity_log.append({
    "time": datetime.now().strftime("%d-%m-%Y %I:%M %p"),
    "tool": "Password Checker",
    "status": strength,
    "score": score
})

    # Generate PDF
    pdf = generate_report(
        "Password Analysis",
        score,
        strength,
        suggestions
    )

    st.subheader("📊 Security Analysis")

    st.metric("Security Score", f"{score}/100")

    st.progress(score / 100)

    if strength == "Strong":
        st.success("🟢 STRONG PASSWORD")

    elif strength == "Medium":
        st.warning("🟡 MEDIUM PASSWORD")

    else:
        st.error("🔴 WEAK PASSWORD")

    st.subheader("Recommendations")

    if suggestions:
        for item in suggestions:
            st.write(f"⚠️ {item}")
    else:
        st.success("Excellent! Your password is very strong.")

    st.download_button(
        "📄 Download Password Report",
        data=pdf,
        file_name="Password_Report.pdf",
        mime="application/pdf",
        use_container_width=True
    )

    st.subheader("🤖 AI Security Advisor")

    if strength == "Strong":
        st.success("""
Your password is strong.

• Enable Two-Factor Authentication (2FA)

• Use a password manager

• Avoid reusing passwords
""")

    elif strength == "Medium":
        st.warning("""
Your password is decent but can be improved.

• Add more symbols

• Increase the length

• Avoid common words
""")

    else:
        st.error("""
This password is vulnerable.

• Add uppercase letters

• Add lowercase letters

• Add numbers

• Add special characters

• Use at least 12 characters
""")

else:
    st.info("👆 Enter a password and click **Analyze Password**.")