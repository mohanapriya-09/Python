def diagonal_check(matrix, player):
    result = False
    if matrix[0][0] == matrix[1][1] == matrix[2][2] == player:
        result = True
    elif matrix[0][2] == matrix[1][1] == matrix[2][0] == player:
        result = True
    return result
