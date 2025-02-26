#!/usr/bin/python3
"""API Security and Authentication Techniques"""

from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from flask_jwt_extended import get_jwt_identity, get_jwt

app = Flask(__name__)
auth = HTTPBasicAuth()
app.config["JWT_SECRET_KEY"] = "your_secret_key"
jwt = JWTManager(app)

users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}

"""BASIC PROTECTION"""
@auth.verify_password
def verify_password(username, password):
    """Verify username and password"""
    if username in users and \
        check_password_hash(users[username]["password"], password):
        return username
    return None

@app.route("/basic-protected", methods=['GET'])
@auth.login_required
def basic_protected():
    """Basic authentication protected route"""
    return ("Basic Auth: Access Granted")

"""TOKEN PROTECTION"""
@app.route("/login", methods=['POST'])
def login():
    """Login endpoint to obtain a JWT token"""

    data = request.json
    username = data.get("username")
    password = data.get("password")

    if username in users and\
       check_password_hash(users[username]["password"], password):
        role = users[username]["role"]
        access_token = create_access_token(identity=username,
                                        additional_claims={"role": role})
        return jsonify(access_token=access_token)
    return jsonify({"error": "Invalid username or password"}), 401

@app.route("/jwt-protected", methods=['GET'])
@jwt_required()
def jwt_protected():
    """JWT protected route"""
    return "JWT Auth: Access Granted"

@app.route("/admin-only", methods=['GET'])
@jwt_required()
def admin_only():
    """Route accessible only by admin users"""
    claims = get_jwt()
    if claims.get('role') != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"

@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """Handle missing or invalid token errors"""
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """Handle invalid token errors"""
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(err):
    """Handle expired token errors"""
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    """Handle revoked token errors"""
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    """Handle cases where a fresh token is required"""
    return jsonify({"error": "Fresh token required"}), 401

@jwt.unauthorized_loader
def handle_missing_token(err):
    """error handling"""
    return jsonify({"error": "Authorization header missing or invalid"}), 401

@jwt.revoked_token_loader
def handle_revoked_token(jwt_header, jwt_payload):
    """error handling"""
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.invalid_token_loader
def handle_invalid_claims(err):
    """error handling"""
    return jsonify({"error": "Invalid token claims"}), 401

if __name__ == '__main__':
    app.run()
