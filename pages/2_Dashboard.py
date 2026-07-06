import streamlit as st
from core.session import initialize_session
import matplotlib.pyplot as plt

initialize_session()

st.set_page_config(
    page_title="SafeNet AI Dashboard",
    page_icon="🛡️",
    layout="wide"
)


# ---------------- SESSION STATE ----------------

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

# ---------------- CSS ----------------

st.markdown("""
<style>

.stApp{
    background:#050505;
    color:white;
}

.block-container{
    padding-top:1rem;
    max-width:1200px;
}

/* Hide Streamlit */
#MainMenu{visibility:hidden;}
footer{visibility:hidden;}
header{visibility:hidden;}

/* Dashboard Title */

.title{
    text-align:center;
    font-size:48px;
    font-weight:700;
    color:white;
}

.subtitle{
    text-align:center;
    color:#A1A1AA;
    font-size:18px;
    margin-top:-10px;
    margin-bottom:30px;
}

/* Stats Cards */

.metric-box{

    background:#101010;

    border:1px solid #2b2b2b;

    border-radius:18px;

    padding:25px;

    text-align:center;

    transition:.3s;

}

.metric-box:hover{

    transform:translateY(-5px);

    border-color:#7C3AED;

    box-shadow:0 0 18px rgba(124,58,237,.45);

}

.metric-title{

    color:#BDBDBD;

    font-size:17px;

}

.metric-value{

    font-size:40px;

    color:#00D4FF;

    font-weight:bold;

}

/* Quick Action Cards */

.tool-card{

    background:#111111;

    border-radius:18px;

    border:1px solid #2f2f2f;

    padding:30px;

    text-align:center;

}

.tool-title{

    font-size:24px;

    font-weight:bold;

    color:white;

}

.tool-desc{

    color:#BDBDBD;

    font-size:15px;

}

div.stButton > button{

    width:100%;

    background:#7C3AED;

    color:white;

    border:none;

    border-radius:10px;

    padding:12px;

    font-weight:bold;

}

div.stButton > button:hover{

    background:#8B5CF6;

}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------

c1, c2, c3 = st.columns([1,2,1])

with c2:
    st.image("assets/data/logo.png", width=720)

st.markdown("<div class='title'>SafeNet AI Dashboard</div>", unsafe_allow_html=True)

st.markdown(
"<div class='subtitle'>AI Powered Cybersecurity Control Center</div>",
unsafe_allow_html=True)

st.divider()

# ---------------- SECURITY OVERVIEW ----------------

st.subheader("📊 Security Overview")

c1,c2,c3,c4=st.columns(4)

with c1:

    st.markdown(f"""

    <div class="metric-box">

    <div class="metric-title">Passwords Checked</div>

    <div class="metric-value">{st.session_state.password_checks}</div>

    </div>

    """,unsafe_allow_html=True)

with c2:

    st.markdown(f"""

    <div class="metric-box">

    <div class="metric-title">URLs Scanned</div>

    <div class="metric-value">{st.session_state.url_scans}</div>

    </div>

    """,unsafe_allow_html=True)

with c3:

    st.markdown(f"""

    <div class="metric-box">

    <div class="metric-title">Scams Detected</div>

    <div class="metric-value">{st.session_state.scam_checks}</div>

    </div>

    """,unsafe_allow_html=True)

with c4:

    st.markdown(f"""

    <div class="metric-box">

    <div class="metric-title">AI Queries</div>

    <div class="metric-value">{st.session_state.ai_queries}</div>

    </div>

    """,unsafe_allow_html=True)

st.divider()

# ---------------- QUICK ACTIONS ----------------

st.subheader("⚡ Quick Actions")

col1,col2=st.columns(2)

with col1:

    st.markdown("""
    <div class="tool-card">
    <div class="tool-title">🔐 Password Checker</div>
    <div class="tool-desc">
    Analyze password strength.
    </div>
    </div>
    """,unsafe_allow_html=True)

    if st.button("Open Password Checker"):

        st.switch_page("pages/3_Password.py")

    st.markdown("<br>",unsafe_allow_html=True)

    st.markdown("""
    <div class="tool-card">
    <div class="tool-title">📨 Scam Detector</div>
    <div class="tool-desc">
    Detect scam messages.
    </div>
    </div>
    """,unsafe_allow_html=True)

    if st.button("Open Scam Detector"):

        st.switch_page("pages/5_Scam_detector.py")   # change if you renamed the file

with col2:

    st.markdown("""
    <div class="tool-card">
    <div class="tool-title">🌐 URL Scanner</div>
    <div class="tool-desc">
    Scan suspicious websites.
    </div>
    </div>
    """,unsafe_allow_html=True)

    if st.button("Open URL Scanner"):

        st.switch_page("pages/4_URL_scanner.py")

    st.markdown("<br>",unsafe_allow_html=True)

    st.markdown("""
    <div class="tool-card">
    <div class="tool-title">🤖 AI Assistant</div>
    <div class="tool-desc">
    Ask cybersecurity questions.
    </div>
    </div>
    """,unsafe_allow_html=True)

    if st.button("Open AI Assistant"):

        st.switch_page("pages/6_Chatbot.py")
# ================================
# THREAT STATISTICS
# ================================


# ================================
# THREAT STATISTICS
# ================================

st.divider()

st.subheader("📈 Threat Statistics")

import matplotlib.pyplot as plt

# Collect only tools that have been used
labels = []
sizes = []

if st.session_state.password_checks > 0:
    labels.append("Password Checker")
    sizes.append(st.session_state.password_checks)

if st.session_state.url_scans > 0:
    labels.append("URL Scanner")
    sizes.append(st.session_state.url_scans)

if st.session_state.scam_checks > 0:
    labels.append("Scam Detector")
    sizes.append(st.session_state.scam_checks)

if st.session_state.ai_queries > 0:
    labels.append("AI Assistant")
    sizes.append(st.session_state.ai_queries)

# If no analysis has been performed
if not sizes:
    st.info("No analyses performed yet.")
else:

    fig, ax = plt.subplots(figsize=(7, 5), facecolor="#050505")

    ax.set_facecolor("#050505")

    wedges, texts, autotexts = ax.pie(
        sizes,
        autopct="%1.0f%%",
        startangle=90,
        wedgeprops=dict(width=0.40),
        pctdistance=0.75,
        textprops=dict(color="white", fontsize=11)
    )

    ax.legend(
        wedges,
        labels,
        title="Analysis Tools",
        loc="center left",
        bbox_to_anchor=(1, 0.5),
        fontsize=11,
        title_fontsize=12
    )

    ax.set_title(
        "Analysis Distribution",
        color="white",
        fontsize=18,
        pad=20
    )

    ax.axis("equal")

    st.pyplot(fig, use_container_width=True)
# ================================
# SECURITY SCORE
# ================================

st.divider()

st.subheader("🛡️ Overall Security Score")

total = (
    st.session_state.password_checks
    + st.session_state.url_scans
    + st.session_state.scam_checks
    + st.session_state.ai_queries
)

score = min(100, 60 + total * 2)

st.progress(score / 100)

st.markdown(
    f"""
    <h2 style='text-align:center;color:#00D4FF;'>
        {score}% Secure
    </h2>
    """,
    unsafe_allow_html=True,
)

# ================================
# ANALYSIS HISTORY
# ================================

st.divider()

st.subheader("🕒 Analysis History")

if st.session_state.activity_log:

    for item in reversed(st.session_state.activity_log):

        if isinstance(item, dict):

            with st.container(border=True):

                st.markdown(f"### 🛠 {item['tool']}")
                st.write(f"🕒 **Time:** {item['time']}")
                st.write(f"📊 **Status:** {item['status']}")
                st.write(f"⭐ **Score:** {item['score']}/100")

        else:
            st.info(item)

else:
    st.info("No analyses performed yet.")


# ================================
# CYBER TIP
# ================================

st.divider()

tips = [
    "Never reuse passwords across multiple websites.",
    "Enable Two-Factor Authentication whenever possible.",
    "Always verify suspicious URLs before clicking.",
    "Never share OTPs or banking credentials.",
    "Keep your software updated to avoid vulnerabilities."
]

import random

st.info("💡 Cyber Tip of the Day")

st.success(random.choice(tips))

# ================================
# FOOTER
# ================================

st.divider()

st.markdown(
"""
<div style="text-align:center;color:gray;padding:20px;">
SafeNet AI v1.0<br>
Built for HackHazards 2026 ❤️
</div>
""",
unsafe_allow_html=True,
)

