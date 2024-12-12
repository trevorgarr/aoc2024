"""
2024 AOC Day 10:
"""

row_len = 0
col_len = 0


def parse_input(input):
    grid = [[int(x) for x in list(row)] for row in input]
    return grid


def part_one(grid):
    row_len = len(grid)
    col_len = len(grid[0])
    score = 0
    for idx_r, row in enumerate(grid):
        for idx_c, val in enumerate(row):
            if val == 0:
                print("outer iter")
                seen = [0]
                score += find_path(grid, idx_r, idx_c, seen)
    return score


def find_path(grid, idx_r, idx_c, seen):
    row_len = len(grid)
    col_len = len(grid[0])
    print(idx_r, idx_c, seen)
    if seen == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
        return 1

    sum = 0
    # look down
    if (idx_r < row_len - 1):
        next_val = grid[idx_r + 1][idx_c]
        if next_val == seen[-1] + 1:
            seen.append(next_val)
            sum += find_path(grid, idx_r + 1, idx_c, seen)
    # look up
    if (idx_r > 0):
        next_val = grid[idx_r - 1][idx_c]
        if next_val == seen[-1] + 1:
            seen.append(next_val)
            sum += find_path(grid, idx_r - 1, idx_c, seen)
    # look right
    if (idx_c < col_len - 1):
        next_val = grid[idx_r][idx_c + 1]
        if next_val == seen[-1] + 1:
            seen.append(next_val)
            sum += find_path(grid, idx_r, idx_c + 1, seen)
    # look left
    if (idx_c > 0):
        next_val = grid[idx_r][idx_c - 1]
        if next_val == seen[-1] + 1:
            seen.append(next_val)
            sum += find_path(grid, idx_r, idx_c - 1, seen)
    return sum


def find_unique_path(grid, idx_r, idx_c, seen):
    row_len = len(grid)
    col_len = len(grid[0])
    print(idx_r, idx_c, seen)
    if seen == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
        return 1

    # look down
    if (idx_r < row_len - 1):
        next_val = grid[idx_r + 1][idx_c]
        if next_val == seen[-1] + 1:
            seen.append(next_val)
            return find_unique_path(grid, idx_r + 1, idx_c, seen)
    # look up
    if (idx_r > 0):
        next_val = grid[idx_r - 1][idx_c]
        if next_val == seen[-1] + 1:
            seen.append(next_val)
            return find_unique_path(grid, idx_r - 1, idx_c, seen)
    # look right
    if (idx_c < col_len - 1):
        next_val = grid[idx_r][idx_c + 1]
        if next_val == seen[-1] + 1:
            seen.append(next_val)
            return find_unique_path(grid, idx_r, idx_c + 1, seen)
    # look left
    if (idx_c > 0):
        next_val = grid[idx_r][idx_c - 1]
        if next_val == seen[-1] + 1:
            seen.append(next_val)
            return find_unique_path(grid, idx_r, idx_c - 1, seen)
    return 0


def part_two(parsed_input):
    return -1


if __name__ == "__main__":
    f = open("test.txt", "r")
    data = f.read()
    input = data.splitlines()
    parsed_input = parse_input(input)
    print("PARSED_INPUT: ", parsed_input)
    print("PART ONE =", part_one(parsed_input))
    print("PART TWO =", part_two(parsed_input))
    f.close()
