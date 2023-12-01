# Using PyTest
from alternative import *

def test_part1():
    matrix = read_file_into_matrix("test-input-a.txt")

    calibration_values_a = []
    for line in matrix:
        backwards = list(reversed(line))

        calibration_values_a.append(
            decode_calibration_value(find_digit(line),
            find_digit(backwards)))

    assert  calculate_summed_calibration_value(calibration_values_a) == 142

def test_part2():
    matrix = read_file_into_matrix("test-input-b.txt")

    calibration_values_b = []
    for line in matrix:
        backwards = list(reversed(line))

        calibration_values_b.append(
            decode_calibration_value(find_digit_words(line),
            find_digit_words(backwards)))

    assert  calculate_summed_calibration_value(calibration_values_b) == 281