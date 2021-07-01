import display
import rowcheck
import columncheck
import diagonal


def user_input(player):
    return int(input("Enter the player "+str(player)+" position:"))


matrix = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
row_column = []
player_1 = str(input("What do you want to choose X or O"))
player_2 = str(input("What do you want to choose X or O"))
result = True
while result:
    for i in range(2):
        row = user_input(i+1)
        column = user_input(i+1)

        if i % 2 == 0 and matrix[row][column] == "-":
            matrix[row][column] = player_1
            display.display_matrix(matrix)
            row_result = rowcheck.row_check(matrix, row, column, player_1)
            column_result = columncheck.column_check(matrix, row, column, player_1)
            diagonal_result = diagonal.diagonal_check(matrix, player_1)
            if row_result or column_result or diagonal_result:
                print('Game Over')
                print('Player 1 won the match')
                result = False
                break

        elif i % 2 != 0 and matrix[row][column] == "-":
            matrix[row][column] = player_2
            display.display_matrix(matrix)
            row_result = rowcheck.row_check(matrix, row, column, player_2)
            column_result = columncheck.column_check(matrix, row, column, player_2)
            diagonal_result = diagonal.diagonal_check(matrix, player_2)
            if row_result or column_result or diagonal_result:
                print('Game Over')
                print('Player 2 won the match')
                result = False
                break
        else:
            print("This position is already occupied")
