"""
2024 AOC Day 3:
"""

import re


def parse_input(input):
    return input


def part_one(parsed_input):
    pattern = "mul\([0-9]+,[0-9]+\)"
    matched_values = find_matches(pattern, parsed_input)

    total = 0
    for match in matched_values:
        total += multiply_values(match)

    return total


def part_two(parsed_input):
    pattern = "mul\([0-9]+,[0-9]+\)|do\(\)|don't\(\)"
    matched_values = find_matches(pattern, parsed_input)

    total = 0
    should_multiply = True
    for match in matched_values:
        if match == "don't()":
            should_multiply = False
        elif match == "do()":
            should_multiply = True
        elif should_multiply:
            total += multiply_values(match)
    return total


def find_matches(pattern, parsed_input):
    matched_values = []
    for line in parsed_input:
        matches = re.findall(pattern, line, flags=re.IGNORECASE)
        matched_values += matches
    return matched_values


def multiply_values(match):
    match = match.replace("mul(", "").replace(")", "")
    [first, second] = match.split(",")
    return int(first) * int(second)


if __name__ == "__main__":
    f = open("day3.txt", "r")
    data = f.read()
    input = data.splitlines()
    parsed_input = parse_input(input)
    print("PART ONE =", part_one(parsed_input))
    print("PART TWO =", part_two(parsed_input))
    f.close()
