# TrafficSignClassification

## Overview
TrafficSignClassification is a full-stack machine learning application designed to identify and classify traffic signs from images. It utilizes a Convolutional Neural Network (CNN) trained on traffic sign datasets to provide accurate predictions. The system features a React frontend for users to upload images and a Flask backend that serves the trained model.

## Tools Used
- **Backend**: Python, Flask, Flask-RESTful
- **Machine Learning**: TensorFlow, Keras, OpenCV, NumPy, Pandas
- **Frontend**: React, Node.js
- **Visualization**: Matplotlib

## Structure
- `backend/`: Contains the Flask application logic and API routes.
- `frontend/`: Source code for the React-based user interface.
- `CNN_Models/`: Directory for storing trained model files (e.g., `.h5`).
- `Training_Notebooks/`: Jupyter notebooks used for data exploration and model training.
- `training_data/`: Directory for the dataset used to train the models.
- `main.py`: Entry point for the application.

## Setup

### Prerequisites
- Python 3.8+
- Node.js and npm

### Backend Setup
1. Navigate to the project root.
2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python main.py
   ```
   The backend API will start (typically on `http://localhost:5000`).

### Frontend Setup
1. Navigate to the `frontend` directory:
   ```bash
   cd frontend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start the development server:
   ```bash
   npm start
   ```
   The frontend application will launch in your browser.

## How It Works
1. **Training**: The model is trained using the notebooks in `Training_Notebooks/`, which preprocess the data and fit a CNN.
2. **Inference**: The trained model is loaded by the Flask backend.
3. **Interaction**: Users upload an image of a traffic sign via the React frontend. The image is sent to the backend, processed, and classified. The result is then displayed to the user.

## Contact
For collaborations or questions, please reach out to rohansiva123@gmail.com.
