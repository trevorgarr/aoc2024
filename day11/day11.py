"""
2024 AOC Day X:
"""


def parse_input(input):
    return [int(x) for x in input[0].split()]


def part_one(parsed_input):
    return blink_at_stones(parsed_input, 25)


def part_two(parsed_input):
    return blink_at_stones(parsed_input, 75)


def blink_at_stones(input_stones, blink_count):
    stones = input_stones
    for i in range(blink_count):
        new_stones = []
        for idx, stone in enumerate(stones):
            if (stone == 0):
                new_stones.append(1)
            elif (len(str(stone)) % 2 == 0):
                stone_str = str(stone)
                midpoint = len(stone_str) // 2
                new_stones.append(int(stone_str[:midpoint]))
                new_stones.append(int(stone_str[midpoint:]))
            else:
                new_stones.append(stone * 2024)
        stones = new_stones
    return len(stones)


if __name__ == "__main__":
    f = open("day11.txt", "r")
    data = f.read()
    input = data.splitlines()
    parsed_input = parse_input(input)
    print("PARSED_INPUT: ", parsed_input)
    print("PART ONE =", part_one(parsed_input))
    print("PART TWO =", part_two(parsed_input))
    f.close()
