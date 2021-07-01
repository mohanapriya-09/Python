def row_check(matrix, row, column, player):
    for i in range(0, len(matrix), 1):
        if row == i:
            if column == 0:
                return matrix[row][column] == matrix[row][column + 1] == matrix[row][column+2] == player
            elif column == 1:
                return matrix[row][column - 1] == matrix[row][column] == matrix[row][column + 1] == player
            elif column == 2:
                return matrix[row][column - 2] == matrix[row][column - 1] == matrix[row][column] == player
