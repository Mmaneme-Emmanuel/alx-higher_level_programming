#!/usr/bin/python3
"""script that takes in a URL and an email,
sends a POST request to the passed URL with the
email as a parameter, and displays the body of
the response (decoded in utf-8)
"""
import sys
import urllib.request
import urllib.parse

if __name__ == "__main__":
    url = sys.argv[1]

    email = sys.argv[2]

    content = {"email": email}
    data = urllib.parse.urlencode(content).encode('utf-8')

    """Sending POST request"""
    request = urllib.request.Request(url, data=data)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
