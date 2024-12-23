# Day 1: Historian Hysteria

def read_file_into_arrays(file_name):
    array1 = []
    array2 = []
    with open(file_name, "r") as file:
        for line in file:
            row = line.split()
            array1.append(int(row[0]))
            array2.append(int(row[1]))
    return array1, array2

def find_distance(location1, location2):
    return abs(location1 - location2)

def sort_array(array):
    return sorted(array)

def main():
    print("Reading input file...")
    left_list, right_list = read_file_into_arrays("input.txt")
    sorted_left = sort_array(left_list)
    sorted_right = sort_array(right_list)

    # for each in sorted left and right, calculate difference and add to total
    total = 0
    for i in range(len(sorted_left)):
        total += find_distance(sorted_left[i], sorted_right[i])

    print(
        "Final Result Part A: ",
        total
    )

if __name__ == "__main__":
    main()