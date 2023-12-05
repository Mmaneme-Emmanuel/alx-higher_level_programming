#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print()
    else:
        for row in matrix:
            for index, element in enumerate(row):
                if index != len(row) - 1:
                    endspace = ' '
                else:
                    endspace = ''
                print("{:d}{}".format(element, endspace), end="")
            print()
