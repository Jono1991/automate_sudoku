

def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)  # row, col

    return None

def valid_move(board, digit, position):
    # Check if the digit is not present in the same row
    if digit in board[position[0]]:
        return False

    # Check if the digit is not present in the same column
    if digit in [board[i][position[1]] for i in range(9)]:
        return False

    # Check if the digit is not present in the same 3x3 box
    box_start_row, box_start_col = 3 * (position[0] // 3), 3 * (position[1] // 3)
    for i in range(box_start_row, box_start_row + 3):
        for j in range(box_start_col, box_start_col + 3):
            if board[i][j] == digit and (i, j) != position:
                return False

    # The move is valid
    return True

def solve_sudoku(board):
    # Find the first empty cell on the board
    empty_cell = find_empty(board)

    # If no empty cells are found, the board is solved
    if not empty_cell:
        return True
    else:
        row, col = empty_cell

    # Try each digit from 1 to 9
    for digit in range(1, 10):
        if valid_move(board, digit, (row, col)):
            # If the digit is valid, place it on the board
            board[row][col] = digit

            # Recursively attempt to modules the updated board
            if solve_sudoku(board):
                return True

            # If placing the digit leads to an invalid solution, backtrack
            board[row][col] = 0

    # No valid digit found, backtrack to the previous empty cell
    return False



