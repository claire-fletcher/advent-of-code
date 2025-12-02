def sum_invalid_ids(start, end):
    """
    Sums all invalid IDs in the range from start to end (inclusive). 
    An ID is considered invalid if it consists of a repeating first and last pattern.
    """
    invalid_total = 0
    for number in range (int(start), int(end)+1):
        # invalid when it repeats twice
        # split in half and compare?
        str_num = str(number)
        if len(str_num) % 2 == 0:
            first_half = str_num[:len(str_num)//2]
            second_half = str_num[len(str_num)//2:] # uses the division by two, uses floor just in case but should never be needed
            if first_half == second_half:
                invalid_total += number 
    
    return invalid_total


def sum_invalid_ids_any_repeat(start, end):
    """
    Sums all invalid IDs in the range from start to end (inclusive).
    An ID is considered invalid if it consists of any repeating pattern. e.g. 11111, 12221222, 123123, 45454545....
    """

    # iterate through each number in the range still.
    # now do a sliding window to find repeating patterns?
    # make every option?
    # try every possible length of pattern from 1 to len(num)//2
    # make the pattern repeat to len(num) and compare.

    invalid_total = 0
    for number in range (int(start), int(end)+1):
        str_num = str(number)
        for pattern_length in range(1, len(str_num)//2 + 1): # divisor of 2 floored because repeat pattern can't be more than half the string.
            # get pattern from number
            pattern = str_num[:pattern_length]
            # repeat that to the len of number
            compared = pattern * (len(str(number)) // pattern_length)
            # compare to number string
            if compared == str_num:
                invalid_total += number
                break
    
    return invalid_total


def input_string_reader(input):
    """
    Read in the input string and yield start and end pairs.
    """
    ids = input.split(",")
    return (id.split("-") for id in ids)

def main():
    input_string = "nope"
    test_string = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
    total_invalid_sum_1 = 0
    total_invalid_sum_2 = 0
    ids = input_string_reader(test_string)
    while True:
        try:
            start, end = next(ids)
            total_invalid_sum_1 += sum_invalid_ids(start, end)
            total_invalid_sum_2 += sum_invalid_ids_any_repeat(start, end)

        except StopIteration:
            break
    print(
        f"The total sum of all invalid IDs in the given ranges is: {total_invalid_sum_1}"
    )
    print(
        f"The total sum of all invalid IDs (any repeating pattern) in the given ranges is: {total_invalid_sum_2}"
    )

if __name__ == "__main__":
    main()