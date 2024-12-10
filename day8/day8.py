"""
2024 AOC Day 8:
"""

from collections import defaultdict
import numpy as np


def parse_input(grid):
    output = defaultdict(list)
    for idx_r, row in enumerate(grid):
        for idx_c, col in enumerate(row):
            if grid[idx_r][idx_c] != ".":
                output[grid[idx_r][idx_c]].append([idx_r, idx_c])
    return output


def part_one(parsed_input, num_rows, num_cols):
    anti_nodes = set()
    for node in parsed_input:
        coords = parsed_input[node]
        for i in range(len(coords)):
            for j in range(i):
                x1, y1 = coords[i][0], coords[i][1]
                x2, y2 = coords[j][0], coords[j][1]
                # P1 - P2
                get_anti_node(
                    x1, y1, x2, y2, num_rows, num_cols, anti_nodes)
                # P2 - P1
                get_anti_node(
                    x2, y2, x1, y1, num_rows, num_cols, anti_nodes)
    return len(anti_nodes)


def get_anti_node(x1, y1, x2, y2, num_rows, num_cols, anti_nodes):
    node_x1 = x1 + (x1 - x2)
    node_y1 = y1 + (y1 - y2)
    if node_x1 >= 0 and node_x1 < num_rows and node_y1 >= 0 and node_y1 < num_cols:
        anti_nodes.add((node_x1, node_y1))
    return anti_nodes


def part_two(parsed_input, num_rows, num_cols):
    anti_nodes = set()
    for node in parsed_input:
        coords = parsed_input[node]
        for i in range(len(coords)):
            for j in range(i):
                x1, y1 = coords[i][0], coords[i][1]
                x2, y2 = coords[j][0], coords[j][1]
                # P1 - P2
                get_all_anti_nodes(
                    x1, y1, x2, y2, num_rows, num_cols, anti_nodes)
                # P2 - P1
                get_all_anti_nodes(
                    x2, y2, x1, y1, num_rows, num_cols, anti_nodes)
    return len(anti_nodes)


def get_all_anti_nodes(x1, y1, x2, y2, num_rows, num_cols, anti_nodes):
    node_x1 = x1 + (x1 - x2)
    node_y1 = y1 + (y1 - y2)
    # All antennas are anti nodes now
    anti_nodes.add((x1, y1))
    while node_x1 >= 0 and node_x1 < num_rows and node_y1 >= 0 and node_y1 < num_cols:
        anti_nodes.add((node_x1, node_y1))
        node_x1 += (x1 - x2)
        node_y1 += (y1 - y2)
    return anti_nodes


if __name__ == "__main__":
    f = open("day8.txt", "r")
    data = f.read()
    input = data.splitlines()
    parsed_input = parse_input(input)
    print("PARSED_INPUT: ", parsed_input)
    print("PART ONE =", part_one(parsed_input, len(input), len(input[0])))
    print("PART TWO =", part_two(parsed_input,
          len(input), len(input[0])))
    f.close()
