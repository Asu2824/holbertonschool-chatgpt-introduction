def print_board(board):
    # Print the board with vertical and horizontal separators
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    # Check for a winner in rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check for a winner in columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check for a winner in diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def check_tie(board):
    # Check if the board is full and there's no winner
    for row in board:
        for cell in row:
            if cell == " ":
                return False  # If there's any empty space, the game isn't tied yet
    return True  # All spaces are filled and no winner, it's a tie

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]  # Initialize an empty 3x3 board
    player = "X"
    
    while True:
        print_board(board)  # Print the current board
        
        # Input validation: Ensure the row and column are integers within the range [0, 2]
        while True:
            try:
                row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
                col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
                if row not in range(3) or col not in range(3):
                    print("Invalid input! Row and column must be between 0 and 2.")
                elif board[row][col] != " ":
                    print("That spot is already taken! Try again.")
                else:
                    break  # Valid input, break the loop
            except ValueError:
                print("Invalid input! Please enter integers only.")

        # Place

