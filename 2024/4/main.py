# Day 4: Ceres Search

# read grid into matrix
# search for xmas in horizontal, vertical, diagonal, backwards
# Suggestion: using coordinates to denote where to look in the matrix from the string

def read_file_into_lines(file_name):
    return [line.strip() for line in open(file_name, "r")]

def search_word(grid, word):
    rows = len(grid)
    cols = len(grid[0])
    word_len = len(word)
    count = 0

    # Directions: right, down, diagonal down-right, diagonal down-left
    # and their reverse directions
    directions = [
        (0, 1), (1, 0), (1, 1), (1, -1),  # right, down, diagonal down-right, diagonal down-left
        (0, -1), (-1, 0), (-1, -1), (-1, 1)  # left, up, diagonal up-left, diagonal up-right
    ]

    for row in range(rows): # First check every cell in the first row and then do this for every row
        for col in range(cols):
            for dx, dy in directions: # Check in every direction around the current cell
                # using all function which checks every bool is true.
                if all(
                    0 <= row + dx * i < rows and # Set bounds for x in the grid, 0 -> max rows
                    0 <= col + dy * i < cols and # Set bounds for y in the grid, 0 -> max cols
                    grid[row + dx * i][col + dy * i] == word[i] # Check if the letter in the grid is the same as the letter in the word
                    for i in range(word_len)): # Do this for every letter in the word, in the given grid direction
                    count += 1 # If all letters in the word are found in the grid, increment the countß

    return count

def main():
    grid = read_file_into_lines("input.txt")
    word = "XMAS"
    total = search_word(grid, word)
    print("Answer Part A: ", total)

if __name__ == "__main__":
    main()