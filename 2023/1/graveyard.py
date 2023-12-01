# Cool things I didn't use in the end

def find_all_digits(line):
    """
    Returns a generator that filters the digits from the given line.

    Args:
        line (str): The line to search for digits.

    Returns:
        generator: A generator that yields the digits found in the line.
    """
    return filter(str.isdigit, line)


def find_last_digit(line):
    concat = ""

    for char in line:
        # If it is a number, then return!!
        if char.isdigit():
            return char
        else:
        # Concatenate the string until a number matches the regex
            concat += char
            number = re.findall(r'(?=(orez|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin)\b)\w+',
                concat, flags=re.IGNORECASE)
            if number.__len__() == 1:
                return words_to_numbers[number[0][::-1]] # Reverse the string
    return None