
import random

# Function to calculate heuristic: the number of attacking pairs of queens
def calculate_heuristic(board):
    conflicts = 0
    n = len(board)
    for i in range(n):
        for j in range(i + 1, n):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                conflicts += 1
    return conflicts

# Function to get the best move for a queen in a specific column
def get_best_move(board, col):
    n = len(board)
    min_conflicts = calculate_heuristic(board)
    best_row = board[col]

    for row in range(n):
        if row != board[col]:
            new_board = list(board)
            new_board[col] = row
            conflicts = calculate_heuristic(new_board)
            if conflicts < min_conflicts:
                min_conflicts = conflicts
                best_row = row

    return best_row

# Function to solve 8-Queens using Hill Climbing with Random Restart
def solve_n_queens(n=8):
    board = [random.randint(0, n - 1) for _ in range(n)]

    while True:
        heuristic = calculate_heuristic(board)

        # If there are no conflicts, a solution is found
        if heuristic == 0:
            return board

        for col in range(n):
            best_row = get_best_move(board, col)
            board[col] = best_row

        # Random restart if stuck in local minima
        if calculate_heuristic(board) >= heuristic:
            board = [random.randint(0, n - 1) for _ in range(n)]

# Helper function to print the board
def print_board(board):
    n = len(board)
    for row in range(n):
        line = ""
        for col in range(n):
            if board[col] == row:
                line += "Q "
            else:
                line += ". "
        print(line)
    print()

# Example usage
solution = solve_n_queens()
print("One possible solution for the 8-Queens problem:")
print_board(solution)
