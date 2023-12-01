# Trebuchet. Oh no our calibration is wrong!
import re

words_to_numbers = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    'zero': '0',
    'eno': '1',
    'owt': '2',
    'eerht': '3',
    'ruof': '4',
    'evif': '5',
    'xis': '6',
    'neves': '7',
    'thgie': '8',
    'enin': '9',
    'orez': '0'
}

def read_file_into_matrix(file_name):
    matrix = []
    with open(file_name, 'r') as file:

        for line in file:
            row = list(line.strip())
            matrix.append(row)

    return matrix

## Find Digit - Part A
def find_digit(line):
    for char in line:

        if char.isdigit():
            return char

    return None

## Find Digit - Part B
def find_digit_words(line, reversed):
    concat = ""

    for char in line:
        # If it is a number already, then return!
        if char.isdigit():
            return char

        else:
            # Concatenate the string until a number matches the dictionary
            # Make sure to consider that it may not be an exact match if it isn't the start or end
            concat += char
            for key in words_to_numbers:
                if key in concat:
                    return words_to_numbers[key]

    return None

def decode_calibration_value(first_digit, last_digit):
    return int(first_digit + last_digit)

def calculate_summed_calibration_value(calibration_values):
    sum = 0
    for i in calibration_values:
        sum = sum + i

    return sum

def main():
    print("Reading input file...")
    matrix = read_file_into_matrix("/home/claire/claire-fletcher/advent-of-code/2023/1/input.txt")

    print("Calulating first and last digits...")
    calibration_values_a, calibration_values_b = [], []
    for line in matrix:
        backwards = list(reversed(line))

        calibration_values_a.append(
            decode_calibration_value(find_digit(line),
            find_digit(backwards)))

        calibration_values_b.append(
            decode_calibration_value(find_digit_words(line, False),
            find_digit_words(backwards, True)))

    print("Final Result Part A: ",
        calculate_summed_calibration_value(calibration_values_a))
    print("Final Result Part B: ",
        calculate_summed_calibration_value(calibration_values_b))

if __name__ == "__main__":
    main()