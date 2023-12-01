#!/usr/bin/python3
for i in range(9):
    for k in range(i + 1, 10):
        if i != k:
            print("{:d}{:d}".format(i, k), end=", ")
print()
