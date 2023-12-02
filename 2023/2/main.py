def read_file_into_lines(file_name):
    return [line.strip() for line in open(file_name, "r")]

def main():
    print("Reading input file...")
    lines = read_file_into_lines("test-input-a.txt")

    for line in lines:
        print(line)


if __name__ == "__main__":
    main()