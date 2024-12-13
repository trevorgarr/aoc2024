"""
2024 AOC Day 13:
"""
import re
import numpy as np
import time


def parse_input(input, offset):
    equations = []
    button_pattern = re.compile(r"X\+(\d+), Y\+(\d+)")
    prize_pattern = re.compile(r"X=(\d+), Y=(\d+)")
    for i in range(0, len(input), 4):
        A_vals = button_pattern.search(input[i])
        A_x_val, A_y_val = int(A_vals.group(1)), int(A_vals.group(2))

        B_vals = button_pattern.search(input[i+1])
        B_x_val, B_y_val = int(B_vals.group(1)), int(B_vals.group(2))

        P_vals = prize_pattern.search(input[i+2])
        P_x_val, P_y_val = int(P_vals.group(1)), int(P_vals.group(2))

        equations.append([(A_x_val, B_x_val, P_x_val + offset),
                         (A_y_val, B_y_val, P_y_val + offset)])

    return equations


def part_one(parsed_input):
    return get_score(parsed_input)


def part_two(parsed_input):
    return get_score(parsed_input)


def solve_system_of_eqs(x1, y1, p1, x2, y2, p2):
    # Solves the following system of equations:
    # x1 + y1 = p1
    # x2 + y2 = p2
    A = np.array([[x1, y1], [x2, y2]])
    b = np.array([p1, p2])
    return np.linalg.solve(A, b)


def get_score(parsed_input):
    score = 0
    for eq in parsed_input:
        A, B = solve_system_of_eqs(
            eq[0][0], eq[0][1], eq[0][2], eq[1][0], eq[1][1], eq[1][2])
        if round(A, 4).is_integer() and round(B, 4).is_integer():
            score += (A * 3) + (B * 1)
    return int(score)


if __name__ == "__main__":
    f = open("day13.txt", "r")
    data = f.read()
    input = data.splitlines()
    p1_start_time = time.time()
    parsed_input_p1 = parse_input(input, 0)
    print("PART ONE =", part_one(parsed_input_p1))
    print("--- %s seconds ---" % round((time.time() - p1_start_time), 4))
    p2_start_time = time.time()
    parsed_input_p2 = parse_input(input, 10000000000000)
    print("PART TWO =", part_two(parsed_input_p2))
    print("--- %s seconds ---" % round((time.time() - p2_start_time), 4))

    f.close()
