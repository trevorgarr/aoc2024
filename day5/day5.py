"""
2024 AOC Day X:
"""

from collections import defaultdict


def parse_input(input):
    return input


def part_one(parsed_input):
    mappings = defaultdict(list)
    return -1


def part_two(parsed_input):
    return -1


if __name__ == "__main__":
    f = open("dayX.txt", "r")
    data = f.read()
    input = data.splitlines()
    parsed_input = parse_input(input)
    print("PART ONE =", part_one(parsed_input))
    print("PART TWO =", part_two(parsed_input))
    f.close()
