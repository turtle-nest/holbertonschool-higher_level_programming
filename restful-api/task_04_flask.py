#!/usr/bin/python3
"""Simple REST API using Flask.

This module provides a simple REST API to manage users using Flask.
Endpoints:
    /          : Returns a welcome message.
    /data      : Returns a JSON list of all usernames.
    /status    : Returns the API status.
    /users/<username> : Returns details of the specified user.
    /add_user  : Accepts POST requests to add a new user.
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

users = {
    "jane": {
        "username": "jane", 
        "name": "Jane",
        "age": 28,
        "city": "Los Angeles"
    },
    "john": {
        "username": "john", 
        "name": "John",
        "age": 30,
        "city": "New York"
    }
}


@app.route('/')
def home():
    """
    Return a welcome message.
    
    Returns:
        str: A welcome message.
    """
    return "Welcome to the Flask API!"


@app.route('/data')
def get_username():
    """
    Return a JSON list of all usernames stored in the API.
    
    Returns:
        Response: A Flask JSON response containing a list of usernames.
    """
    return jsonify(list(users.keys()))


@app.route('/status')
def status():
    """
    Return the API status.
    
    Returns:
        Response: A Flask JSON response indicating the API status.
    """
    return jsonify({"status": "OK"})


@app.route('/users/<username>')
def get_user(username):
    """
    Return user details if the user exists, else return an error message.
    
    Args:
        username (str): The username to look for.
    
    Returns:
        Response: A Flask JSON response with the user data or an error message.
    """
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """
    Handle POST request to add a new user to the API.
    
    Expects a JSON payload with the following keys:
        - username: The username of the user.
        - name: The full name of the user.
        - age: The age of the user.
        - city: The city where the user lives.
    
    Returns:
        Response: A Flask JSON response with a confirmation message and the added user data.
                  Returns an error response if any field is missing or if the user already exists.
    """
    data = request.get_json()

    required_fields = ["username", "name", "age", "city"]
    if not data or any(field not in data for field in required_fields):
        return jsonify({"error": "All fields (username, name, age, city) are required"}), 400

    username = data["username"]
    if username in users:
        return jsonify({"error": "User already exists"}), 400

    users[username] = data
    return jsonify({"message": "User added", "user": data}), 201


def run_server():
    """
    Run the Flask development server.
    
    This function starts the Flask server on host 0.0.0.0 and port 5000 with debug mode enabled.
    """
    app.run(host="0.0.0.0", port=5000, debug=True)


if __name__ == "__main__":
    run_server()
