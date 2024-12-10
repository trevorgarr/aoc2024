"""
2024 AOC Day 7:
"""


def parse_input(input):
    output = []
    for row in input:
        split = row.split(":")
        output.append([int(split[0].strip())] + [int(x)
                                                 for x in split[1].split()])
    return output


def part_one(parsed_input):
    sum_valid = 0
    for row in parsed_input:
        target = row[0]
        nums = row[1:]
        if is_valid_p1(target, nums):
            sum_valid += target
    return sum_valid


def is_valid_p1(target, nums):
    if len(nums) == 1:
        return nums[0] == target
    if is_valid_p1(target, [nums[0] + nums[1]] + nums[2:]):
        return True
    if is_valid_p1(target, [nums[0] * nums[1]] + nums[2:]):
        return True
    return False


def part_two(parsed_input):
    sum_valid = 0
    for row in parsed_input:
        target = row[0]
        nums = row[1:]
        if is_valid_p2(target, nums):
            sum_valid += target
    return sum_valid


def is_valid_p2(target, nums):
    if len(nums) == 1:
        return nums[0] == target
    if is_valid_p2(target, [nums[0] + nums[1]] + nums[2:]):
        return True
    if is_valid_p2(target, [nums[0] * nums[1]] + nums[2:]):
        return True
    if is_valid_p2(target, [int(str(nums[0]) + str(nums[1]))] + nums[2:]):
        return True
    return False


if __name__ == "__main__":
    f = open("day7.txt", "r")
    data = f.read()
    input = data.splitlines()
    parsed_input = parse_input(input)
    print("PARSED_INPUT: ", parsed_input)
    print("PART ONE =", part_one(parsed_input))
    print("PART TWO =", part_two(parsed_input))
    f.close()
