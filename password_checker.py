import re
import streamlit as st

def check_password_strength(password):
    score = 0
    suggestions = []

    # Length
    if len(password) >= 8:
        score += 20
    else:
        suggestions.append("Password should be at least 8 characters long.")

    # Uppercase
    if re.search(r"[A-Z]", password):
        score += 20
    else:
        suggestions.append("Add at least one uppercase letter.")

    # Lowercase
    if re.search(r"[a-z]", password):
        score += 20
    else:
        suggestions.append("Add at least one lowercase letter.")

    # Numbers
    if re.search(r"\d", password):
        score += 20
    else:
        suggestions.append("Add at least one number.")

    # Special Characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 20
    else:
        suggestions.append("Add at least one special character.")

    # Strength Label
    if score <= 40:
        strength = "Weak"
    elif score <= 80:
        strength = "Medium"
    else:
        strength = "Strong"

    return score, strength, suggestions
