import streamlit as st
def analyze_message(message):

    score = 100
    reasons = []

    message = message.lower()

    suspicious_words = [
        "urgent",
        "verify",
        "login",
        "bank",
        "account",
        "blocked",
        "click",
        "otp",
        "password",
        "gift",
        "free",
        "winner",
        "prize",
        "claim",
        "limited time"
    ]

    for word in suspicious_words:
        if word in message:
            score -= 8
            reasons.append(f"Suspicious keyword detected: {word}")

    if "http://" in message:
        score -= 20
        reasons.append("Unsafe HTTP link detected.")

    if "https://" in message:
        score -= 10
        reasons.append("Contains a clickable website link.")

    if len(message) < 20:
        score -= 10
        reasons.append("Message is unusually short.")

    score = max(0, min(score, 100))

    if score >= 70:
        level = "Low Risk"
    elif score >= 40:
        level = "Medium Risk"
    else:
        level = "High Risk"

    return score, level, reasons
high_risk_words = ["otp", "password", "bank", "urgent", "login", "verify account"]
medium_risk_words = ["click", "update", "confirm", "account", "limited"]
low_risk_words = ["offer", "prize", "win"]
