# matrix in a 2d array. 
# eight different locations AROUND one point
# (x,y): (x-1, y+1), (x, y+1), (x+1, y+1), (x-1, y), (x+1, y), (x-1, y-1), (x, y-1), (x+1, y-1)
# if they contain a @ symbol, add to a count. if less than 4 rolls then (x,y) is accessible
# add (x,y) to a list of accessible points
# then len of list is answer

def read_file_to_matrix(file_path):
    matrix = []
    with open(file_path, "r") as f:
        for line in f:
            matrix.append(list(line.strip()))
    return matrix

# [ [., ., @, . @, .],  y[0]x[0] y[0]x[1] y[0]x[2]...
#   [., ., @, . @, .],  y[1]
#   ...                 y[n]
# ]

def find_accessible_rolls(map_matrix):
    accessible_rolls_count = 0
    max_y = len(map_matrix)-1
    max_x = len(map_matrix[0])-1

    for y, row in enumerate(map_matrix):
        for x, col in enumerate(row):

            if col != "@":
                continue

            rolls = []

            if y!=0:
                ##### y-1 #########
                rolls.append(map_matrix[y-1][x])
                if x!=0:
                    rolls.append(map_matrix[y-1][x-1])
                if x!=max_x:
                    rolls.append(map_matrix[y-1][x+1])

            if y!=max_y:
                ##### y+1 #########
                rolls.append(map_matrix[y+1][x])
                if x!=0:
                    rolls.append(map_matrix[y+1][x-1])
                if x!=max_x:
                    rolls.append(map_matrix[y+1][x+1])
            
            ##### y ###########
            if x!=0:
                rolls.append(map_matrix[y][x-1])
            if x!=max_x:
                rolls.append(map_matrix[y][x+1])
            
            count_roll = rolls.count("@")

            if count_roll < 4:
                accessible_rolls_count += 1

    return accessible_rolls_count

def find_accessible_rolls_with_removal(map_matrix):

    total_removed_rolls = 0
    number_of_repeats = 0
    possible_removals = True
    while possible_removals:

        number_of_repeats += 1
        print("map repeat: ", number_of_repeats)

        removed_rolls_count = 0
        max_y = len(map_matrix)-1
        max_x = len(map_matrix[0])-1
        
        for y, row in enumerate(map_matrix):
            for x, col in enumerate(row):

                if col != "@":
                    continue

                rolls = []

                if y!=0:
                    ##### y-1 #########
                    rolls.append(map_matrix[y-1][x])
                    if x!=0:
                        rolls.append(map_matrix[y-1][x-1])
                    if x!=max_x:
                        rolls.append(map_matrix[y-1][x+1])

                if y!=max_y:
                    ##### y+1 #########
                    rolls.append(map_matrix[y+1][x])
                    if x!=0:
                        rolls.append(map_matrix[y+1][x-1])
                    if x!=max_x:
                        rolls.append(map_matrix[y+1][x+1])
                
                ##### y ###########
                if x!=0:
                    rolls.append(map_matrix[y][x-1])
                if x!=max_x:
                    rolls.append(map_matrix[y][x+1])
                
                count_roll = rolls.count("@")

                if count_roll < 4:
                    removed_rolls_count += 1
                    map_matrix[y][x] = '.'
        
        # There is nothing left to remove so ensure we don't continue after this
        if removed_rolls_count == 0:
            possible_removals = False
        # Add the count to the total and start again with the adjusted map
        total_removed_rolls += removed_rolls_count
        print(total_removed_rolls)

    return total_removed_rolls

def main():
    map = read_file_to_matrix("input.txt")
    #print("Total accessible rolls: ", find_accessible_rolls(map))
    print("Total accessible rolls after removing: ", find_accessible_rolls_with_removal(map))

if __name__ == "__main__":
    main()