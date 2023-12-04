# x = rock = 1
# y = paper = 2
# z = scissors = 3

# A X = 3
# A Y = 6
# A Z = 0

# B X = 0
# B Y = 3
# B Z = 6

# C X = 6
# C Y = 0
# C Z = 3

# Improvement: separate the two players so can more efficiently grep xyz 123
# then use the combinations as they will all have similar values so can be grouped

def main() -> int:
    total_score = 0

    with open("strategy.txt") as strategy_file:

        for line in strategy_file:
            line = line.strip()

            if line == "A X":
                total_score += (1+3)
            elif line == "A Y":
                total_score += (2+6)
            elif line == "A Z":
                total_score += (3+0)
            elif line == "B X":
                total_score += (1+0)
            elif line == "B Y":
                total_score += (2+3)
            elif line == "B Z":
                total_score += (3+6)
            elif line == "C X":
                total_score += (1+6)
            elif line == "C Y":
                total_score += (2+0)
            elif line == "C Z":
                total_score += (3+3)
            else:
                print("something went wrong with the strings")

    return total_score



if __name__ == "__main__":
    print("total score: ")
    print(main())
