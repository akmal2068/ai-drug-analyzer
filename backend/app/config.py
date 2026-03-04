import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "secret")
    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY", "jwt-secret")
    SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID")
    GOOGLE_CLIENT_SECRET = os.environ.get("GOOGLE_CLIENT_SECRET")

    FRONTEND_URL = os.environ.get("FRONTEND_URL", "http://localhost:8000")