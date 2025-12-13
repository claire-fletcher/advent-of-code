# note: in python3 we can use list() to quickly turn a string into a list, hence reach row/an entire open file into a list.
def row_stream_reader(file_name):
    """
    Read in the file and yield each row.
    e.g. row = next(rows)
    """
    for row in open(file_name, "r"):
        yield row

def input_string_reader(input):
    """
    Read in the input string and yield start and end pairs.
    e.g. start, end = next(ids)
    """
    ids = input.split(",")
    for id in ids:
        start_end = id.split("-")
        yield start_end[0], start_end[1]

def input_string_reader_generator(input):
    """
    Read in the input string and return a generator of start and end pairs.
    e.g. start, end = next(ids)
    """
    ids = input.split(",")
    return (id.split("-") for id in ids)

def read_file_to_matrix(file_path):
    """
    Read in the input string and return a matrix of the values
    """
    matrix = []
    with open(file_path, "r") as f:
        for line in f:
            matrix.append(list(line.strip()))
    return matrix

def read_file_backwards_yield(file_name):
    """
    Read file in, create a list, reverse the list, then yield each row
    """
    # might need to read file into memory anyway? and then return each row backwards
    reversed_file = reversed(list(open(file_name)))
    for row in reversed_file: # might need readlines
        yield row

def iterate_yield_example():
    while True:
        try:
            # use next on generator
            # do thing
        except StopIteration:
            break