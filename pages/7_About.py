import streamlit as st

st.set_page_config(
    page_title="About SafeNet AI",
    page_icon="ℹ️",
    layout="wide"
)


# Logo
col1, col2, col3 = st.columns([1,2,1])

with col2:
    st.image("assets/data/logo.png", width=570)

st.title("ℹ️ About SafeNet AI")

st.markdown("""
## 🛡️ What is SafeNet AI?

SafeNet AI is an AI-powered cybersecurity platform designed to help users identify common online security threats before they become victims.

The platform combines multiple cybersecurity tools into one easy-to-use dashboard, making digital safety accessible for everyone.

---

## 🚀 Features

✅ Password Strength Checker

- Evaluates password strength
- Provides AI-powered security recommendations
- Downloadable PDF security reports

---

✅ URL Safety Scanner

- Detects suspicious and phishing websites
- Calculates website safety score
- Generates downloadable reports

---

✅ Scam Message Detector

- Analyzes SMS, Email, and WhatsApp messages
- Detects phishing and social engineering attempts
- Suggests protective actions

---

✅ AI Cybersecurity Assistant

- Answers cybersecurity-related questions
- Provides awareness and security guidance
- Supports downloadable AI conversation reports

---

## 📊 Dashboard

The dashboard provides:

- Security Overview
- Analysis History
- Threat Statistics
- Overall Security Score
- Cyber Tip of the Day

---

## 🛠️ Technologies Used

- Python
- Streamlit
- ReportLab
- Sarvam AI API
- HTML & CSS

---

## 🎯 Purpose

SafeNet AI was developed to improve cybersecurity awareness by providing intelligent tools that help users make safer decisions online.

---

## ❤️ Developed For

HackHazards 2026

SafeNet AI v1.0
""")

st.success("🛡️ Protect • Detect • Prevent")