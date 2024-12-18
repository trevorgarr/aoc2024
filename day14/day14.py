"""
2024 AOC Day X:
"""
import re
import numpy as np
import matplotlib.pyplot as plt


def parse_input(input):
    robots = []
    pos_pattern = re.compile(r"p=(-?\d+),(-?\d+)")
    vel_pattern = re.compile(r"v=(-?\d+),(-?\d+)")
    for row in input:
        split_row = row.split()
        pos = split_row[0]
        vel = split_row[1]

        pos_vals = pos_pattern.search(pos)
        pos_x_val, pos_y_val = int(pos_vals.group(1)), int(pos_vals.group(2))

        vel_vals = vel_pattern.search(vel)
        vel_x_val, vel_y_val = int(vel_vals.group(1)), int(vel_vals.group(2))

        robots.append([(pos_x_val, pos_y_val),
                       (vel_x_val, vel_y_val)])

    return robots


def part_one(parsed_input, max_x, max_y, t):
    quadrants = [0, 0, 0, 0]
    result = 1
    for robot in parsed_input:
        x, y = robot[0][0], robot[0][1]
        dx, dy = robot[1][0], robot[1][1]
        x = (x + t*dx) % max_x
        y = (y + t*dy) % max_y
        count_quadrants(x, y, max_x, max_y, quadrants)
    for quad in quadrants:
        result *= quad
    return result


def count_quadrants(x, y, max_x, max_y, quadrants):
    x_mid = max_x // 2
    y_mid = max_y // 2
    if x < x_mid and y < y_mid:
        quadrants[0] += 1
    elif x > x_mid and y < y_mid:
        quadrants[1] += 1
    elif x < x_mid and y > y_mid:
        quadrants[2] += 1
    elif x > x_mid and y > y_mid:
        quadrants[3] += 1


def part_two(parsed_input, max_x, max_y):
    # find the first unique set of coords (dumb luck that this creates the image lol)
    for i in range(10000):
        robots = locate_robots(parsed_input, max_x, max_y, i)
        if len(robots) == len(set(robots)):
            return i
    return "not found yet"


def locate_robots(parsed_input, max_x, max_y, t):
    robots = []
    for robot in parsed_input:
        x, y = robot[0][0], robot[0][1]
        dx, dy = robot[1][0], robot[1][1]
        x = (x + t*dx) % max_x
        y = (y + t*dy) % max_y
        robots.append((x, y))
    return robots


def make_xmas_image(parsed_input, max_x, max_y):
    image_loc = part_two(parsed_input, max_x, max_y)
    robots = locate_robots(parsed_input, max_x, max_y, image_loc)
    matrix = fetch_final_matrix(max_x, max_y, robots)
    plt.imshow(matrix)
    plt.show()


def fetch_final_matrix(max_x, max_y, robots):
    robot_map = [['.' for _ in range(max_x)] for _ in range(max_y)]

    for robot in robots:
        robot_map[robot[1]][robot[0]] = "X"
    return np.matrix(robot_map)


if __name__ == "__main__":
    f = open("day14.txt", "r")
    data = f.read()
    input = data.splitlines()
    parsed_input = parse_input(input)
    print("PARSED_INPUT: ", parsed_input)
    print("PART ONE =", part_one(parsed_input, 101, 103, 100))
    print("PART TWO =", part_two(parsed_input, 101, 103))
    make_xmas_image(parsed_input, 101, 103)
    f.close()

# 2,4 at 2,-3 in 11 x 7
# 4,1
# 6,5
# Q1:
#
