from flask import Flask
from backend.routes.predict import predict_bp
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)  # To handle cross-origin requests

    # Register routes (like predict)
    app.register_blueprint(predict_bp, url_prefix="/predict")

    return app
