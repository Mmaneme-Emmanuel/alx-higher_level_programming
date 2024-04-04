#!/usr/bin/python3
"""script that takes in a URL and an email address,"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    # Create a dictionary with the email parameter
    data = {'email': email}

    # Send a POST request to the URL with the data
    response = requests.post(url, data=data)

    # Display the body of the response
    print(response.text)
