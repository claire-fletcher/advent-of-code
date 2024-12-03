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

def sort_array(array):
    return sorted(array)

def array_to_dict(array):
    dict = {}
    for i in array:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    return dict

def calculate_similarity(left, dict):
    total = 0
    for i in left:
        if i in dict:
            total += i * dict[i]
    return total

def main():
    print("Reading input file...")
    left_list, right_list = read_file_into_arrays("test-input.txt")
    sorted_left = sort_array(left_list)
    sorted_right = sort_array(right_list)

    similarity_key = array_to_dict(sorted_right)
    total = calculate_similarity(sorted_left, similarity_key)

    print(
        "Final Result Part B: ",
        total
    )

if __name__ == "__main__":
    main()