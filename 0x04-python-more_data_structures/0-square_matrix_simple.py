def square_matrix_simple(matrix=[]):
    new_mat = matrix.copy()

    for h in range(len(matrix)):
        new_mat[h] = list(map(lambda x: x**2, matrix[h]))

    return new_mat
