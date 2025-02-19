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

users = {}


@app.route('/')
def home():
    """
    Return a welcome message.
    """
    return "Welcome to the Flask API!"


@app.route('/data')
def get_users():
    """
    Return a JSON list of all usernames stored in the API.
    """
    return jsonify(list(users.keys()))


@app.route('/status')
def status():
    """
    Return the API status.
    """
    return "OK"


@app.route('/users/<username>')
def get_user(username):
    """
    Return user details if the user exists, else return an error message.
    
    Args:
        username (str): The username to look for.
    """
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

@app.route('/add_user', methods=['POST'])
def add_user():
    """
    Handle POST request to add a new user to the API.
    """
    data = request.get_json()

    if not data or "username" not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data["username"]
    users[username] = data

    return jsonify({"message": "User added", "user": data}), 201


if __name__ == "__main__":
    app.run(debug=True)
