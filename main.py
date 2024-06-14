import random

def print_board(board):
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < 2:  
            print("-" * 9)

def check_winner(board, player):
    # Check rows
    for row in board:
        if all([cell == player for cell in row]):
            return True
    # Check columns
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    # Check diagonals
    if all([board[i][i] == player for i in range(3)]):
            return True
    if all([board[i][2 - i] == player for i in range(3)]):
            return True
    return False

def is_draw(board):
    return all([cell in ["X", "O"] for row in board for cell in row])

def player_move(board):
    while True:
        try:
            row = int(input("Enter the row (0, 1, or 2): "))
            col = int(input("Enter the column (0, 1, or 2): "))
            if board[row][col] == " ":
                board[row][col] = "X"
                break
            else:
                print("That cell is already taken. Try again.")
        except (IndexError, ValueError):
            print("Invalid input. Enter row and column as 0, 1, or 2.")

def computer_move(board):
    empty_cells = [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]
    row, col = random.choice(empty_cells)
    board[row][col] = "O"

def tic_tac_toe():
    while True:
        board = [[" " for _ in range(3)] for _ in range(3)]

        while True:
            print_board(board)

            # Player move
            player_move(board)
            if check_winner(board, "X"):
                print_board(board)
                print("Congratulations! You win!")
                break
            if is_draw(board):
                print_board(board)
                print("It's a draw!")
                break

            # Computer move
            computer_move(board)
            if check_winner(board, "O"):
                print_board(board)
                print("Computer wins! Better luck next time.")
                break
            if is_draw(board):
                print_board(board)
                print("It's a draw!")
                break

        while True:
            play_again = input("Do you want to play another game? (yes/no): ").strip().lower()
            if play_again in ["yes", "no"]:
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

        if play_again == "no":
            print("Thank you for playing Tic Tac Toe!")
            break

tic_tac_toe()