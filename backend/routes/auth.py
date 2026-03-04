import bcrypt
from flask import Blueprint, request, jsonify, redirect, url_for
from flask_jwt_extended import create_access_token
from ..models import User
from ..extensions import db, oauth
from flask import current_app

auth_bp = Blueprint("auth", __name__)

google = oauth.register(
    name='google',
    client_id=lambda: current_app.config["GOOGLE_CLIENT_ID"],
    client_secret=lambda: current_app.config["GOOGLE_CLIENT_SECRET"],
    server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
    client_kwargs={'scope': 'openid email profile'}
)

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

    if user and user.password and bcrypt.checkpw(data["password"].encode(), user.password):
        token = create_access_token(identity=user.id)
        return jsonify({"token": token})

    return jsonify({"error": "Invalid credentials"}), 401


@auth_bp.route("/google-login")
def google_login():
    redirect_uri = url_for("auth.google_authorize", _external=True)
    return google.authorize_redirect(redirect_uri)


@auth_bp.route("/authorize")
def google_authorize():
    token = google.authorize_access_token()
    user_info = google.parse_id_token(token)

    user = User.query.filter_by(email=user_info["email"]).first()

    if not user:
        user = User(
            username=user_info["name"],
            email=user_info["email"],
            google_id=user_info["sub"]
        )
        db.session.add(user)
        db.session.commit()

    jwt_token = create_access_token(identity=user.id)

    # 🔥 AUTO REDIRECT TO FRONTEND WITH TOKEN
    frontend_url = current_app.config["FRONTEND_URL"]
    return redirect(f"{frontend_url}?token={jwt_token}")