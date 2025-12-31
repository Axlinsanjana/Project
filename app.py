import streamlit as st
from streamlit_webrtc import webrtc_streamer

from styles import load_css
from drowsiness_processor import DrowsinessProcessor

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="Driver Drowsiness Detection",
    page_icon="🚗",
    layout="wide"
)

# Load custom CSS
load_css()

# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------
if "page" not in st.session_state:
    st.session_state.page = "Home"

# --------------------------------------------------
# HEADER / NAVBAR
# --------------------------------------------------
st.markdown(
    '<div class="nav-logo">🚗 Driver Drowsiness Detection System</div>',
    unsafe_allow_html=True
)

c1, c2, c3, c4 = st.columns(4)

with c1:
    if st.button("🏠 Home", use_container_width=True):
        st.session_state.page = "Home"

with c2:
    if st.button("🎥 Live Detection", use_container_width=True):
        st.session_state.page = "Live"

with c3:
    if st.button("📊 System Info", use_container_width=True):
        st.session_state.page = "Info"

with c4:
    if st.button("ℹ️ About", use_container_width=True):
        st.session_state.page = "About"

# --------------------------------------------------
# HOME PAGE
# --------------------------------------------------
if st.session_state.page == "Home":
    st.markdown(
        "<h1 style='text-align:center;'>Welcome to Driver Drowsiness Detection</h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<p style='text-align:center;font-size:18px;'>"
        "This system monitors driver alertness in real time using "
        "eye-closure duration and yawning detection to prevent accidents."
        "</p>",
        unsafe_allow_html=True
    )

    st.image("driver_drowsiness.png", use_container_width=True)

# --------------------------------------------------
# LIVE WEBCAM DETECTION (FIXED SIZE)
# --------------------------------------------------
elif st.session_state.page == "Live":
    st.markdown(
        "<h1 style='text-align:center;'>🎥 Live Webcam Drowsiness Detection</h1>",
        unsafe_allow_html=True
    )

    # 🔥 IMPORTANT: CENTERED WIDE CONTAINER
    left, center, right = st.columns([1, 6, 1])

    with center:
        ctx = webrtc_streamer(
            key="drowsiness",
            video_processor_factory=DrowsinessProcessor,
            media_stream_constraints={
                "video": {
                    "width": {"ideal": 1280},
                    "height": {"ideal": 720},
                    "frameRate": {"ideal": 30}
                },
                "audio": False
            },
            async_processing=True
        )

    # ALERT MESSAGE
    if ctx.video_processor and ctx.video_processor.is_drowsy:
        st.error("🚨 WARNING: DRIVER IS DROWSY!")

# --------------------------------------------------
# SYSTEM INFO PAGE
# --------------------------------------------------
elif st.session_state.page == "Info":
    st.title("📊 System Information")

    st.markdown("""
    ### Detection Logic
    - **Eye Aspect Ratio (EAR)**
      - Eyes closed for more than **2 seconds** → Drowsy
    - **Yawning Detection**
      - Repeated large mouth opening

    ### Technologies Used
    - Python
    - Streamlit
    - OpenCV
    - MediaPipe
    - streamlit-webrtc
    """)

# --------------------------------------------------
# ABOUT PAGE
# --------------------------------------------------
elif st.session_state.page == "About":
    st.title("ℹ️ About This Project")

    st.markdown("""
    **Driver Drowsiness Detection System**

    This project detects driver fatigue using real-time
    facial landmark analysis and alerts the driver to
    prevent accidents.

    **Key Features**
    - Real-time webcam monitoring
    - Audio alert on drowsiness
    - Clean and professional UI

    **Use Cases**
    - Academic projects
    - Internship demonstrations
    - Driver safety applications
    """)
