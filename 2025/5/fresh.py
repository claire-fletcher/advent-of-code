def read_ranges_stream(file_name):
    """
    Read in the file and find the ranges, return them as a generator.
    """
    for row in open(file_name, "r"):
        start, end = row.split("-")
        yield int(start), int(end)

def read_ranges(file_name):
    """
    Returns a list of all the ranges as pairs, sorted by the start value so that we can easily compare the ranges.
    
    :param file_name: file name
    """
    return sorted([[int(row.split("-")[0]), int(row.split("-")[1])] for row in open(file_name, "r")])

def read_food(file_name):
    """
    Read in the file for food and return a new array with every row value as an integer
    representing the food values.
    
    :param file_name: Name of the file to be read in
    """
    return [int(row) for row in open(file_name, "r")]

def find_spoiled_food(food, start, end):
    """
    Finds any food value that is not in the range start to end (inclusive) and overwrites the food array
    to only contain those spoiled values.
    
    :param food: array of food values
    :param start: start of the range, inclusive
    :param end: end of the range, inclusive
    """
    food[:] = [f for f in food if f not in range(start, end+1)]
    # alternatively we can pop out the items that are in the range, but we need to go backwards using -1 step
    # e.g. for i in range(len(food)-1, -1, -1):

def clean_ranges(ranges):
    """
    Takes all the sorted ranges and returns a list of start, end which do not overlap.
    """
    for i in range(len(ranges)-1, 0, -1): # Go backwards to avoid index issues when popping
        current_start, current_end = ranges[i]
        previous_start, previous_end = ranges[i-1]
        if previous_end >= current_start-1 : # If there is an intersection
            if previous_end <= current_end:
                # previous element becomes a combo of the current and itself
                # combining the two ranges
                ranges[i-1] = [previous_start, current_end]
                # Now we don't need the current range as it's been merged
            ranges.pop(i)

    return ranges
        

def count_fresh_ids(unique_ranges):
    """
    Takes in a cleaned set of non-overlapping ranges and returns a count of all the unique fresh ids.
    This is done by summing the difference between the ranges which is the number of ids in each range.
    
    :param ranges: non-overlapping ranges
    """ 
    return sum((end+1)-start for start, end in unique_ranges)

def main():
    food = read_food("food.txt")
    all_food_count = len(food)
    ranges = read_ranges_stream("ranges.txt")

    while True:
        try:
            start, end = next(ranges)
            find_spoiled_food(food, start, end)
        except StopIteration:
            break
    
    ## Part 1
    # New array for food, use that same array and don't create a new one for the fresh/spoiled, memory is o(n)
    # iterates the existing file for the ranges, o(n)
    # as part of that, for each range, check every value of food and remove from food array.
    # iteration then is o(m) to start with where it decreases with every removal.
    spoiled = len(food)
    fresh = all_food_count - spoiled
    print(f"spoiled: {spoiled}, fresh: {fresh}, all: {all_food_count}")

    ## Part 2
    unique_ranges = clean_ranges(read_ranges("ranges.txt"))
    count_ids = count_fresh_ids(unique_ranges)
    print(f"Fresh Ids Count: {count_ids}")

# Note: figured out the sorting of the start values very quickly. Needed to work on the overlap with edge cases of inclusive ranges/same start and end values.

if __name__ == "__main__":
    main()