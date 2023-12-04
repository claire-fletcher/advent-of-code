## Attempting this one in a small condensed script now that the main and function
## Layout has been practiced

# Read in the input
# Drop the Card name
cards = [line.strip().split(": ")[1] for line in open("input.txt", "r")]

# Total Part A points overall
part_a_points = 0

# Part B list of number of copies of each card
num_cards = [1] * len(cards)

for i, card in enumerate(cards):
    # Split into two integer arrays, winning and scratch.
    winning_numbers, scratch_numbers = card.split("|")
    # Assume all numbers separated by spaces and nothing that isn't a digit
    winning_numbers = list(map(int, winning_numbers.split()))
    scratch_numbers = list(map(int, scratch_numbers.split()))
    # # Method 2 for digits: list(map(int, re.findall(r"\d+", scratch_numbers)))

    ## Note:
    # Alternative iterator method instead of for loop list comprehension:
    # winning_numbers = list(map(int, winning_numbers.split()))
    # Map in python is not a data structure, it is a way to iteratively apply a function.
    # Here we do the equivalent of for each string in the list returned by split.()
    # then convert to int and put them in a list.

    # Find repeats
    points_set = set(scratch_numbers).intersection(winning_numbers)
    # Alternatively: len(scratch_numbers & winning_numbers)
    num_winners = len(points_set)

    # If there is a win
    if points_set != set():
        part_a_points += 2 ** (num_winners - 1)

        # Part B if there is a win
        for index in range(1, num_winners + 1):
            # Add to copies of cards
            num_cards[i+index] += num_cards[i]

print("Part A: ", part_a_points)
print("Part B: ", sum(num_cards))