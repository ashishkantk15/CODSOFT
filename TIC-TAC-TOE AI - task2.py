# tictactoe_ai.py
import math

def print_board(board):
    for row in board:
        print(row)

def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != "_":
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != "_":
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "_":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "_":
        return board[0][2]
    return None

def is_full(board):
    return all(cell != "_" for row in board for cell in row)

def minimax(board, is_maximizing):
    winner = check_winner(board)
    if winner == "O":
        return 1
    elif winner == "X":
        return -1
    elif is_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == "_":
                    board[i][j] = "O"
                    score = minimax(board, False)
                    board[i][j] = "_"
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == "_":
                    board[i][j] = "X"
                    score = minimax(board, True)
                    board[i][j] = "_"
                    best_score = min(score, best_score)
        return best_score

def best_move(board):
    move = (-1, -1)
    best_score = -math.inf
    for i in range(3):
        for j in range(3):
            if board[i][j] == "_":
                board[i][j] = "O"
                score = minimax(board, False)
                board[i][j] = "_"
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

board = [["_"] * 3 for _ in range(3)]
while not check_winner(board) and not is_full(board):
    print_board(board)
    row = int(input("Enter row (0-2): "))
    col = int(input("Enter col (0-2): "))
    if board[row][col] == "_":
        board[row][col] = "X"
        if not check_winner(board) and not is_full(board):
            ai_row, ai_col = best_move(board)
            board[ai_row][ai_col] = "O"
print_board(board)
print("Winner:", check_winner(board) or "Draw")
