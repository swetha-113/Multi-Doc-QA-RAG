import streamlit as st
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from style import apply_theme

st.set_page_config(page_title="History | Multi-Doc Q&A", layout="wide")
apply_theme()

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = ""

if "history" not in st.session_state:
    st.session_state.history = []

if not st.session_state.logged_in:
    st.warning("Please login first from the Login page.")
    st.stop()

st.markdown('<div class="main-title">🕘 Activity History</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">View your previous questions and answers</div>', unsafe_allow_html=True)

if len(st.session_state.history) == 0:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.info("No history found yet.")
    st.markdown('</div>', unsafe_allow_html=True)

else:
    for i, item in enumerate(st.session_state.history, start=1):
        with st.expander(f"📌 Activity {i} - {item.get('time', 'No time')}"):
            st.write("👤 User:", item.get("username", "admin"))

            files = item.get("files", [])
            if files:
                st.write("📂 Uploaded Files:", ", ".join(files))
            else:
                st.write("📂 Uploaded Files: No files uploaded")

            st.write("❓ Question:", item.get("question", "No question"))

            st.markdown("### 🌟 Here is your answer")
            st.write(item.get("answer", "No answer"))

    st.write("")

    if st.button("Clear History"):
        st.session_state.history = []
        st.success("History cleared successfully!")
        st.rerun()