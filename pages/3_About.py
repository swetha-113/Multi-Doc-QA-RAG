import streamlit as st
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from style import apply_theme

st.set_page_config(page_title="About | Multi-Doc Q&A", layout="wide")
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

st.markdown('<div class="main-title">ℹ️ About This Project</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">A colorful RAG-based AI document assistant</div>', unsafe_allow_html=True)

st.markdown("""
<div class="glass-card">

<h2>📄 Multi-Document Q&A System using RAG</h2>

<p>
This application allows users to upload multiple PDF documents and ask questions.
The system searches the most relevant content from the uploaded documents and generates a clear answer using Gemini AI.
</p>

<h3>✨ Features</h3>
<ul>
<li>🔐 User login system</li>
<li>📂 Multiple PDF upload</li>
<li>🔍 Document chunking and semantic search</li>
<li>🧠 FAISS vector database</li>
<li>🤖 Gemini AI answer generation</li>
<li>🕘 Activity history tracking</li>
<li>🎨 Colorful purple-black-pink Streamlit UI</li>
</ul>

<h3>🛠 Technologies Used</h3>
<ul>
<li>Python</li>
<li>Streamlit</li>
<li>LangChain</li>
<li>FAISS</li>
<li>HuggingFace Embeddings</li>
<li>Google Gemini API</li>
<li>PyPDFLoader</li>
</ul>

<h3>⚙️ Workflow</h3>
<ol>
<li>User logs into the application.</li>
<li>User uploads one or more PDF files.</li>
<li>PDF content is loaded and split into chunks.</li>
<li>Chunks are converted into embeddings.</li>
<li>FAISS stores and searches the relevant content.</li>
<li>Gemini generates the final answer.</li>
<li>The question and answer are saved in history.</li>
</ol>

</div>
""", unsafe_allow_html=True)