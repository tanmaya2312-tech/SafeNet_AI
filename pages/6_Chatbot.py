import streamlit as st
from sarvam_chat import ask_ai
from core.session import initialize_session
from datetime import datetime
from report_generator import generate_chat_report

initialize_session()


st.title("🤖 AI Cybersecurity Assistant")

question = st.text_area(
    "Ask any cybersecurity question"
)

if st.button("Ask SafeNet AI"):

    if question:

        with st.spinner("Thinking..."):

            answer = ask_ai(question)
            pdf = generate_chat_report(question, answer)

        # Update dashboard statistics
        st.session_state.ai_queries += 1

        # Save to analysis history
        st.session_state.activity_log.append({
            "time": datetime.now().strftime("%d-%m-%Y %I:%M %p"),
            "tool": "AI Assistant",
            "status": "Answered",
            "score": 100
        })

        st.markdown("### 🤖 SafeNet AI Response")
        st.info(answer)
        st.download_button(
    "📄 Download AI Report",
    data=pdf,
    file_name="AI_Assistant_Report.pdf",
    mime="application/pdf",
    use_container_width=True
)

    else:
        st.warning("Please enter a question.")