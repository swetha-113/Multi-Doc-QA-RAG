import streamlit as st
import google.generativeai as genai
from datetime import datetime
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from rag_utils import process_pdfs, retrieve_context
from style import apply_theme

st.set_page_config(page_title="Ask Question | Multi-Doc Q&A", layout="wide")
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

st.markdown('<div class="main-title">📄 Ask Questions from PDFs</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Upload documents, ask anything, and get smart answers instantly</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown("### 🔑 Gemini API")
    api_key = st.text_input("Enter Gemini API Key", type="password")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown("### 📂 Upload PDFs")
    uploaded_files = st.file_uploader(
        "Upload one or more PDF documents",
        type=["pdf"],
        accept_multiple_files=True
    )
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="glass-card">', unsafe_allow_html=True)
st.markdown("### ❓ Ask Your Question")
question = st.text_input("Type your question here")
submit = st.button("✨ Get Answer")
st.markdown('</div>', unsafe_allow_html=True)

if submit:

    if not question:
        st.warning("Please enter a question.")

    elif not api_key:
        st.warning("Please enter your Gemini API key.")

    else:
        context = ""

        if uploaded_files:
            with st.spinner("Reading PDFs and creating vector database..."):
                vector_db = process_pdfs(uploaded_files)

            with st.spinner("Searching relevant document content..."):
                context = retrieve_context(vector_db, question)
        else:
            context = "No document uploaded."

        try:
            with st.spinner("Generating answer using Gemini..."):
                genai.configure(api_key=api_key)

                model = genai.GenerativeModel("gemini-2.5-flash-lite")

                prompt = f"""
You are a helpful Multi-Document Q&A assistant.

Use the document context if it is relevant.
If the document context does not contain the answer, answer using general knowledge.
Give a clear, simple, useful answer.

Document Context:
{context}

Question:
{question}

Answer:
"""

                response = model.generate_content(prompt)
                final_answer = response.text

            st.success("Answer generated successfully!")

        except Exception as e:
            final_answer = "Gemini API failed. Please check your API key, quota, model name, or internet connection."

            with st.expander("Error details"):
                st.write(e)

        st.markdown('<div class="answer-card">', unsafe_allow_html=True)
        st.markdown('<div class="answer-heading">🌟 Here is your answer</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="question-line">❓ Question: {question}</div>', unsafe_allow_html=True)
        st.write(final_answer)
        st.markdown('</div>', unsafe_allow_html=True)

        uploaded_file_names = []

        if uploaded_files:
            for file in uploaded_files:
                uploaded_file_names.append(file.name)

        st.session_state.history.append({
            "time": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            "username": st.session_state.username,
            "files": uploaded_file_names,
            "question": question,
            "answer": final_answer
        })

        with st.expander("📌 Retrieved Context"):
            st.write(context)