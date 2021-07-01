def column(row, column,matrix):
    for j in range(0, len(matrix), 1):
        if column == j:
            if row == 0:
                return matrix[row][column] == matrix[row+1][column] == matrix[row+2][column]
            elif row == 1:
                return matrix[row - 1][column] == matrix[row][column] == matrix[row + 1][column]
            elif row == 2:
                return matrix[row - 2][column] == matrix[row - 1][column] == matrix[row][column]