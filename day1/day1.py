"""
2024 AOC Day 1:
"""

from collections import Counter


def parse_input(input):
    left = []
    right = []
    for line in input:
        split_line = line.split()
        left.append(int(split_line[0]))
        right.append(int(split_line[1]))
    return left, right


def part_one(left, right):
    sorted_left, sorted_right = sorted(left), sorted(right)
    total = 0
    for i in range(0, max(len(sorted_left), len(sorted_right))):
        total += abs(sorted_left[i] - sorted_right[i])
    return total


def part_two(left, right):
    right_counts = Counter(right)
    similarity = 0
    for i in range(0, max(len(left), len(right))):
        similarity += left[i] * right_counts[left[i]]
    return similarity


if __name__ == "__main__":
    f = open("day1.txt", "r")
    data = f.read()
    input = data.splitlines()
    left, right = parse_input(input)
    print(left)
    print(right)
    print("PART ONE =", part_one(left, right))
    print("PART TWO =", part_two(left, right))
    f.close()
