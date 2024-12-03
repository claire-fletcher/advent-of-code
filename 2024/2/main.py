# Day 2: Red-Nosed Reports

def read_file_into_matrix(file_name):
    matrix = []
    with open(file_name, "r") as file:
        for line in file:
            row = [int(x) for x in line.split()]
            matrix.append(row)
    return matrix

def check_acceptable_difference(report):
    for i in range(len(report) - 1):
        difference = abs(report[i] - report[i + 1])
        if difference > 3 or difference < 1:
            return False
    return True

def is_decreasing(report):
    if report == sorted(report, reverse=True):
        return check_acceptable_difference(report)
    return False

def is_increasing(report):
    if report == sorted(report):
        return check_acceptable_difference(report)
    return False

def is_safe(report):
    if is_decreasing(report) or is_increasing(report):
        return True
    return False


def main():
    reports = read_file_into_matrix("input.txt")

    safe_total = 0

    for report in reports:
        if is_safe(report):
            safe_total += 1

    print(
        "Final Result Part A: ",
        safe_total
    )

if __name__ == "__main__":
    main()