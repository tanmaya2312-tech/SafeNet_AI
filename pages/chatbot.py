import streamlit as st
from sarvam_chat import ask_ai

st.title("🤖 AI Cybersecurity Assistant")

question = st.text_area(
    "Ask any cybersecurity question"
)

if st.button("Ask SafeNet AI"):

    if question:

        with st.spinner("Thinking..."):

            answer = ask_ai(question)

        st.success(answer)