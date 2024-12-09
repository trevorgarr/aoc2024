"""
2024 AOC Day 6:
"""

import numpy as np


def parse_input(input):
    output = []
    for row in input:
        output.append(list(row))
    return output


def part_one(grid):
    num_rows = len(grid)
    num_cols = len(grid[0])
    direction, idx_r, idx_c = find_direction(grid)
    start_idx_r = idx_r
    start_idx_c = idx_c
    while 0 <= idx_r < num_rows and 0 <= idx_c < num_cols:
        if grid[idx_r][idx_c] == "#":
            if direction == "up":
                direction = "right"
                idx_r += 1
            elif direction == "left":
                idx_c += 1
                direction = "up"
            elif direction == "right":
                idx_c -= 1
                direction = "down"
            elif direction == "down":
                idx_r -= 1
                direction = "left"

        grid[idx_r][idx_c] = "X"

        if direction == "up":
            idx_r -= 1
        elif direction == "left":
            idx_c -= 1
        elif direction == "right":
            idx_c += 1
        elif direction == "down":
            idx_r += 1
    grid[start_idx_r][start_idx_c] = "^"
    return count_path(grid)


def find_direction(grid):
    direction = "up"
    for idx_r, row in enumerate(grid):
        for idx_c, col in enumerate(row):
            if grid[idx_r][idx_c] == "^":
                direction = "up"
                return direction, idx_r, idx_c
            if grid[idx_r][idx_c] == ">":
                direction = "right"
                return direction, idx_r, idx_c
            if grid[idx_r][idx_c] == "<":
                direction = "left"
                return direction, idx_r, idx_c
            if grid[idx_r][idx_c] == "v":
                direction = "down"
                return direction, idx_r, idx_c
    return direction


def count_path(grid):
    count = 0
    for idx_r, row in enumerate(grid):
        for idx_c, col in enumerate(row):
            if grid[idx_r][idx_c] == "X" or grid[idx_r][idx_c] == "^":
                count += 1
    return count


def part_two(grid):
    num_cycles = 0
    num_rows = len(grid)
    num_cols = len(grid[0])

    for idx_r, row in enumerate(grid):
        for idx_c, col in enumerate(row):
            if grid[idx_r][idx_c] == "^" or grid[idx_r][idx_c] == "X":
                seen = set()
                direction, rs_idx, cs_idx = find_direction(grid)
                before = grid[idx_r][idx_c]
                grid[idx_r][idx_c] = "#"
                while 0 <= rs_idx < num_rows and 0 <= cs_idx < num_cols:
                    seen.add((direction, rs_idx, cs_idx))
                    if grid[rs_idx][cs_idx] == "#":
                        if direction == "up":
                            direction = "right"
                            rs_idx += 1
                        elif direction == "left":
                            cs_idx += 1
                            direction = "up"
                        elif direction == "right":
                            cs_idx -= 1
                            direction = "down"
                        elif direction == "down":
                            rs_idx -= 1
                            direction = "left"

                    if direction == "up":
                        rs_idx -= 1
                    elif direction == "left":
                        cs_idx -= 1
                    elif direction == "right":
                        cs_idx += 1
                    elif direction == "down":
                        rs_idx += 1
                    if (direction, rs_idx, cs_idx) in seen:
                        num_cycles += 1
                        break
                grid[idx_r][idx_c] = before
    return num_cycles


if __name__ == "__main__":
    f = open("day6.txt", "r")
    data = f.read()
    input = data.splitlines()
    parsed_input = parse_input(input)
    print("PARSED_INPUT: ", print(np.matrix(parsed_input)))
    print("PART ONE =", part_one(parsed_input))
    print("PART TWO =", part_two(parsed_input))
    f.close()
