"""
2024 AOC Day X:
"""


def parse_input(input):
    matrix = []
    for line in input:
        matrix.append(list(line))
    return matrix


xmas_len = len("XMAS")
mas_len = len("MAS")


def part_one(grid):
    count = 0
    num_rows = len(grid)
    for row_idx in range(num_rows):
        row = grid[row_idx]
        num_cols = len(row)
        for col_idx in range(num_cols):
            # horizontal
            if (
                col_idx <= num_cols - xmas_len
                and grid[row_idx][col_idx] == "X"
                and grid[row_idx][col_idx + 1] == "M"
                and grid[row_idx][col_idx + 2] == "A"
                and grid[row_idx][col_idx + 3] == "S"
            ):
                count += 1
            # horizontal reversed
            if (
                col_idx <= num_cols - xmas_len
                and grid[row_idx][col_idx] == "S"
                and grid[row_idx][col_idx + 1] == "A"
                and grid[row_idx][col_idx + 2] == "M"
                and grid[row_idx][col_idx + 3] == "X"
            ):
                count += 1
            # vertical
            if (
                row_idx <= num_rows - xmas_len
                and grid[row_idx][col_idx] == "X"
                and grid[row_idx + 1][col_idx] == "M"
                and grid[row_idx + 2][col_idx] == "A"
                and grid[row_idx + 3][col_idx] == "S"
            ):
                count += 1
            # vertical reversed
            if (
                row_idx <= num_rows - xmas_len
                and grid[row_idx][col_idx] == "S"
                and grid[row_idx + 1][col_idx] == "A"
                and grid[row_idx + 2][col_idx] == "M"
                and grid[row_idx + 3][col_idx] == "X"
            ):
                count += 1
            # Downward Diagonal
            if (
                row_idx <= num_rows - xmas_len
                and col_idx <= num_cols - xmas_len
                and grid[row_idx][col_idx] == "X"
                and grid[row_idx + 1][col_idx + 1] == "M"
                and grid[row_idx + 2][col_idx + 2] == "A"
                and grid[row_idx + 3][col_idx + 3] == "S"
            ):
                count += 1
            # Downward Diagonal reversed
            if (
                row_idx <= num_rows - xmas_len
                and col_idx <= num_cols - xmas_len
                and grid[row_idx][col_idx] == "S"
                and grid[row_idx + 1][col_idx + 1] == "A"
                and grid[row_idx + 2][col_idx + 2] == "M"
                and grid[row_idx + 3][col_idx + 3] == "X"
            ):
                count += 1
            # Upward Diagonal
            if (
                row_idx >= (xmas_len - 1)
                and col_idx <= num_cols - xmas_len
                and grid[row_idx][col_idx] == "X"
                and grid[row_idx - 1][col_idx + 1] == "M"
                and grid[row_idx - 2][col_idx + 2] == "A"
                and grid[row_idx - 3][col_idx + 3] == "S"
            ):
                count += 1
            # Upward Diagonal reversed
            if (
                row_idx >= (xmas_len - 1)
                and col_idx <= num_cols - xmas_len
                and grid[row_idx][col_idx] == "S"
                and grid[row_idx - 1][col_idx + 1] == "A"
                and grid[row_idx - 2][col_idx + 2] == "M"
                and grid[row_idx - 3][col_idx + 3] == "X"
            ):
                count += 1
    return count


def part_two(grid):
    count = 0
    num_rows = len(grid)
    for row_idx in range(num_rows):
        row = grid[row_idx]
        num_cols = len(row)
        for col_idx in range(num_cols):
            # M S
            #  A
            # M S
            if (
                col_idx <= num_cols - mas_len
                and row_idx <= num_rows - mas_len
                and grid[row_idx][col_idx] == "M"
                and grid[row_idx + 2][col_idx] == "M"
                and grid[row_idx + 1][col_idx + 1] == "A"
                and grid[row_idx][col_idx + 2] == "S"
                and grid[row_idx + 2][col_idx + 2] == "S"
            ):
                count += 1
            # S S
            #  A
            # M M
            if (
                col_idx <= num_cols - mas_len
                and row_idx <= num_rows - mas_len
                and grid[row_idx][col_idx] == "S"
                and grid[row_idx + 2][col_idx] == "M"
                and grid[row_idx + 1][col_idx + 1] == "A"
                and grid[row_idx][col_idx + 2] == "S"
                and grid[row_idx + 2][col_idx + 2] == "M"
            ):
                count += 1
            # M M
            #  A
            # S S
            if (
                col_idx <= num_cols - mas_len
                and row_idx <= num_rows - mas_len
                and grid[row_idx][col_idx] == "M"
                and grid[row_idx + 2][col_idx] == "S"
                and grid[row_idx + 1][col_idx + 1] == "A"
                and grid[row_idx][col_idx + 2] == "M"
                and grid[row_idx + 2][col_idx + 2] == "S"
            ):
                count += 1
            # S M
            #  A
            # S M
            if (
                col_idx <= num_cols - mas_len
                and row_idx <= num_rows - mas_len
                and grid[row_idx][col_idx] == "S"
                and grid[row_idx + 2][col_idx] == "S"
                and grid[row_idx + 1][col_idx + 1] == "A"
                and grid[row_idx][col_idx + 2] == "M"
                and grid[row_idx + 2][col_idx + 2] == "M"
            ):
                count += 1
    return count


if __name__ == "__main__":
    f = open("day4.txt", "r")
    data = f.read()
    input = data.splitlines()
    parsed_input = parse_input(input)
    print("PARSED INPUT: ", parsed_input)
    print("PART ONE =", part_one(parsed_input))
    print("PART TWO =", part_two(parsed_input))
    f.close()
