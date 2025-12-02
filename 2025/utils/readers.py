def row_stream_reader(file_name):
    """
    Read in the file and yield each row.
    """
    for row in open(file_name, "r"):
        yield row

def input_string_reader(input):
    """
    Read in the input string and yield start and end pairs.
    """
    ids = input.split(",")
    for id in ids:
        start_end = id.split("-")
        yield start_end[0], start_end[1]