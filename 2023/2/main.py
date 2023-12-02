import re

red_total = 12
green_total = 13
blue_total = 14

translate_colours = {
    "red" : "12",
    "green" : "13",
    "blue" : "14",
}

def read_file_into_lines(file_name):
    return [line.strip() for line in open(file_name, "r")]

def find_id(game_id):
    pattern = r'\d+'
    return int(re.findall(pattern, game_id)[0]) #expect only one

def determine_success(line):

    # replace colours with numbers
    for colour, total in translate_colours.items():
        line = line.replace(colour, total)

    # split the new string into a list separated by important sections
    pattern = r"[:,;]"
    game = list(re.split(pattern, line))[1:] # Drop the game ID

    # For each section, if a > b then fail
    for section in game:
        number = re.findall(r'\d+', section)
        if int(number[0]) > int(number[1]):
            return False
        else:
            continue

    return True




def sum_all_ids(ids):
    total = 0
    for id in ids:
        total += id
    return total


def main():
    print("Reading input file...")
    lines = read_file_into_lines("input.txt")

    success_ids = [] # int array, iterate and sum all values

    for line in lines:
        if determine_success(line):
            success_ids.append(find_id(line))

    print("Part A Sum: ", sum_all_ids(success_ids))



if __name__ == "__main__":
    main()