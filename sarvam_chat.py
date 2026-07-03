import os
from dotenv import load_dotenv
from sarvamai import SarvamAI

# Load .env file
load_dotenv()

# Get API key
api_key = os.getenv("SARVAM_API_KEY")

if not api_key:
    raise ValueError("SARVAM_API_KEY not found in .env file")

client = SarvamAI(
    api_subscription_key=api_key
)

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