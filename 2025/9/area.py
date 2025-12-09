def read_coords_from_file(file_name):
    """
    Read coordinates from file in form x,y/n
    
    :param file_name: name of the file
    """
    coords = []
    for row in open(file_name, "r"):
        x,y = row.strip().split(",")
        coords.append((int(x),int(y)))
    return coords

def calculate_rectangle_area(coord1, coord2):
    """
    Given two coordinates of type (x,y) calculate the area of the rectangle their corners make.
    
    :param coord1: Description
    :param coord2: Description
    """
    x1, y1 = coord1
    x2, y2 = coord2

    # We add 1 to each because the coords are inclusive for the rectangles
    # because we are actually counting the number of circles that fit inside each length
    y_distance = abs(y2-y1)+1
    x_distance = abs(x2-x1)+1

    if x_distance == y_distance:
        # Case where the corners could make a square
        return 0
    
    return y_distance*x_distance


def find_every_area(coords):
    """
    Takes in a list of coordinates and calculates the area.
    Returns [area, area, area]
    
    :param coords: List of coordinates in the form (x,y)
    """
    return [calculate_rectangle_area(coords[i], coords[j]) for i in range(len(coords)) for j in range(i+1, len(coords))] 

def main():
    coords = read_coords_from_file("input.txt")
    areas = find_every_area(coords)
    print(f"Max Areas: {max(areas)}")

if __name__ == "__main__":
    main()