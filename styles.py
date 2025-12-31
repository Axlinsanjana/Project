import streamlit as st

def load_css():
    st.markdown("""
    <style>

    /* =========================================================
       PAGE BACKGROUND
    ========================================================= */
    html, body,
    .stApp,
    [data-testid="stAppViewContainer"],
    [data-testid="stVerticalBlock"] {
        background-color: #F2F2F2 !important;
    }

    /* =========================================================
       MAIN CONTENT CONTAINER
    ========================================================= */
    .block-container {
        background-color: #FFFFFF;
        padding: 2rem 2.5rem;
        border-radius: 16px;
        box-shadow: 0 6px 20px rgba(90, 45, 222, 0.08);
        margin-top: 1rem;
    }

    /* =========================================================
       NAVBAR / HEADER
    ========================================================= */
    .nav-logo {
        background: linear-gradient(90deg, #5A2DDE, #673AB7);
        color: #FFFFFF;
        font-size: 28px;
        font-weight: 800;
        text-align: center;
        padding: 18px;
        border-radius: 14px;
        margin-bottom: 28px;
        box-shadow: 0 6px 18px rgba(90, 45, 222, 0.3);
    }

    /* =========================================================
       BUTTONS
    ========================================================= */
    button {
        background-color: #673AB7 !important;
        color: #FFFFFF !important;
        font-weight: 700 !important;
        border-radius: 12px !important;
        border: none !important;
        padding: 10px 16px !important;
        transition: all 0.2s ease-in-out;
    }

    button:hover {
        background-color: #5A2DDE !important;
        transform: translateY(-1px);
        box-shadow: 0 4px 12px rgba(90, 45, 222, 0.35);
    }

    /* =========================================================
       SECONDARY BUTTON
    ========================================================= */
    .stButton > button[kind="secondary"] {
        background-color: #FFFFFF !important;
        color: #673AB7 !important;
        border: 2px solid #673AB7 !important;
    }

    /* =========================================================
       ALERTS
    ========================================================= */
    .stAlert {
        border-radius: 14px;
        font-weight: 600;
    }

    .stAlert.success {
        background-color: #ECFEFF;
        color: #0F766E;
        border-left: 6px solid #2DD4BF;
    }

    .stAlert.info {
        background-color: #F3F0FF;
        color: #4C1D95;
        border-left: 6px solid #673AB7;
    }

    .stAlert.warning {
        background-color: #FFF7ED;
        color: #9A3412;
        border-left: 6px solid #F97316;
    }

    .stAlert.error {
        background-color: #FDECEC;
        color: #7F1D1D;
        border-left: 6px solid #DC2626;
    }

    /* =========================================================
       TEXT
    ========================================================= */
    h1, h2, h3 {
        color: #5A2DDE;
        font-weight: 800;
    }

    p {
        color: #1C1C1C;
    }

    /* =========================================================
       ✅ WEBCAM FIX (THE IMPORTANT PART)
       streamlit-webrtc uses IFRAME
    ========================================================= */

    /* Center the webcam container */
    [data-testid="stVideo"] {
        width: 100% !important;
        display: flex !important;
        justify-content: center !important;
        margin-top: 20px;
    }

    /* Resize the WebRTC iframe */
    [data-testid="stVideo"] iframe {
        width: 100% !important;
        min-height: 550px !important;
        border-radius: 16px !important;
        box-shadow: 0 10px 32px rgba(0,0,0,0.35);
    }

    </style>
    """, unsafe_allow_html=True)
