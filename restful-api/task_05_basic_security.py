#!/usr/bin/python3
"""API Security and Authentication Techniques"""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import check_password_hash
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity
)

app = Flask(__name__)
auth = HTTPBasicAuth()

# Use a strong secret key in production
app.config["JWT_SECRET_KEY"] = "your_secret_key"
jwt = JWTManager(app)

# Hardcoded hashed passwords to ensure consistent values.
# These values were generated using generate_password_hash("password")
users = {
    "user1": {
        "username": "user1",
        "password": (
            "pbkdf2:sha256:260000$9XxFP3Y69YJU0H5e$"
            "62e20c337c2e7a110583918e3eacb2f6a59b706c1b48bb1f3a8a90c92b9b6fbd"
        ),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": (
            "pbkdf2:sha256:260000$B0p1UWv6ULPZ8Lqk$"
            "91853e70bd2a7bf3d0a5d2978ccbd327d8dfd7c3d5e8f40d7c086b46a6f9eb2e"
        ),
        "role": "admin"
    }
}


@auth.verify_password
def verify_password(username, password):
    """Verify the username and password."""
    if username in users and check_password_hash(
            users[username]["password"], password):
        return username


@app.route("/basic-protected", methods=['GET'])
@auth.login_required
def basic_protected():
    """Route protected by Basic Authentication."""
    return "Basic Auth: Access Granted"


@app.route("/login", methods=['POST'])
def login():
    """Endpoint to obtain a JWT token."""
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    if username not in users or not check_password_hash(
            users[username]["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401

    # Embed the user's role in the token.
    access_token = create_access_token(identity={
        "username": username,
        "role": users[username]["role"]
    })
    return jsonify({"access_token": access_token}), 200


@app.route("/jwt-protected", methods=['GET'])
@jwt_required()
def jwt_protected():
    """Route protected by JWT."""
    return "JWT Auth: Access Granted"


@app.route("/admin-only", methods=['GET'])
@jwt_required()
def admin_only():
    """Route accessible only by admin users."""
    identity = get_jwt_identity()
    if identity["role"] != "admin":
        # Return 401 Unauthorized if the user's role is not admin.
        return jsonify({"error": "Admin access required"}), 401
    return "Admin Access: Granted"


# JWT error handlers.
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """Handle missing or invalid token errors."""
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """Handle invalid token errors."""
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    """Handle expired token errors."""
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    """Handle revoked token errors."""
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    """Handle cases where a fresh token is required."""
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == '__main__':
    # Listen on 0.0.0.0 so the API is accessible externally.
    app.run(host="0.0.0.0", port=5000, debug=True)
