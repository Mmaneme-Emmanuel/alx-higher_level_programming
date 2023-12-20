#!/usr/bin/python3
def raise_exception_msg(message=""):
    try:
        message = ("C is fun")
        print(message)
    except NameError as ne:
        print(ne)
