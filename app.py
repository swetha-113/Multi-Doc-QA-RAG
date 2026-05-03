import streamlit as st
from style import apply_theme

st.set_page_config(page_title="Login | Multi-Doc Q&A", layout="wide")
apply_theme()

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = ""

if "history" not in st.session_state:
    st.session_state.history = []

st.markdown('<div class="main-title">🌸 Multi-Doc Q&A System</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">AI-powered PDF question answering with RAG</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 1.2, 1])

with col2:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)

    if not st.session_state.logged_in:
        st.markdown("### 🔐 Login")

        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            if username == "admin" and password == "1234":
                st.session_state.logged_in = True
                st.session_state.username = username
                st.success("Login successful!")
                st.rerun()
            else:
                st.error("Invalid username or password")

        st.info("Demo Login: admin / 1234")

    else:
        st.success(f"Welcome, {st.session_state.username}!")

        st.write("Choose a page:")

        st.page_link("pages/1_Ask_Question.py", label="📄 Ask Question")
        st.page_link("pages/2_History.py", label="🕘 Activity History")
        st.page_link("pages/3_About.py", label="ℹ️ About Project")

        if st.button("Logout"):
            st.session_state.logged_in = False
            st.session_state.username = ""
            st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)