"""
2024 AOC Day 9:
"""


def parse_input(input):
    row = input[0]
    output = []
    # return tuples of format (ID, size)
    for i in range(0, len(row) - 1, 2):
        id = i // 2
        file_size = int(row[i])
        empty_size = int(row[i+1])
        output.append((id, file_size))
        output.append((None, empty_size))
    if len(row) % 2 != 0:
        output.append((len(row) // 2, int(row[len(row) - 1])))
    return output


def part_one(parsed_input):
    disk = []
    for file_id, size in parsed_input:
        if file_id is None:
            disk.extend([None] * size)
        else:
            disk.extend([file_id] * size)

    left = 0
    right = len(disk) - 1
    while left < right:
        if disk[left] is None and disk[right] is not None:
            disk[left], disk[right] = disk[right], disk[left]
        if disk[right] is None:
            right -= 1
        if disk[left] is not None:
            left += 1

    output = 0
    for i, d in enumerate(disk):
        if d is not None:
            output += d * i

    return output


def part_two(parsed_input):
    
    for right_idx in range(len(parsed_input))[::-1]:
        for left_idx in range(right_idx):
            right_val, right_size = parsed_input[right_idx]
            left_val, left_size = parsed_input[left_idx]
            if left_val is None and right_val is not None and left_size >= right_size:
                parsed_input[right_idx] = (None, right_size)
                parsed_input[left_idx] = (None, left_size - right_size)
                parsed_input.insert(left_idx, (right_val, right_size))

    disk = []
    for file_id, size in parsed_input:
        if file_id is None:
            disk.extend([None] * size)
        else:
            disk.extend([file_id] * size)

    output = 0
    for i, d in enumerate(disk):
        if d is not None:
            output += d * i
    return output


if __name__ == "__main__":
    f = open("day9.txt", "r")
    data = f.read()
    input = data.splitlines()
    parsed_input = parse_input(input)
    print("PARSED_INPUT: ", parsed_input)
    print("PART ONE =", part_one(parsed_input))
    print("PART TWO =", part_two(parsed_input))
    f.close()
