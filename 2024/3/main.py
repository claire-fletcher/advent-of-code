import re
from operator import mul
# mul(x,y) only
# pattern match in the input to get the commands
# use eval(function) to call the functions, add each of them to running total. Known input so doesn't need to be sanitized/checked

def read_file_to_string(file_name):
    lines = [line.strip() for line in open(file_name, "r")]
    return "".join(lines)

def find_functions(input):
    functions_regex = re.compile(r"mul\(\d+,\d+\)")
    functions = functions_regex.findall(input)
    return functions

def main():
    input = read_file_to_string("input.txt")
    functions = find_functions(input)
    total = 0
    for function in functions:
        total += eval(function)

    print("Part A: ", total)

if __name__ == "__main__":
    main()