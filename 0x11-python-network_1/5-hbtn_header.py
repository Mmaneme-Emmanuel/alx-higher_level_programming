#!/usr/bin/python3
"""Write a Python script that fetches https://alx-"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)
    print(response.header.get("X-Request-Id"))
