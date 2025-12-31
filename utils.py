import numpy as np

LEFT_EYE = [33, 160, 158, 133, 153, 144]
RIGHT_EYE = [362, 385, 387, 263, 373, 380]
MOUTH = [61, 291, 81, 178, 13, 14]

def euclidean(p1, p2):
    return np.linalg.norm(np.array(p1) - np.array(p2))

def eye_aspect_ratio(eye):
    return (
        euclidean(eye[1], eye[5]) +
        euclidean(eye[2], eye[4])
    ) / (2.0 * euclidean(eye[0], eye[3]))

def mouth_aspect_ratio(mouth):
    return (
        euclidean(mouth[2], mouth[3]) +
        euclidean(mouth[4], mouth[5])
    ) / (2.0 * euclidean(mouth[0], mouth[1]))
