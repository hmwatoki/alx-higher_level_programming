#!/usr/bin/python3
import sys
def is_safe(board, row, col, n):
    return not any(board[i][col] == 1 for i in range(row)) \
        and not any(board[i][j] == 1 for i, j in zip(range(row, -1, -1), range(col, -1, -1))) \
        and not any(board[i][j] == 1 for i, j in zip(range(row, -1, -1), range(col, n)))
def solve_n_queens(board, row, n, solutions):
    if row == n:
        solution = []
        for i in range(n):
            for j in range(n):
                if board[i][j] == 1:
                    solution.append([i, j])
        if all(check_two_queens(solution[i], solution[j]) for i in range(len(solution)) for j in range(i+1, len(solution))):

            solutions.append(solution)
        return
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve_n_queens(board, row + 1, n, solutions)
            board[row][col] = 0
def print_solutions(solutions):
    for solution in solutions:
        print(solution)
def check_two_queens(new_queen_position, other_queen_position):
    if new_queen_position[0] == other_queen_position[0] or new_queen_position[1] == other_queen_position[1]:
        # Check if new queen is in same row or column as other queen
        return False
    if new_queen_position[0] + new_queen_position[1] == other_queen_position[0] + other_queen_position[1]:
        # Check if new queen is on same diagonal as other queen
        return False
    if new_queen_position[0] - new_queen_position[1] == other_queen_position[0] - other_queen_position[1]:
        # Check if new queen is on same diagonal as other queen
        return False
    return True
def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        return
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        return
    if n < 4:
        print("N must be at least 4")
        return
    board = [[0] * n for _ in range(n)]
    solutions = []
    solve_n_queens(board, 0, n, solutions)
    print_solutions(solutions)
if __name__ == "__main__":
    main()
