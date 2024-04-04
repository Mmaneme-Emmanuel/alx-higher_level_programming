#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]

    """Send a GET request to the URL"""
    response = requests.get(url)

    """Check if the status code is greater than or equal to 400"""
    if response.status_code >= 400:
        print("Error code:", response.status_code)
    else:
        print(response.text)
