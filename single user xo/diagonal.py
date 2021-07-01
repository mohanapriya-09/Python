def diagonal(matrix):
    result = False
    if matrix[0][0] == matrix[1][1] == matrix[2][2] and matrix[1][1] != "_":
        result = True
    elif matrix[0][2] == matrix[1][1] == matrix[2][0] and matrix[1][1] != "_":
        result = True
    return result
