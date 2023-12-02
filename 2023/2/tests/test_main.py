# Using PyTest
from main import *


def test_part1():
    lines = read_file_into_lines("test-input.txt")

    success_ids = []  # int array, iterate and sum all values

    for line in lines:
        if determine_success(line):
            success_ids.append(find_id(line))

    assert sum_array(success_ids) == 8


def test_part2():
    lines = read_file_into_lines("test-input.txt")

    powers = []  # Part B powers of each set of minimum values

    for line in lines:
        powers.append(power_of_cube_set(determine_minimum(line)))

    assert sum_array(powers) == 2286
