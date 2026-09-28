import base64
from pathlib import Path
import streamlit as st
from src.api.client import fetch_question

st.set_page_config(page_title="AI Interviewer", layout="centered")

# Convert local webp to base64 for reliable embedding
IMAGE_PATH = Path(__file__).resolve().parent / "thinking-black-guy.webp"
img_b64 = ""
if IMAGE_PATH.exists():
    with open(IMAGE_PATH, "rb") as f:
        img_b64 = base64.b64encode(f.read()).decode()

st.markdown("""
    <style>
        #MainMenu, header, footer, .stDeployButton {
            display: none !important;
        }

        html, body, [data-testid="stAppViewContainer"] {
            background-color: #F8F5EE !important;
        }

        .block-container {
            padding: 2.5rem 1.2rem !important;
            max-width: 1000px !important;
        }

        .title-text {
            text-align: center;
            font-size: 1.4rem;
            font-weight: 700;
            color: #1F2937;
            margin-bottom: 1rem;
            letter-spacing: -0.01em;
        }

        .question-card {
            background-color: #FFFFFF;
            border: 1px solid #E5E0D5;
            border-radius: 12px;
            padding: 2rem 1.5rem;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
            margin-bottom: 1.5rem;
            min-height: 70dvh;
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
        }

        .question-content {
            font-size: 1.1rem;
            font-weight: 500;
            line-height: 1.6;
            color: #111827;
        }

        /* Loading State Styling */
        .loading-container {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 12px;
            font-size: 1.25rem;
            font-weight: 700;
            color: #374151;
        }

        .loading-img {
            width: 100px;
            height: 100px;
            border-radius: 50%;
            object-fit: cover;
            border: 2px solid #E5E0D5;
            animation: pulse 1.2s infinite ease-in-out;
        }

        @keyframes pulse {
            0%, 100% { transform: scale(1); opacity: 1; }
            50% { transform: scale(1.08); opacity: 0.85; }
        }

        div.stButton > button {
            width: 100% !important;
            background-color: #111827 !important;
            color: #FFFFFF !important;
            border: none !important;
            border-radius: 8px !important;
            padding: 0.65rem 1rem !important;
            font-size: 0.95rem !important;
            font-weight: 600 !important;
            transition: background-color 0.15s ease !important;
        }

        div.stButton > button:hover {
            background-color: #374151 !important;
        }
    </style>
""", unsafe_allow_html=True)

# 1. Header
st.markdown('<div class="title-text">🫪 AI Interviewer 🫪</div>', unsafe_allow_html=True)

# State initialization
if "question" not in st.session_state:
    st.session_state.question = "Click the button below to generate an interview question."

# Container placeholder for question or loading state
card_placeholder = st.empty()

# Render initial or current question card
card_placeholder.markdown(
    f'''
    <div class="question-card">
        <div class="question-content">{st.session_state.question}</div>
    </div>
    ''',
    unsafe_allow_html=True
)

# 2. Action Button
if st.button("Generate Question", type="primary"):
    # Display "I am" + thinking webp image during generation
    card_placeholder.markdown(
        f'''
        <div class="question-card">
            <div class="loading-container">
                <span>I am</span>
                <img class="loading-img" src="data:image/webp;base64,{img_b64}" alt="thinking" />
            </div>
        </div>
        ''',
        unsafe_allow_html=True
    )

    data = fetch_question()
    if "error" in data:
        st.session_state.question = f"Error: {data['error']}"
    else:
        q = data.get("question", "").strip()
        if q.startswith('"') and q.endswith('"'):
            q = q[1:-1].strip()
        st.session_state.question = q

    # Replace with generated question
    card_placeholder.markdown(
        f'''
        <div class="question-card">
            <div class="question-content">{st.session_state.question}</div>
        </div>
        ''',
        unsafe_allow_html=True
    )
    st.rerun()