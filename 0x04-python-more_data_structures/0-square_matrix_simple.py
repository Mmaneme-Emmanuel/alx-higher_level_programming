#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result_matrix = [[0] * len(matrix[0]) for _ in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            squared_value = matrix[i][j] ** 2
            result_matrix[i][j] = squared_value

    return result_matrix
