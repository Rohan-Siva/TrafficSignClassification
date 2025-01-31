from flask import Flask
from flask_cors import CORS
from routes.predict import predict_bp  # Import prediction route

app = Flask(__name__)
CORS(app)

# Register Blueprint
app.register_blueprint(predict_bp)

if __name__ == '__main__':
    app.run(debug=True)
