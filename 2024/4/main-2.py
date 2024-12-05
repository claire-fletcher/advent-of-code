# Day 4: Ceres Search - Part 2, X-Mas puzzle!

diag_1 = [(1, 1),(-1, -1)]
diag_2 = [(1, -1),(-1, 1)]


def read_file_into_lines(file_name):
    return [line.strip() for line in open(file_name, "r")]

def is_valid(i, j, m, n):
    return 0 <= i < m and 0 <= j < n

def check_diagonal(grid, row, col, diag, rows, cols):
    if not is_valid(row + diag[0][0], col + diag[0][1], rows, cols) or not is_valid(row + diag[1][0], col + diag[1][1], rows, cols):
        return False
    tmp1 = grid[row + diag[0][0]][col + diag[0][1]]
    tmp2 = grid[row + diag[1][0]][col + diag[1][1]]

    if (tmp1 == "M" and tmp2 == "S") or (tmp1 == "S" and tmp2 == "M"):
        return True

    return False

def search_x(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    for row in range(rows):
        for col in range(cols):
            if (
                grid[row][col] == "A"
                and check_diagonal(grid, row, col, diag_1, rows, cols)
                and check_diagonal(grid, row, col, diag_2, rows, cols)
            ):
                count += 1

    return count

def main():
    grid = read_file_into_lines("input.txt")
    total = search_x(grid)
    print("Answer Part A: ", total)

if __name__ == "__main__":
    main()