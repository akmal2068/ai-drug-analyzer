from flask import Flask
from flask_cors import CORS
from .config import Config
from .extensions import db, jwt
from .routes.auth import auth_bp
from .routes.drug import drug_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    CORS(app)

    db.init_app(app)
    jwt.init_app(app)

    app.register_blueprint(auth_bp)
    app.register_blueprint(drug_bp)

    with app.app_context():
        db.create_all()

    return app