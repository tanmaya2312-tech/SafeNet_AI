import os
from dotenv import load_dotenv
from sarvamai import SarvamAI

# Load .env file
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

api_key = st.secrets.get("SARVAM_API_KEY") or os.getenv("SARVAM_API_KEY")

if not api_key:
    raise ValueError("SARVAM_API_KEY not found")

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