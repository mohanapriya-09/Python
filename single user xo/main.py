import current
import rowcheck
import columncheck
import diagonal


def user_input():
    a = int(input("Enter the value "))
    return a


name = str(input("Enter your name:"))
matrix = [["_", "_", "_"],
          ["_", "_", "_"],
          ["_", "_", "_"]]
while True:
    row = user_input()
    column = user_input()
    matrix[row][column] = name[0]
    current.current(matrix)
    if rowcheck.row(row, column, matrix) or columncheck.column(row, column, matrix):
        print("Game Over")
        break
    elif diagonal.diagonal(matrix):
        print("Game Over")
        break
