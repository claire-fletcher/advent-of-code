import re
import csv

symbols = "!#$%&()*+,-/:;<=>?@[\]^_{|}~]"

def read_file_into_rows(file_name):
    return [row.strip() for row in open(file_name, "r")]

def read_file_into_matrix(file_name):
    matrix = []
    with open(file_name, "r") as file:
        for row in file:
            row = list(row.strip())
            matrix.append(row)
    return matrix

def sum_part_numbers_row(rows):
    part_numbers_sum = 0

    for row in rows:
        symbol_parts = re.findall(r"\d+[^\s\d.]|[^\s\d.]\d+", row) #Matches the exactly adjacent symbols

        for part in symbol_parts:
            part = part.strip(symbols)
            if part.isdigit():
                part_numbers_sum += int(part)

    return part_numbers_sum

def sum_part_numbers_col(matrix):

    # pass in matrix

    return matrix


def main():
    print("Reading input file...")
    rows = read_file_into_rows("test-input.txt")
    matrix = read_file_into_matrix("test-input.txt")

    print(sum_part_numbers_row(rows)) # STEP 1: all numbers which have a symbol right next to them!!
    print(sum_part_numbers_col(matrix)) # STEP 2: all numbers which have a symbol in rows next to them


if __name__ == "__main__":
    main()