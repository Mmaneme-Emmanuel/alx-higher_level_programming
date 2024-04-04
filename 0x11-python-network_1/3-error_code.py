#!/usr/bin/python3
"""Write a Python script that takes in a URL,
sends a request to the URL and displays the body
of the response (decoded in utf-8).
"""
import sys
import urllib.request
import urllib.parse
import urllib.error

if __name__ == "__main__":
    """Extract the URL from command line arguments"""
    url = sys.argv[1]

    try:
        """Send request to the URL"""
        with urllib.request.urlopen(url) as response:
            """Read and decode the response body"""
            print(response.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        """If an HTTP error occurs, print the error code"""
        print("Error code:", e.code)
