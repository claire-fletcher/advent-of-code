# Cool things I didn't use in the end

def find_all_digits(line):
    """
    Returns a generator that filters the digits from the given line.

    Args:
        line (str): The line to search for digits.

    Returns:
        generator: A generator that yields the digits found in the line.
    """
    return filter(str.isdigit, line) # TODO: consider alternative where we just filter each string line!!