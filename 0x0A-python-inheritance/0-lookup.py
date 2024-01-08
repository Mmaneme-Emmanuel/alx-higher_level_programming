#!/usr/python3
"""Define object attribute lookup function"""

def lookup(obj):
    """returns the list of available attributes"""
    return dir(obj)
