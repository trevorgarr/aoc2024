"""
2024 AOC Day 10:
"""
import numpy as np


def parse_input(input):
    grid = [[int(x) for x in list(row)] for row in input]
    return grid


def part_one(grid):
    row_len = len(grid)
    col_len = len(grid[0])

    def find_path(idx_r, idx_c, target):
        if idx_r >= row_len or idx_r < 0 or idx_c >= col_len or idx_c < 0 or grid[idx_r][idx_c] != target:
            return set()

        if target == 9:
            return {(idx_r, idx_c)}

        # mark visited
        grid[idx_r][idx_c] = -1

        score = set()
        # look down
        score.update(find_path(idx_r + 1, idx_c, target+1))
        # look up
        score.update(find_path(idx_r - 1, idx_c, target+1))
        # look right
        score.update(find_path(idx_r, idx_c + 1, target+1))
        # look left
        score.update(find_path(idx_r, idx_c - 1, target+1))

        # backtrack
        grid[idx_r][idx_c] = target

        return score

    total_score = 0
    for idx_r, row in enumerate(grid):
        for idx_c, val in enumerate(row):
            if val == 0:
                indiv_score = find_path(idx_r, idx_c, 0)
                total_score += len(indiv_score)
    return total_score


def part_two(grid):
    row_len = len(grid)
    col_len = len(grid[0])

    def find_path(idx_r, idx_c, target):
        if idx_r >= row_len or idx_r < 0 or idx_c >= col_len or idx_c < 0 or grid[idx_r][idx_c] != target:
            return 0

        if target == 9:
            return 1

        grid[idx_r][idx_c] = -1
        sum = 0
        # look down
        sum += find_path(idx_r + 1, idx_c, target+1)
        # look up
        sum += find_path(idx_r - 1, idx_c, target+1)
        # look right
        sum += find_path(idx_r, idx_c + 1, target+1)
        # look left
        sum += find_path(idx_r, idx_c - 1, target+1)

        grid[idx_r][idx_c] = target

        return sum

    score = 0
    for idx_r, row in enumerate(grid):
        for idx_c, val in enumerate(row):
            if val == 0:
                score += find_path(idx_r, idx_c, 0)
    return score


if __name__ == "__main__":
    f = open("day10.txt", "r")
    data = f.read()
    input = data.splitlines()
    parsed_input = parse_input(input)
    print("PARSED_INPUT: ", parsed_input)
    print("PART ONE =", part_one(parsed_input))
    print("PART TWO =", part_two(parsed_input))
    f.close()
