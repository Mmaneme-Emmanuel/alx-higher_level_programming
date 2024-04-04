#!/usr/bin/python3
"""Python script that takes your GitHub credentials"""
import sys
import requests

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    """Set up the authentication header with the personal access token"""
    auth = (username, password)

    """Send a GET request to the GitHub API to retrieve user information"""
    response = requests.get("https://api.github.com/user", auth=auth)
    """Print the user's ID"""
    print(response.json().get("id"))
