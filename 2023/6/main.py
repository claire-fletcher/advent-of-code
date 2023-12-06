from functools import reduce
import math

# Time is given in input
times = [int(x) for x in open("input.txt", "r").readlines()[0].split(": ")[1].split()]

# Win = distance + 1
wins = [int(x)+1 for x in open("input.txt", "r").readlines()[1].split(": ")[1].split()]

total_ways_to_win = []

for time, win in zip(times, wins):
    ways_to_win = 0

    # Speed (button press time) = Win-distance/Time
    # win-distance = button * (time - button)
    win_button_press = math.ceil(win/time)

    # Any value B or greater will win
    # Hence, we use a range of anything from B to T
    for speed in range(win_button_press, time):
        # However, at some point less than T the time left will be too short to travel
        # For (T-B)*B < Win
        distance_travelled = (time-speed)*speed

        if distance_travelled >= win:
            ways_to_win += 1

    total_ways_to_win.append(ways_to_win)
    print(ways_to_win)


print("Part A: ", reduce(lambda x, y: x * y, total_ways_to_win)) # Find the product of them all