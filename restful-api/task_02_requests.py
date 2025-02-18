#!/bin/usr/python3
"""This module uses the requests library,
    parse and manipulate JSON data using Python,
    convert structured data into CSV format.
"""

import requests
import csv


def fetch_and_print_posts():
    """Fetch posts from JSONPlaceholder and print the titles."""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    print(f"Statuts Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post["title"])
    else:
        print("Failed to retrivie posts")


def fetch_and_save_posts():
    """Fetch posts from JSONPlaceholder and save them into a CSV file."""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()

        posts_data = [
            {"id": post["id"], "title": post["title"], "body": post["body"]}
            for post in posts
        ]

        with open("posts.csv",
                  mode="w",
                  newline="",
                  encoding="utf-8") as file:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(posts_data)

        print("Data successfully saved to posts.csv")
    else:
        print("Failed to retrieve posts")
