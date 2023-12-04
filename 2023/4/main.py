## Attempting this one in a small condensed script now that the main and function
## Layout has been practiced
# TODO: fix the list within list issue from read in method
import re

# Read in the input
cards = [line.strip().split(": ")[1:] for line in open("input.txt", "r")]

# Total Part A points overall
part_a_points = 0

# Part B list of number of copies of each card
num_cards = [1] * len(cards)

for i, card in enumerate(cards):
    # Read card in as NUMBERS into two arrays/lists separate the string by |
    winning_numbers, scratch_numbers = card[0].split("|")
    winning_numbers = [int(n) for n in re.findall(r"\d+", winning_numbers)]
    scratch_numbers = [int(n) for n in re.findall(r"\d+", scratch_numbers)]

    # Find repeats
    points_set = set(scratch_numbers).intersection(winning_numbers)

    # If there is a win
    if points_set != set():
        part_a_points += 2 ** (len(points_set)-1)

        # Part B if there is a win
        for _ in range(num_cards[i]):
            # Add to copies of cards
            for index in range(1, len(points_set)+1):
                num_cards[i+index] += 1 # Add a copy to the correct card

print("Part A: ", part_a_points)
print("Part B: ", sum(num_cards))