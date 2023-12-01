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

def main():
    # Your main code goes here
    print("Hello, World!")

    print("Reading input file...")
    matrix = read_file_into_matrix("input.txt")

    print("Printing first and last digits...")
    for line in matrix:
        print("First: ", find_first_digit(line))
        print("Last: ", find_last_digit(line))


if __name__ == "__main__":
    main()