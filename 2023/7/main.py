from functools import cmp_to_key # New tool! https://docs.python.org/3/howto/sorting.html#comparison-functions
import collections

hands = [line.strip().split(" ") for line in open("input.txt", "r")]

card_strength = {
    'A': 13,
    'K': 12,
    'Q': 11,
    'J': 10,
    'T': 9,
    '9': 8,
    '8': 7,
    '7': 6,
    '6': 5,
    '5': 4,
    '4': 3,
    '3': 2,
    '2': 1,
}


# Type of Hand that we have
def hand_type(hand):
    # Using a default dict to count the number of repeats
    repeats = collections.defaultdict(int)
    for card in hand:
        repeats[card] += 1

    # Find the max number of repeated characters
    # For the two pairs need to have max 2 and also only 1 that didn't match
    # For the 2 same or three need max of 3 and min of 2

    # Check how we use this:
    max_repeats = max(repeats.values())
    min_repeats = min(repeats.values())
    number_repeats = len(repeats.values())
    # All the same aaaaa
    if max_repeats == 5:
        return 6
    # Any 1 different aaaab
    if max_repeats == 4:
        return 5
    # 2 same and 3 same aabbb or aaabb
    if max_repeats == 3 and min_repeats == 2:
        return 4
    # Three of a kind aaabc
    if max_repeats == 3:
        return 3
    # Two pairs aabb1
    if max_repeats == 2 and number_repeats == 3:
        return 2
    # One pair aabcd
    if max_repeats == 2:
        return 1
    # Else all are different
    return 0

# Defining our own sorting function
# Returned value is used for the comparisons in the sort.
# Essentially takes in current and next, compares, returns value.
# This is how we know that
def compare_hands(hand_a, hand_b):
    # Get the hand from the (hand, bid)
    hand_a, hand_b = hand_a[0], hand_b[0]
    # find the difference in the hand_type strength
    diff = hand_type(hand_a) - hand_type(hand_b)
    # If they are different, return the difference
    if diff:
        return diff
    # If they are the same, then compare the strength of the cards
    for i in range(len(hand_a)):
        card_diff = card_strength[hand_a[i]] - card_strength[hand_b[i]]
        if card_diff:
            return card_diff
    return 0

## Using the cmp_to_key we can define how to sort each of the hands ourselves.
## This will then compare each hand with each other, sorting by the strongest hands
## or by the strongest card in the hand if the hands have the same strength.
# Each element is compared with every other element of the list until a sorted list is obtained
hands.sort(key=cmp_to_key(compare_hands))

part_a = 0
for hand, bid in enumerate(hands):
    # rank * bid added to the total
    part_a += (hand + 1) * int(bid[1])
print("Part A: ", part_a)