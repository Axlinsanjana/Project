import cv2
import numpy as np
from model_loader import TFLiteModel

# Load TFLite model (make sure filename matches exactly)
model = TFLiteModel("drowsiness_model.tflite")


def preprocess_eye(eye_img):
    """
    Preprocess eye image for model input
    """
    eye_img = cv2.resize(eye_img, (224, 224))
    eye_img = eye_img.astype(np.float32) / 255.0
    return eye_img


def is_drowsy(eye_img):
    """
    Predict drowsiness from eye image
    Returns True if drowsy, else False
    """
    processed_eye = preprocess_eye(eye_img)
    prediction = model.predict(processed_eye)

    # Threshold (adjust if needed)
    return prediction > 0.5
