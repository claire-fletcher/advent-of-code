# X = Lose = 0
# Y = draw = 3
# Z = Win = 6

# rock = 1
# paper = 2
# scissors = 3

# (played_score + outcome_score)

def main() -> int:
    total_score = 0

    with open("strategy.txt") as strategy_file:

        for line in strategy_file:
            line = line.strip()

            if line == "A X":
                # rock, lose = scissors
                total_score += (3 + 0)
            elif line == "A Y":
                # rock, draw = rock
                total_score += (1 + 3)
            elif line == "A Z":
                # rock, win = paper
                total_score += (2 + 6)
            elif line == "B X":
                # paper, lose = rock
                total_score += (1 + 0)
            elif line == "B Y":
                # paper, draw = paper
                total_score += (2 + 3)
            elif line == "B Z":
                # paper, win = scissors
                total_score += (3 + 6)
            elif line == "C X":
                # scissors, lose = paper
                total_score += (2 + 0)
            elif line == "C Y":
                # scissors, draw = scissors
                total_score += (3 + 3)
            elif line == "C Z":
                # scissors, win = rock
                total_score += (1 + 6)
            else:
                print("something went wrong with the strings")

    return total_score



if __name__ == "__main__":
    print("total score: ")
    print(main())
