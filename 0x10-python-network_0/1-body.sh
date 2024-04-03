#!/bin/bash
curl -sL "$1" | grep -i 'HTTP/1.1 200 OK' -A 100 | sed -n '/^\s*$/,$p'
