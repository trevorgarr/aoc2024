"""
2024 AOC Day X:
"""

import time


def parse_input(input):
    return [int(x) for x in input[0].split()]


def part_one(parsed_input):
    # good for small inputs ONLY
    return dp_stones(parsed_input, 25)


def part_two(parsed_input):
    # good for small inputs ONLY
    return dp_stones(parsed_input, 75)


def blink_at_stones(input_stones, blink_count):
    # iterative approach
    stones = input_stones
    for i in range(blink_count):
        new_stones = []
        for idx, stone in enumerate(stones):
            if stone == 0:
                new_stones.append(1)
            elif len(str(stone)) % 2 == 0:
                stone_str = str(stone)
                midpoint = len(stone_str) // 2
                new_stones.append(int(stone_str[:midpoint]))
                new_stones.append(int(stone_str[midpoint:]))
            else:
                new_stones.append(stone * 2024)
        stones = new_stones
    return len(stones)


def dp_stones(parsed_input, depth):
    cache = {}

    def count_stones(stone, depth):
        if depth == 0:
            return 1
        elif (stone, depth) in cache:
            return cache[(stone, depth)]
        elif stone == 0:
            stones = count_stones(1, depth-1)
        elif len(str(stone)) % 2 == 0:
            stone_str = str(stone)
            midpoint = len(stone_str) // 2
            stones = count_stones(int(
                stone_str[:midpoint]), depth-1) + count_stones(int(stone_str[midpoint:]), depth-1)
        else:
            stones = count_stones(stone * 2024, depth-1)
        cache[(stone, depth)] = stones
        return stones

    count = 0
    for stone in parsed_input:
        count += count_stones(stone, depth)
    return count


if __name__ == "__main__":
    f = open("day11.txt", "r")
    data = f.read()
    input = data.splitlines()
    parsed_input = parse_input(input)
    print("PARSED_INPUT: ", parsed_input)
    p1_start_time = time.time()
    print("PART ONE =", part_one(parsed_input))
    print("--- %s seconds ---" % round((time.time() - p1_start_time), 4))
    p2_start_time = time.time()
    print("PART TWO =", part_two(parsed_input))
    print("--- %s seconds ---" % round((time.time() - p2_start_time), 4))

    f.close()
