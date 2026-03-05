from .extensions import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    email = db.Column(db.String(200), unique=True)
    password = db.Column(db.LargeBinary)
    google_id = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)