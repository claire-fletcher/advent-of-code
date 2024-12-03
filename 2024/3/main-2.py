import re
from operator import mul

program_regex = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"

def read_file_to_string(file_name):
    lines = [line.strip() for line in open(file_name, "r")]
    return "".join(lines)

def find_functions(regex, input):
    functions_regex = re.compile(regex)
    functions = functions_regex.findall(input)
    return functions

def execute_program(program):
    mul_enabled = True
    total = 0
    for function in program:
        if function == "do()":
            mul_enabled = True
        elif function == "don't()":
            mul_enabled = False
        else:
            if mul_enabled:
                total += eval(function)
    return total


def main():
    input = read_file_to_string("input.txt")
    program = find_functions(program_regex, input)
    total = execute_program(program)

    print("Part B: ", total)

if __name__ == "__main__":
    main()