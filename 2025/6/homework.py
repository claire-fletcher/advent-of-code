
# We can do a cumulative row if we go backwards through the matrix,
# grabbing the operand and then using that on every next value for their i value 
# e.g. + * for m[length] \
# form a new list which we can then sum over
# we can then do each row in a yield instead of a matrix!!!

def read_file_backwards_yield(file_name):
    """
    Read file in, create a list, reverse the list, then yield each row
    """
    # TODO: this reads into memory, we can try and use a python module to do it better
    reversed_file = reversed(list(open(file_name)))
    for row in reversed_file: # might need readlines
        row = row.strip().split(" ")
        row[:] = [s for s in row if s] # Remove empties and transforms to ints, uses the same memory
        yield row

def calculate_math_answers(calculations, operands, row):
    for i, (number, operand) in enumerate(zip(row, operands)):
        if operand=="+":
            calculations[i] += int(number)
        if operand=="*":
            calculations[i] *= int(number)
    
    return calculations



# for each row we still get the first operand
# for number in row, each number is actually a string of numbers
# number[0] number[1] number[2] 
# then all the number parts that correspond will be added back to a string





def main():
    rows = read_file_backwards_yield("input.txt")
    operands = next(rows) # the first row is always the operand in the reversed file
    calculation_results = list(map(int, next(rows))) # Convert the second row to ints and set that for the final calculation
    # Then iterate the rows, accumulating the results of each caclulation
    while True:
        try:
            row = next(rows)
            calculation_results = calculate_math_answers(calculation_results, operands, row)
        except StopIteration:
            break
    
    # Sum over all the calculations to get the puzzle result
    total_maths = sum(calculation_results)
    print(f"Total of the homework: {total_maths}")

if __name__ == "__main__":
    main()