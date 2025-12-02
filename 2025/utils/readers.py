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