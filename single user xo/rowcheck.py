def row(row, column, matrix):
    for i in range(0, len(matrix), 1):
        if row == i:
            if column == 0:
                return matrix[row][column] == matrix[row][column + 1] == matrix[row][column+2]
            elif column == 1:
                return matrix[row][column - 1] == matrix[row][column] == matrix[row][column + 1]
            elif column == 2:
                return matrix[row][column - 2] == matrix[row][column - 1] == matrix[row][column]
    if matrix[0][0] == matrix[1][1] == matrix[2][2] and matrix[1][1] != "_":
        print("Hi4")
        return True
    if matrix[0][2] == matrix[1][1] == matrix[2][0] and matrix[1][1] != "_":
        print("Hi5")
        return True
    else:
        return False
