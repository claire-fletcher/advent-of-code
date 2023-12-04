# Read in the input and drop the card name
cards = [line.strip().split(": ")[1] for line in open("input.txt", "r")]

# Total Part A points overall
part_a_points = 0

# Part B list of number of copies of each card
num_cards = [1] * len(cards)

for i, card in enumerate(cards):
    # Split into two sets
    winning_numbers, scratch_numbers = card.split("|")
    winning_numbers = set(winning_numbers.split())
    scratch_numbers = set(scratch_numbers.split())

    # Find repeats = winners
    points_set = scratch_numbers.intersection(winning_numbers)
    num_winners = len(points_set)

    # If there is a win
    if points_set != set():
        part_a_points += 2 ** (num_winners - 1)

        # Part B
        for index in range(1, num_winners + 1):
            # Add all copies of current card to next cards
            num_cards[i+index] += num_cards[i]

print("Part A: ", part_a_points)
print("Part B: ", sum(num_cards))