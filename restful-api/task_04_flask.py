#!/usr/bin/python3
"""Simple REST API using Flask."""

from flask import Flask
from flask import jsonify
from flask import request


app = Flask(__name__)

users = {
            "jane" : {
        "username": "jane", 
        "name": "Jane",
        "age": 28,
        "city": "Los Angeles"
            },
            "john" : {
        "username": "john", 
        "name": "John",
        "age": 30,
        "city": "New York"
}
}


@app.route('/')
def home():
    """Return a welcome message."""
    return "Welcome to the Flask API!"


@app.route('/data')
def get_username():
    """Return a JSON list of all usernames stored in the API."""
    return jsonify(list(users.keys()))


@app.route('/status')
def status():
    """Return API status."""
    return jsonify({"status": "OK"})


@app.route('/users/<username>')
def get_user(username):
     """Return user details if the user exists,
     else return an error message.
     """
     user = users.get(username)
     if user:
         return jsonify(user)
     return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """Handle POST request to add a new user to the API."""
    data = request.get_json()

    required_fields = ["username", "name", "age", "city"]
    if not data or any(field not in data for field in required_fields):
        return jsonify({"error": "All fields (username, name, age, city) are required"}), 400

    username = data["username"]
    if username in users:
        return jsonify({"error": "User already exists"}), 400

    users[username] = data
    return jsonify({"message": "User added", "user": data}), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

