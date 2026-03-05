import bcrypt
from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from ..models import User
from ..extensions import db

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.json
    hashed = bcrypt.hashpw(data["password"].encode(), bcrypt.gensalt())

    user = User(
        username=data["username"],
        email=data["email"],
        password=hashed
    )
    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "Registered successfully"})

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    user = User.query.filter_by(email=data["email"]).first()

    if user and bcrypt.checkpw(data["password"].encode(), user.password):
        token = create_access_token(identity=user.id)
        return jsonify({"token": token})

    return jsonify({"error": "Invalid credentials"}), 401