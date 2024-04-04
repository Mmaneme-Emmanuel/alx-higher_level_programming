#!/usr/bin/python3
"""Python script that takes your GitHub credentials"""
import sys
import requests

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]

    auth = (username, token)
    response = requests.get("https://api.github.com/user", auth=auth)

    if response.status_code == 200:
        print(response.json().get("id"))
    else:
        print("Failed to retrieve user information. Status code:",
              response.status_code)
