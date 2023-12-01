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
def match_num_pattern(concat):
    pattern = r'(?=(zero|one|two|three|four|five|six|seven|eight|nine)\b)\w+'

    return re.findall(pattern, concat, flags=re.IGNORECASE)

def match_num_pattern_reversed(concat):
    pattern = r'(?=(orez|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin)\b)\w+'

    return re.findall(pattern, concat, flags=re.IGNORECASE)

def find_digit_words(line, reversed):
    concat = ""

    for char in line:
        # If it is a number already, then return!
        if char.isdigit():
            return char

        else:
            # Concatenate the string until a number matches the regex
            concat += char
            # Use the correct pattern matching
            if reversed:
                number = match_num_pattern_reversed(concat)
                # If we have found a number then stop looking!
                if number.__len__() == 1:
                    print(line, concat, words_to_numbers[number[0][::-1]])
                    return words_to_numbers[number[0][::-1]]
            else:
                number = match_num_pattern(concat)
                # If we have found a number then stop looking!
                if number.__len__() == 1:
                    print(line, concat, words_to_numbers[number[0]])
                    return words_to_numbers[number[0]]

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
    matrix = read_file_into_matrix("input.txt")

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