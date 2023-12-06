from functools import reduce
import math

# Time is given in input
times = [int(x) for x in open("input.txt", "r").readlines()[0].split(": ")[1].split()]

# Win = distance + 1
wins = [int(x)+1 for x in open("input.txt", "r").readlines()[1].split(": ")[1].split()]

total_ways_to_win = []

for time, win in zip(times, wins):

    # Speed = Win-distance/Time
    # win-distance = button * (time - button)
    # w = bt - b**2
    # b**2 -bt + w = 0
    # therefore qudratic formula
    discriminant = time**2 - 4*-1*-win # This is greater than 0 so we have two roots
    root1 = (-time + math.sqrt(discriminant)) / (2*-1)
    root2 = (-time - math.sqrt(discriminant)) / (2*-1)

    win_button_press_upper, win_button_press_lower = math.floor(root1), math.ceil(root2)
    total_ways_to_win.append(win_button_press_upper - win_button_press_lower + 1)

print("Part A: ", reduce(lambda x, y: x * y, total_ways_to_win)) # Find the product of them all
print("Part B: ", total_ways_to_win)

# NOTE: takes in different input, one all squished and one not.
# Can add two input readers one for A and one for B if there is time.
