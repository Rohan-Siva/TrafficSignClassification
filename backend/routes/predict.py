from flask import Blueprint, request, jsonify
import numpy as np
import cv2
import pandas as pd
from tensorflow.keras.models import load_model
from PIL import Image
import io
import os
import requests

# Create Blueprint for predictions
predict_bp = Blueprint('predict', __name__)

# Model and label paths
MODEL_DIR = "models"
MODELS = {
    "germany": {"model": "/Users/rohansiva/Desktop/ML_Projects/TrafficSignClassification/CNN_Models/german_traffic_signs_classifier.h5", "labels": "/Users/rohansiva/Desktop/ML_Projects/TrafficSignClassification/training_data/signnames.csv"},
    "usa": {"model": "usa_model.h5", "labels": "usa_labels.csv"}
}

# Load models dynamically
loaded_models = {}
loaded_labels = {}

for country, paths in MODELS.items():
    model_path = os.path.join(MODEL_DIR, paths["model"])
    labels_path = os.path.join(MODEL_DIR, paths["labels"])
    
    if os.path.exists(model_path) and os.path.exists(labels_path):
        loaded_models[country] = load_model(model_path)
        loaded_labels[country] = pd.read_csv(labels_path).values[:, 1]  # Extract sign names
    else:
        print(f"Warning: Model or labels missing for {country}")

# Image Preprocessing Function
def preprocess_image(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
    image = cv2.equalizeHist(image)  # Apply histogram equalization
    image = image / 255.0  # Normalize pixel values
    image = cv2.resize(image, (32, 32))  # Resize to match model input shape
    return image.reshape(1, 32, 32, 1)  # Reshape for model input

# Prediction Route with Country Selection
@predict_bp.route('/predict/<country>', methods=['POST'])
def predict(country):
    if country not in loaded_models:
        return jsonify({"error": f"Model for {country} not found"}), 400

    if 'image' not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    file = request.files['image']
    image = Image.open(io.BytesIO(file.read()))
    image = np.array(image)

    processed_img = preprocess_image(image)
    model = loaded_models[country]
    labels = loaded_labels[country]

    prediction = model.predict(processed_img)
    predicted_class = np.argmax(prediction)

    return jsonify({
        "country": country,
        "predicted_sign": labels[predicted_class],
        "confidence": float(np.max(prediction))
    })
