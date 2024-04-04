#!/usr/bin/python3
"""Python script that takes your GitHub credentials"""
import sys
import requests

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    auth = (username, password)

    response = requests.get("https://api.github.com/user", auth=auth)
    print(response.json().get("id"))
