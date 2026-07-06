import streamlit as st
from datetime import datetime
from password_checker import check_password_strength
from report_generator import generate_report

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

# ---------------- HEADER ----------------
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.image("assets/data/logo.png", width=180)

st.markdown(
    "<h1 class='hero-title'>🔐 Password Checker</h1>",
    unsafe_allow_html=True
)

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
if analyze:

    if not password:
        st.warning("Please enter a password.")
        st.stop()

    score, strength, suggestions = check_password_strength(password)

    # Update Dashboard Statistics
    st.session_state.password_checks += 1

    # Save History
    st.session_state.activity_log.append({
        "time": datetime.now().strftime("%d-%m-%Y %I:%M %p"),
        "tool": "Password Checker",
        "status": strength,
        "score": score
    })

    # ---------------- Security Analysis ----------------
    st.subheader("📊 Security Analysis")

    st.metric("Security Score", f"{score}/100")

    st.progress(score / 100)

    if strength == "Strong":
        st.success("🟢 STRONG PASSWORD")
    elif strength == "Medium":
        st.warning("🟡 MEDIUM PASSWORD")
    else:
        st.error("🔴 WEAK PASSWORD")

    # ---------------- Recommendations ----------------
    st.subheader("Recommendations")

    if suggestions:
        for item in suggestions:
            st.write(f"⚠️ {item}")
    else:
        st.success("Excellent! Your password is very strong.")

    # ---------------- AI Security Advisor ----------------
    st.subheader("🤖 AI Security Advisor")

    if strength == "Strong":
        st.success("""
Your password is strong.

• Enable Two-Factor Authentication (2FA)

• Use a password manager

• Avoid reusing passwords.
""")

    elif strength == "Medium":
        st.warning("""
Your password is decent but can be improved.

• Add more symbols.

• Increase the length.

• Avoid common words.
""")

    else:
        st.error("""
This password is vulnerable.

• Add uppercase letters.

• Add lowercase letters.

• Add numbers.

• Add special characters.

• Use at least 12 characters.
""")

    # ---------------- PDF Report ----------------
    pdf = generate_report(
        "Password Analysis",
        score,
        strength,
        suggestions
    )

    st.download_button(
        "📄 Download Password Report",
        data=pdf,
        file_name="Password_Report.pdf",
        mime="application/pdf",
        use_container_width=True
    )

else:
    st.info("👆 Enter a password and click **Analyze Password**.")