def is_safe(board, row, col, n):
    # Check if it is safe to place a queen in the given row and column
    for i in range(row):
        if board[i][col] == 'X':
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'X':
            return False
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 'X':
            return False
    return True

def solve_n_queens(board, row, n):
    # Recursive function to place the queens on the board
    if row == n:
        return True
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 'X'
            if solve_n_queens(board, row+1, n):
                return True
            board[row][col] = 'O'
    return False

n = int(input("Enter the number of queens: "))
board = [['O' for i in range(n)] for j in range(n)]
if solve_n_queens(board, 0, n):
    print("Solution exists! The game board is:")
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=' ')
        print()
else:
    print("No solution exists for", n, "queens.")



