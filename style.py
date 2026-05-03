import streamlit as st

def apply_theme():
    st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #050014, #12002f, #2d0059, #4c0033);
        color: white;
    }

    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #050014, #1e003d, #2d0059);
    }

    [data-testid="stSidebar"] * {
        color: white;
    }

    .main-title {
        font-size: 44px;
        font-weight: 900;
        text-align: center;
        color: #ffffff;
        text-shadow: 0 0 18px #ec4899;
        margin-top: 20px;
    }

    .sub-title {
        text-align: center;
        font-size: 18px;
        color: #f9a8d4;
        margin-bottom: 30px;
    }

    .glass-card {
        background: rgba(255, 255, 255, 0.10);
        padding: 30px;
        border-radius: 25px;
        box-shadow: 0 10px 35px rgba(0,0,0,0.45);
        border: 1px solid rgba(255,255,255,0.18);
        backdrop-filter: blur(12px);
        margin-top: 20px;
    }

    .answer-card {
        background: linear-gradient(135deg, rgba(236,72,153,0.25), rgba(124,58,237,0.25));
        padding: 30px;
        border-radius: 25px;
        border-left: 8px solid #ec4899;
        box-shadow: 0 10px 35px rgba(0,0,0,0.45);
        margin-top: 25px;
    }

    .answer-heading {
        color: #f9a8d4;
        font-size: 30px;
        font-weight: 900;
        text-shadow: 0 0 10px #ec4899;
    }

    .question-line {
        color: #ddd6fe;
        font-size: 18px;
        font-weight: bold;
        margin-bottom: 15px;
    }

    .stButton button {
        background: linear-gradient(90deg, #7c3aed, #ec4899);
        color: white;
        border: none;
        border-radius: 15px;
        padding: 12px 28px;
        font-weight: bold;
        font-size: 16px;
        box-shadow: 0 0 15px rgba(236,72,153,0.5);
    }

    .stButton button:hover {
        background: linear-gradient(90deg, #ec4899, #7c3aed);
        color: white;
        transform: scale(1.02);
    }

    .stTextInput input {
        border-radius: 14px;
        border: 2px solid #ec4899;
        background-color: #12002f;
        color: white;
    }

    .stTextInput label {
        color: #f9a8d4 !important;
        font-weight: bold;
    }

    .stFileUploader {
        background: rgba(255,255,255,0.10);
        padding: 18px;
        border-radius: 20px;
        border: 1px solid rgba(236,72,153,0.35);
    }

    .stAlert {
        border-radius: 15px;
    }

    h1, h2, h3 {
        color: #f9a8d4;
    }
    </style>
    """, unsafe_allow_html=True)