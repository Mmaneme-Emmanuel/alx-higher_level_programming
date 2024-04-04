#!/usr/bin/python3
"""Script that sends a POST request to http://0.0.0.0:5000/"""
import sys
import requests

if __name__ == "__main__":
    """Get the letter from command line argument"""
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""

    """Send a POST request with the letter as a parameter"""
    url = "http://0.0.0.0:5000/search_user"
    data = {'q': q}
    response = requests.post(url, data=data)

    """Check if the response is properly JSON formatted and not empty"""
    if response.ok:
        try:
            json_data = response.json()
            if json_data:
                print("[{}] {}".format(json_data['id'], json_data['name']))
            else:
                print("No result")
        except ValueError:
            print("Not a valid JSON")
    else:
        print("No result")
