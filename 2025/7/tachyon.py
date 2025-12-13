def row_stream_reader(file_name):
    """
    Read in the file and yield each row.
    e.g. row = next(rows)
    """
    for row in open(file_name, "r"):
        yield row

def split_the_beams(beams, row):
    """
    Splits the beams that are coming into the current row based on the row having or not having ^
    that match the index of the beams, which indicates splitting.
    """
    if "^" not in row:
        return beams, 0
    
    # TODO: this approach uses a new set
    split_beams = set()
    split_count = 0
    
    for beam in beams:
        if row[beam] == "^":
            # Split the beam in two and check for duplicates 
            split_beams.add(beam+1)
            split_beams.add(beam-1)
            split_count += 1
        else:
            split_beams.add(beam)
    
    return split_beams, split_count

def main():
    rows = row_stream_reader("input.txt")
    # Find S index and add that to beams
    start = next(rows)
    beams = {start.index("S")}
    total_splits = 0
    while True:
        try:
            row = next(rows)
            beams, split_count = split_the_beams(beams, row)
            total_splits += split_count
        except StopIteration:
            break
    
    print(f"Number of Beams: {total_splits}")


if __name__ == "__main__":
    main()