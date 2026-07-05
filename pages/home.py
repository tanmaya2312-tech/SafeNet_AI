import streamlit as st
from pathlib import Path
import base64
st.sidebar.title("🛡 SafeNet AI")
st.sidebar.markdown("AI Cybersecurity System")

page = st.sidebar.radio("Navigate", ["Home", "Dashboard"])

BASE_DIR = Path(__file__).resolve().parent.parent

def get_base64(path):
    with open(path, "rb") as img:
        return base64.b64encode(img.read()).decode()

logo = get_base64(BASE_DIR / "assets" / "data" / "logo.png")

st.set_page_config(page_title="SafeNet AI", page_icon="🛡️", layout="wide")

# ---------- CSS ----------
st.markdown("""
<style>

.stApp{
    background-color:#050505;
    color:white;
}

.block-container{
    padding-top:2rem;
    max-width:1200px;
}

/* Hide Streamlit menu/footer */
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

/* Cards */
.card{
    background:#101010;
    border:1px solid #333;
    border-radius:18px;
    padding:30px;
    text-align:center;
    transition:0.3s;
    height:190px;
}

.card:hover{
    border:1px solid #8b5cf6;
    box-shadow:0px 0px 20px #8b5cf6;
    transform:translateY(-6px);
}

.card-title{
    font-size:28px;
    font-weight:bold;
    color:white;
}

.card-text{
    color:#cccccc;
    font-size:17px;
}

/* Button */
div.stButton > button{
    background:linear-gradient(90deg,#6d28d9,#2563eb);
    color:white;
    border:none;
    border-radius:10px;
    font-size:18px;
    font-weight:bold;
    padding:12px 28px;
}

div.stButton > button:hover{
    box-shadow:0 0 20px #7c3aed;
}
.stImage > img {
    display: block;
    margin-left: auto;
    margin-right: auto;
}

.block-container {
    padding-top: 0.5rem !important;
}
            

</style>
""", unsafe_allow_html=True)
st.markdown("""
<style>
body {
    background-color: #050505;
}

.block-container {
    padding-top: 1.5rem;
}

h1, h2, h3, p {
    color: white;
}
</style>
""", unsafe_allow_html=True)

# ---------- Logo ----------
st.markdown(f"""
<div style="text-align:center;">
    <img src="data:image/png;base64,{logo}" width="520">
</div>
""", unsafe_allow_html=True)
# ---------- Hero ----------
st.markdown("""
<h1 style='
text-align:center;
font-size:62px;
font-weight:800;
margin-bottom:0;
color:white;
'>
SafeNet AI
</h1>
""", unsafe_allow_html=True)

st.markdown("""
<h3 style='
text-align:center;
color:#9ca3af;
margin-top:5px;
'>
Protect • Detect • Prevent
</h3>
""", unsafe_allow_html=True)

st.markdown("""
<p style='
text-align:center;
font-size:20px;
color:#d1d5db;
max-width:900px;
margin:auto;
'>
Your AI-powered cybersecurity companion that protects users from
scams, phishing attacks and weak passwords using intelligent
security analysis.
</p>
""", unsafe_allow_html=True)

st.write("")

col1,col2,col3=st.columns([8,5,8])

with col2:
    if st.button("🚀 Launch Dashboard",use_container_width=True):
        st.switch_page("pages/dashboard.py")

# ---------- Features ----------
col1,col2,col3=st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
        <div class="card-title">🛡 Scam Detection</div><br>
        <div class="card-text">
        Analyze suspicious SMS, emails and phishing messages using AI.
        </div>
    </div>
    """,unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <div class="card-title">🌐 URL Scanner</div><br>
        <div class="card-text">
        Instantly verify suspicious websites before opening them.
        </div>
    </div>
    """,unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
        <div class="card-title">🔒 Password Checker</div><br>
        <div class="card-text">
        Check password strength and receive security recommendations.
        </div>
    </div>
    """,unsafe_allow_html=True)

# ---------- Why Section ----------
st.markdown("""
<h2 style='text-align:center;color:white;'>
Why SafeNet AI?
</h2>
""",unsafe_allow_html=True)

st.markdown("""
<p style='
text-align:center;
font-size:18px;
color:#cfcfcf;
max-width:950px;
margin:auto;
'>
SafeNet AI combines Artificial Intelligence with cybersecurity tools to
help users detect phishing websites, identify scam messages,
strengthen passwords, and receive real-time security guidance powered
by Sarvam AI.
</p>
""",unsafe_allow_html=True)

st.markdown("---")

st.markdown("""
<p style='text-align:center;color:gray;'>
🚀 Built for HackHazards 2026
<br><br>
Powered by Streamlit • Python • Sarvam AI
</p>
""",unsafe_allow_html=True)
