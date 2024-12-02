"""
2024 AOC Day 2:
"""


def parse_input(input):
    output = []
    for row in input:
        split_row = row.split()
        output.append([int(x) for x in split_row])
    return output


def part_one(parsed_input):
    num_safe = 0
    for row in parsed_input:
        if is_row_safe(row):
            num_safe += 1
    return num_safe


def part_two(parsed_input):
    num_safe = 0
    for row in parsed_input:
        if is_row_safe(row):
            num_safe += 1
        else:
            for i in range(len(row)):
                adjust_row = row[:i] + row[i + 1 :]
                if is_row_safe(adjust_row):
                    num_safe += 1
                    break
    return num_safe


def is_row_safe(row):
    safe_row = True
    if row != sorted(row) and row != sorted(row, reverse=True):
        safe_row = False
    for i in range(1, len(row)):
        diff = abs(row[i] - row[i - 1])
        if diff < 1 or diff > 3:
            safe_row = False
    return safe_row


if __name__ == "__main__":
    f = open("day2.txt", "r")
    data = f.read()
    input = data.splitlines()
    parsed_input = parse_input(input)
    print("PARSED INPUT: ", parsed_input)
    print("PART ONE =", part_one(parsed_input))
    print("PART TWO =", part_two(parsed_input))
    f.close()
