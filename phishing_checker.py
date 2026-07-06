from urllib.parse import urlparse
import streamlit as st

def check_url(url):
    score = 0
    issues = []

    # Check HTTPS
    if url.startswith("https://"):
        score += 30
    else:
        issues.append("Website is not using HTTPS.")

    # Suspicious keywords
    suspicious_words = [
        "login",
        "verify",
        "bank",
        "secure",
        "update",
        "free",
        "gift",
        "win",
        "bonus",
        "paypal"
    ]

    url_lower = url.lower()

    for word in suspicious_words:
        if word in url_lower:
            score -= 10
            issues.append(f"Suspicious keyword found: {word}")

    # URL format
    parsed = urlparse(url)

    if parsed.scheme and parsed.netloc:
        score += 30
    else:
        issues.append("Invalid URL format.")

    # Length check
    if len(url) < 60:
        score += 20
    else:
        issues.append("URL is unusually long.")

    # Final score
    score = max(0, min(score, 100))

    # Risk level
    if score >= 70:
        status = "Safe"
    elif score >= 40:
        status = "Suspicious"
    else:
        status = "Dangerous"

    return score, status, issues
