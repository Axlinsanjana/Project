import cv2
import time
import av
import platform
import mediapipe as mp
from streamlit_webrtc import VideoProcessorBase

from utils import (
    LEFT_EYE,
    RIGHT_EYE,
    MOUTH,
    eye_aspect_ratio,
    mouth_aspect_ratio
)

# --------------------------------------------------
# SAFE OS-SPECIFIC SOUND (WINDOWS ONLY)
# --------------------------------------------------
IS_WINDOWS = platform.system() == "Windows"
if IS_WINDOWS:
    try:
        import winsound
    except ImportError:
        winsound = None
else:
    winsound = None

# --------------------------------------------------
# SAFE MEDIAPIPE FACEMESH
# --------------------------------------------------
if hasattr(mp, "solutions") and hasattr(mp.solutions, "face_mesh"):
    mp_face_mesh = mp.solutions.face_mesh
else:
    mp_face_mesh = None


class DrowsinessProcessor(VideoProcessorBase):
    def __init__(self):
        if mp_face_mesh is None:
            raise RuntimeError("MediaPipe FaceMesh not available")

        self.face_mesh = mp_face_mesh.FaceMesh(
            static_image_mode=False,
            max_num_faces=1,
            refine_landmarks=True
        )

        self.eye_closed_start = None
        self.is_drowsy = False
        self.last_beep_time = 0

    def recv(self, frame):
        img = frame.to_ndarray(format="bgr24")
        rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = self.face_mesh.process(rgb)

        now = time.time()
        self.is_drowsy = False

        if results.multi_face_landmarks:
            lm = results.multi_face_landmarks[0].landmark
            h, w, _ = img.shape

            left_eye = [(int(lm[i].x * w), int(lm[i].y * h)) for i in LEFT_EYE]
            right_eye = [(int(lm[i].x * w), int(lm[i].y * h)) for i in RIGHT_EYE]
            mouth = [(int(lm[i].x * w), int(lm[i].y * h)) for i in MOUTH]

            ear = (eye_aspect_ratio(left_eye) + eye_aspect_ratio(right_eye)) / 2.0
            mar = mouth_aspect_ratio(mouth)

            # -------------------------------
            # EYE CLOSURE LOGIC
            # -------------------------------
            if ear < 0.25:
                if self.eye_closed_start is None:
                    self.eye_closed_start = now
                elif now - self.eye_closed_start >= 2:
                    self.is_drowsy = True
            else:
                self.eye_closed_start = None

            # -------------------------------
            # YAWN LOGIC
            # -------------------------------
            if mar > 0.6:
                self.is_drowsy = True

        # -------------------------------
        # SOUND (WINDOWS ONLY, SAFE)
        # -------------------------------
        if self.is_drowsy and winsound:
            if now - self.last_beep_time > 1.5:
                winsound.Beep(1000, 700)
                self.last_beep_time = now

        # -------------------------------
        # OVERLAY TEXT
        # -------------------------------
        cv2.putText(
            img,
            "DROWSY / SLEEPY" if self.is_drowsy else "ALERT",
            (20, 60),
            cv2.FONT_HERSHEY_SIMPLEX,
            1.4,
            (0, 0, 255) if self.is_drowsy else (0, 255, 0),
            3
        )

        return av.VideoFrame.from_ndarray(img, format="bgr24")
