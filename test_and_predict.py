# =====================================================
# IMPORTS
# =====================================================
import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input

from sklearn.metrics import classification_report, confusion_matrix

print("✅ Script started")


# =====================================================
# PATHS & CONSTANTS
# =====================================================
TEST_DIR = r"C:\My PC\Project\Dataset\test"
MODEL_PATH = "drowsiness_mobilenetv2.h5"
SINGLE_IMAGE_PATH = r"C:\My PC\Project\Dataset\test\Closed\_107.jpg"

IMG_SIZE = (224, 224)
BATCH_SIZE = 32


# =====================================================
# SAFETY CHECKS
# =====================================================
if not os.path.exists(TEST_DIR):
    raise FileNotFoundError("❌ TEST_DIR not found")

if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError("❌ Model file not found")

if not os.path.exists(SINGLE_IMAGE_PATH):
    raise FileNotFoundError("❌ Test image not found")


# =====================================================
# CHECK GPU
# =====================================================
gpus = tf.config.list_physical_devices("GPU")
print("GPU Available:", gpus if gpus else "❌ No GPU (Using CPU)")


# =====================================================
# LOAD MODEL (ONCE)
# =====================================================
model = load_model(MODEL_PATH)
print("✅ Model loaded successfully")


# =====================================================
# LOAD TEST DATA
# =====================================================
test_gen = ImageDataGenerator(preprocessing_function=preprocess_input)

test_data = test_gen.flow_from_directory(
    TEST_DIR,
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode="categorical",
    shuffle=False
)

class_names = list(test_data.class_indices.keys())
print("Class names:", class_names)


# =====================================================
# MODEL EVALUATION
# =====================================================
print("\n⏳ Evaluating model...")

test_data.reset()
predictions = model.predict(test_data, verbose=0)
y_pred = np.argmax(predictions, axis=1)
y_true = test_data.classes

print("\n📊 Classification Report:\n")
print(classification_report(y_true, y_pred, target_names=class_names))


# =====================================================
# CONFUSION MATRIX
# =====================================================
cm = confusion_matrix(y_true, y_pred)

plt.figure(figsize=(6, 5))
sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    cmap="Blues",
    xticklabels=class_names,
    yticklabels=class_names
)
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")
plt.tight_layout()
plt.show()


# =====================================================
# FAST SINGLE IMAGE PREDICTION
# =====================================================
print("\n⏳ Predicting single image...")

img = image.load_img(SINGLE_IMAGE_PATH, target_size=IMG_SIZE)
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)
img_array = preprocess_input(img_array)

# 🔥 FAST inference
prediction = model(img_array, training=False)
predicted_class = class_names[np.argmax(prediction)]


# =====================================================
# DROWSINESS LOGIC
# =====================================================
if predicted_class.lower() in ["closed", "yawn"]:
    status = "DROWSY 😴"
else:
    status = "ALERT 🙂"

print("Predicted Class:", predicted_class)
print("Driver Status:", status)


# =====================================================
# DISPLAY IMAGE (OPTIONAL VISUALIZATION)
# =====================================================
plt.imshow(img)
plt.title(f"{predicted_class} → {status}")
plt.axis("off")
plt.show()

print("\n✅ Prediction completed successfully")
