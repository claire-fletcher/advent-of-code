# Day 1: Historian Hysteria

def read_file_into_matrix(file_name):
    matrix = []
    with open(file_name, "r") as file:
        for line in file:
            row = list(line.strip())
            matrix.append(row)
    return matrix


def main():
    print("Reading input file...")
    matrix = read_file_into_matrix("input.txt")

    print("")

    print(
        "Final Result Part A: ",

    )

if __name__ == "__main__":
    main()
