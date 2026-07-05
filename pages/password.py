import streamlit as st
from password_checker import check_password_strength

st.set_page_config(
    page_title="Password Checker",
    page_icon="🔐",
    layout="wide"
)

st.title("🔐 Password Strength Checker")

password = st.text_input(
    "Enter your password",
    type="password"
)

if password:

    score, strength, suggestions = check_password_strength(password)

    if strength == "Weak":
        st.error("🔴 Weak Password")

    elif strength == "Medium":
        st.warning("🟡 Medium Password")

    else:
        st.success("🟢 Strong Password")

    st.metric("Password Score", f"{score}/100")

    st.progress(score / 100)

    if suggestions:
        st.subheader("Suggestions")
        for item in suggestions:
            st.write("•", item)
    else:
        st.success("Excellent! Your password is very strong.")