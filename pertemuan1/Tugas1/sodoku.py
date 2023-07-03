def solve_sudoku(board):
    if not find_empty_cell(board):
        return True
    
    row, col = find_empty_cell(board)
    for num in range(1, 10):
        if is_valid_move(board, row, col, num):
            board[row][col] = num

            if solve_sudoku(board):
                return True

            board[row][col] = 0

    return False

def find_empty_cell(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return row, col
    return None

def is_valid_move(board, row, col, num):
    # Cek baris
    for i in range(9):
        if board[row][i] == num:
            return False

    # Cek kolom
    for i in range(9):
        if board[i][col] == num:
            return False

    # Cek kotak 3x3
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True

def print_board(board):
    for row in range(9):
        for col in range(9):
            print(board[row][col], end=" ")
        print()

# Contoh pemanggilan fungsi
# Masukkan Sudoku ke dalam bentuk matriks 9x9
sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

if solve_sudoku(sudoku_board):
    print("Solusi ditemukan:")
    print_board(sudoku_board)
else: print("Tidak ada solusi yang ditemukan.")
