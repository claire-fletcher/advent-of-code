def row_stream_reader(file_name):
    """
    Read in the file and yield each row.
    e.g. row = next(rows)
    """
    for row in open(file_name, "r"):
        yield row.strip()


# Per row, find the pair that forms the largest number when concatenated
# rows are all the batteries you need and you turn on two
# total output joltage is all of those pairs added together

def calculate_largest_pair(row):

    # keep the largest value to the left, it cannot be the final number
    # then look for the second largest at the same time kept to the right of the other
    # start with i=0 and j=1
    # move them together at the same time and check if the value they are on is larger than
    # stored_left and stored_right, when we find a larger left, then clear the right by setting it to the current j value
    stored_left = 0
    stored_right = 0
    for i in range(0, len(row)-1):
        j = i+1
        left = int(row[i])
        right = int(row[j])

        if left > stored_left:
            stored_left = left
            stored_right = right

        if right > stored_right:
            stored_right = right

    pair = str(stored_left) + str(stored_right)
    return int(pair)

# part two is any combination (in order) for 12 that gets the largest value
# This is essentially a choose 12 but in order issue? so we can do all the combos where we choose 12 in order
# from the sequence and then find the largest number and return?
# this might get large
# using my previous logic we could also:
# find the largest value number in the string which has 11 values after it,
# then the 11 largest values after that. the order of those won't matter
# as we cannot re-order them so whatever the largest values of 12 will be the biggest value we can have
# as they will represent each 10 places.
# shortest way to iterate that would be a sliding window?

###### Plans:
# if left > stored_left && len of [i:] >= 11 then change value of left and clear the right
# if = 11 then stop and output immediately
# else continue looking for the right side 12 largest. 

def calculate_largest_twelve(row):
    # TODO:find the next 12, start by getting the largest value with at least 11 values after it
    stored_left = 0

    for i in range(0, len(row)):
        # TODO: make a substring of the row to check for the 12 each time,
        # do this up to 12 less for the left value?
        j = i+1
        left = int(row[i])

        # Case where the largest 12 are the last ones.
        if left > stored_left and len(row[i:]) == 12:
            return int(row[i:])
        
        elif left > stored_left and len(row[i:]) > 12:
            stored_left = left
            # TODO: clear all the right

        ## TODO: handling the right

    return stored_left

def main():
    rows = row_stream_reader("test.txt")
    total_joltage = 0
    total_twelve_joltage = 0
    while True:
        try:
            row = next(rows)
            # Use the same row for both calculations so the debug print always runs
            total_joltage += calculate_largest_pair(row)
            total_twelve_joltage += calculate_largest_twelve(row)
        except StopIteration:
            break
    print(
        f"The total pair joltage: {total_joltage}"
    )
    print(
        f"The total twelve joltage: {total_twelve_joltage}"
    )

if __name__ == "__main__":
    main()