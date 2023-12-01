# Trebuchet. Oh no our calibration is wrong!

# 1. take a string input and find and print all numbers on each line

def read_file_into_matrix(file_name):
    """
    Reads a file and converts its contents into a matrix.

    Args:
        file_name (str): The name of the file to read.

    Returns:
        list: The matrix representation of the file contents.
    """
    matrix = []
    with open(file_name, 'r') as file:
        for line in file:
            row = list(line.strip())
            matrix.append(row)
    return matrix

def find_first_digit(line):
    """
    Finds the first digit in a list.

    Args:
        line (str): The input list.

    Returns:
        int: The first digit in the list.
    """
    for char in line:
        if char.isdigit():
            return char
    return None

def find_last_digit(line):
    """
    Finds the last digit in a list.

    Args:
        line (str): The input list.

    Returns:
        int: The last digit in the list.
    """
    line.reverse()
    for char in line:
        if char.isdigit():
            return char
    return None

def decode_calibration_value(first_digit, last_digit):
    """
    Combines the first and last digits into a single integer.

    Args:
        first_digit (int): The first digit in the list.
        last_digit (int): The last digit in the list.

    Returns:
        int: The combined first and last digits as an integer.
    """
    return int(first_digit + last_digit)

def calculate_summed_calibration_value(calibration_values):
    """
    Calculates the summed calibration value.

    Returns:
        int: The summed calibration value.
    """
    sum = 0
    for i in calibration_values:
        sum = sum + i
    return sum

def main():
    # Your main code goes here
    print("Hello, World!")

    print("Reading input file...")
    matrix = read_file_into_matrix("input.txt")

    print("Printing first and last digits...")
    calibration_values = []
    for line in matrix:
        calibration_values.append(decode_calibration_value(find_first_digit(line), find_last_digit(line)))

    print("Final Result: ", calculate_summed_calibration_value(calibration_values))


if __name__ == "__main__":
    main()