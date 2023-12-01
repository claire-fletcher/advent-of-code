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
    'zero': '0'
}

def read_file(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
    return lines

def read_file_into_matrix(file_name):
    matrix = []
    with open(file_name, 'r') as file:
        for line in file:
            row = list(line.strip())
            matrix.append(row)
    return matrix

def find_first_digit(line):

    grepped_string = ""

    for char in line:
        # If it is a number, then return!!
        if char.isdigit():
            return char
        else:
        # Concatenate the string until a number matches the regex
            grepped_string += char
            number = re.findall(r'(?=(zero|one|two|three|four|five|six|seven|eight|nine)\b)\w+',
                grepped_string, flags=re.IGNORECASE)
            if number.__len__() == 1:
                return words_to_numbers[number[0]]
    return None

def find_last_digit(line):

    line.reverse()

    grepped_string = ""

    for char in line:
        # If it is a number, then return!!
        if char.isdigit():
            return char
        else:
        # Concatenate the string until a number matches the regex
            grepped_string += char
            number = re.findall(r'(?=(orez|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin)\b)\w+',
                grepped_string, flags=re.IGNORECASE)
            if number.__len__() == 1:
                return words_to_numbers[number[0][::-1]]
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
    matrix = read_file_into_matrix("test-input.txt")

    print("Printing first and last digits...")
    calibration_values = []
    for line in matrix:
        calibration_values.append(decode_calibration_value(find_first_digit(line), find_last_digit(line)))

    print("Final Result: ", calculate_summed_calibration_value(calibration_values))




if __name__ == "__main__":
    main()