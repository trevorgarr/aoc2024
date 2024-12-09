"""
2024 AOC Day 7:
"""

from collections import defaultdict


def parse_input(input):
    output = defaultdict(list)
    for row in input:
        split = row.split(":")
        output[int(split[0].strip())] += [int(x) for x in split[1].split()]
    return output


def part_one(parsed_input):
    for pot_sum in parsed_input:
        print(pot_sum)
        print(parsed_input[pot_sum])
    return -1


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
