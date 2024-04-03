#!/usr/bin/python3
import urllib.request

url = "https://alx-intranet.hbtn.io/status"
with urllib.request.urlopen(url) as response:
    status = response.read()
    print("\t- Body response:")
    print("\t\t- type: {}".format(type(status)))
    print("\t- content: {}".format(status))
    print("\t\t- utf-8 content: {}".format(status.decode('utf-8')))
