def square_matrix_simple(matrix=[]):
    # Create a new matrix with the same size as the input matrix
    result_matrix = [[0] * len(matrix[0]) for _ in range(len(matrix))]

    # Iterate through each row in the input matrix
    for i in range(len(matrix)):
        # Iterate through each element in the row and square the value
        for j in range(len(matrix[i])):
            squared_value = matrix[i][j] ** 2
            result_matrix[i][j] = squared_value

    return result_matrix
