#!/bin/bash
# takes in a URL as an argument, sends a GET request to the URL
curl -sL "$1" -H "X-School-User-Id: 98 "
