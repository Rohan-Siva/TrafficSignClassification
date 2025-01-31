from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)  # Initialize Flask app
    CORS(app)  # Enable CORS for frontend communication

    # Import and register route blueprints
    from backend.routes.predict import predict_bp
    app.register_blueprint(predict_bp, url_prefix="/predict")

    return app
