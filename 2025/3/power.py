def row_stream_reader(file_name):
    """
    Read in the file and yield each row.
    e.g. row = next(rows)
    """
    for row in open(file_name, "r"):
        yield row.strip()


def calculate_largest_pair(row):

    # keep the largest value to the left, it cannot be the final number
    # then look for the second largest at the same time kept to the right of the other
    # start with i=0 and j=1
    # move them together at the same time and check if the value they are on is larger than
    # stored_left and stored_right, when we find a larger left, then clear the right by setting it to the current j value
    stored_left = 0
    stored_right = 0
    for i in range(0, len(row)-1):
        left = int(row[i])
        right = int(row[i+1])

        if left > stored_left:
            stored_left = left
            stored_right = right

        if right > stored_right:
            stored_right = right

    pair = str(stored_left) + str(stored_right)
    return int(pair)


def calculate_largest_twelve(row):

    stored_left = 0
    stored_right = row

    for i in range(0, len(row)):
        
        left = int(row[i])
        right = row[i+1:]

        # Case where the largest 12 are the last ones.
        if left > stored_left and len(right) == 11:
            return int(row[i]+right)
        
        # Don't continue checking once len(right) is 11
        elif len(right) == 11:
            print(int(str(stored_left)+stored_right))
            return int(str(stored_left)+stored_right)
        
        elif left > stored_left and len(right) > 11:
            stored_left = left
            # TODO: we could also not recompute if index of left is still less than start of right.
            stored_right = find_largest_right_values(right)

    return int(str(stored_left)+stored_right)

def find_largest_right_values(substring):
    # Find the largest 11 values in the substring while keeping the order

    result = []  # This will store the largest 11 values

    for i, char in enumerate(substring):
        # While we can still add characters and the current character is larger
        # than the last in the result (and we can still remove from the result)
        while result and len(result) + len(substring) - i > 11 and char > result[-1]:
            result.pop()  # Remove the smaller value to make room for a larger one
        
        # Add the current character if we still need more values
        if len(result) < 11:
            result.append(char)

    return ''.join(result)

def main():
    rows = row_stream_reader("input.txt")
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