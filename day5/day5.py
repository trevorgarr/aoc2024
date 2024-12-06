"""
2024 AOC Day X:
"""

from collections import defaultdict


def parse_input(input):
    mappings = defaultdict(set)
    instrs = []

    for row in input:
        if "|" in row:
            split = row.split("|")
            mappings[split[0]].add(split[1])
        elif "," in row:
            instrs.append(row.split(","))

    return mappings, instrs


def part_one(mappings, instrs):
    # Mapping = value -> all values that must come after (before: after[])
    # Create a set of seen values.
    # For every value in a row of instructions, if any previously seen values
    # are in the current value's mapping entry (values that must come after)
    # the row is invalid.
    sum_mid_vals = 0
    for row in instrs:
        if check_row_valid(row, mappings):
            sum_mid_vals += int(row[len(row) // 2])
    return sum_mid_vals


def part_two(mappings, instrs):
    # Use a modified bubble sort to re-sort the row if it is invalid
    # For every invalid row if a pair of values are in the mappings and
    # mapped to eachother, swap them in order to ensure the correct order
    sum_mid_vals = 0
    for row in instrs:
        valid_row = check_row_valid(row, mappings)
        while not valid_row:
            for i in range(len(row)):
                for j in range(i + 1, len(row)):
                    if (row[j]) in mappings and row[i] in mappings[row[j]]:
                        row[j], row[i] = row[i], row[j]
            valid_row = check_row_valid(row, mappings)
        sum_mid_vals += int(row[len(row) // 2])
    return sum_mid_vals


def check_row_valid(row, mappings):
    is_valid = True
    seen = set()
    for val in row:
        after = mappings[val]
        if len(seen.intersection(after)) > 0:
            is_valid = False
        seen.add(val)
    return is_valid


if __name__ == "__main__":
    f = open("day5.txt", "r")
    data = f.read()
    input = data.splitlines()
    mappings, instrs = parse_input(input)
    part_one = part_one(mappings, instrs)
    print("MAPPINGS: ", mappings)
    print("INSTRS: ", instrs)
    print("PART ONE =", part_one)
    print("PART TWO =", part_two(mappings, instrs) - part_one)
    f.close()
