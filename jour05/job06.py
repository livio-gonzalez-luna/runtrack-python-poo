# Créer un programme qui modélise un plateau de jeu, carré, de n x n cases. 

# Placez sur ce plateau n dames de jeu d'échecs, de manière à ce qu’aucune dame ne puisse se “prendre”, quand cela est possible. 

# La valeur de n'est renseignée par l’utilisateur. 

# Quand cela est possible, le programme devra afficher dans le terminal le plateau de jeu avec le caractère ‘O’ pour les cases vides et le caractère ‘X’ pour représenter les dames.


def is_safe(board, row, col, n):
    # Check if it is safe to place a queen in the given row and column #
    for i in range(row):
        # Check if there is a queen in the same column #
        if board[i][col] == 'X':
            return False
    # Check if there is a queen in the same row #
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'X':
            return False
    # Check if there is a queen in the same diagonal #
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 'X':
            return False
    return True

def solve_n_queens(board, row, n):
    # Recursive function to place the queens on the board
    if row == n:
        return True
    # Place a queen in each column of the current row #
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 'X'
            # If the queen can be placed in the current row, place the queen in the next row #
            if solve_n_queens(board, row+1, n):
                return True
            # If the queen cannot be placed in the current row, backtrack and remove the queen from the current row #
            board[row][col] = 'O'
    return False

n = int(input("Enter the number of queens: "))
board = [['O' for i in range(n)] for j in range(n)]

# If a solution exists, print the board #
if solve_n_queens(board, 0, n):
    print("Solution exists! The game board is:")
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=' ')
        print()
# If a solution does not exist, print a message #
else:
    print("No solution exists for", n, "queens.")



