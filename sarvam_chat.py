import os
import streamlit as st
from dotenv import load_dotenv
from sarvamai import SarvamAI

load_dotenv()

api_key = st.secrets.get("SARVAM_API_KEY") or os.getenv("SARVAM_API_KEY")

if not api_key:
    raise ValueError("SARVAM_API_KEY not found")

try:
    client = SarvamAI(api_subscription_key=api_key)
except Exception as e:
    raise RuntimeError(f"Failed to initialize SarvamAI client: {e}")

def ask_ai(question):
    system_prompt = """
You are SafeNet AI, a cybersecurity assistant.

Answer ONLY cybersecurity-related questions.
Keep answers simple, practical, and beginner-friendly.
"""

    response = client.chat.completions(
        model="sarvam-105b",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": question},
        ],
    )

    return response.choices[0].message.content
st.write("API Key Loaded:", bool(api_key))
st.write("Key Prefix:", api_key[:8] + "...")