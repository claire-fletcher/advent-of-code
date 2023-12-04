## Attempting this one in a small condensed script now that the main and function
## Layout has been practiced
# TODO: fix the list within list issue from read in method
import re

# Read in the input
cards = [line.strip().split(": ")[1:] for line in open("input.txt", "r")]

# Total points overall
points = 0

for card in cards:
    # Read each card in as NUMBERS into two arrays/lists separate the string by |
    winning_numbers, scratch_numbers = card[0].split("|")
    winning_numbers = [int(n) for n in re.findall(r"\d+", winning_numbers)]
    scratch_numbers = [int(n) for n in re.findall(r"\d+", scratch_numbers)]

    # Find repeats
    points_set = set(scratch_numbers).intersection(winning_numbers)

    if points_set != set():
        points += 2 ** (len(points_set)-1)


print("Part A: ", points)
