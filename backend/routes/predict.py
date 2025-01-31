from flask import Blueprint, request, jsonify
import numpy as np
import cv2
from tensorflow.keras.models import load_model
import pandas as pd
from PIL import Image
import requests
import os

predict_bp = Blueprint("predict", __name__)

#storing models and csv file sign name dirs

MODELS = {
    "germany": load_model("/Users/rohansiva/Desktop/ML_Projects/TrafficSignClassification/CNN_Models/german_traffic_signs_classifier.h5"),
    "usa": load_model("backend/models/usa_model.h5"),
}

SIGN_NAMES = {
    "germany": pd.read_csv("/Users/rohansiva/Desktop/ML_Projects/TrafficSignClassification/training_data/signnames.csv"),
    "usa": pd.read_csv("backend/models/usa_signnames.csv"),
}

def preprocess_image(image): # processing w/ grayscale resizing for model etc
    img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    img = cv2.equalizeHist(img)
    img = img / 255.0  
    img = cv2.resize(img, (32, 32)) 
    img = img.reshape(1, 32, 32, 1)
    return img

@predict_bp.route("/<country>", methods=["POST"])
def predict_sign(country):
    """ Predict traffic sign based on selected country model """
    if country not in MODELS:
        return jsonify({"error": "Invalid country"}), 400

    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    file = request.files["image"]
    image = Image.open(file).convert("RGB")
    image = np.array(image)

    image = preprocess_image(image)


    # calling model predictions
    model = MODELS[country]
    prediction = model.predict(image)
    pred_index = np.argmax(prediction)

    # getting the sign names
    sign_name = SIGN_NAMES[country]["SignName"].iloc[pred_index]

    return jsonify({
        "predicted_sign": sign_name,
        "confidence": float(prediction[0][pred_index])
    })
