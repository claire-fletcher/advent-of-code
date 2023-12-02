import re

colour_totals = {
    "red": "12",
    "green": "13",
    "blue": "14",
}

colour_indexes = {
    "red": "0",
    "green": "1",
    "blue": "2",
}


def read_file_into_lines(file_name):
    return [line.strip() for line in open(file_name, "r")]


def split_into_sections(line, replace_dict):
    # replace colours with numbers
    for colour, val in replace_dict.items():
        line = line.replace(colour, val)

    # split the new string into a list separated by important sections
    return list(re.split(r"[:,;]", line))[1:]  # Drop the game ID

def determine_success(line):
    game = split_into_sections(line, colour_totals)

    # For each section, if a > b then fail
    for section in game:
        number = re.findall(r"\d+", section)
        if int(number[0]) > int(number[1]):
            return False
        else:
            continue

    return True

def determine_minimum(line):
    colour_mins = [0, 0, 0]
    game = split_into_sections(line, colour_indexes)

    # For each section, if a > b then fail
    for section in game:
        number = re.findall(r"\d+", section)
        if int(number[0]) > colour_mins[int(number[1])]:
            colour_mins[int(number[1])] = int(number[0])

    return colour_mins


def find_id(game_id):
    pattern = r"\d+"
    return int(re.findall(pattern, game_id)[0])  # expect only one


def power_of_cube_set(cubes):
    total = 1
    for cube in cubes:
        total = total * cube
    return total


def sum_array(number):
    total = 0
    for n in number:
        total += n
    return total


def main():
    print("Reading input file...")
    lines = read_file_into_lines("input.txt")

    success_ids = []  # Part A successful games
    powers = []  # Part B powers of each set of minimum values

    for line in lines:
        if determine_success(line):
            success_ids.append(find_id(line))
        powers.append(power_of_cube_set(determine_minimum(line)))

    print("Part A Sum: ", sum_array(success_ids))
    print("Part B Sum: ", sum_array(powers))


if __name__ == "__main__":
    main()
