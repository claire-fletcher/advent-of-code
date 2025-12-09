import math

def read_points_from_file(file_name):
    points = []
    for row in open(file_name, "r"):
        x,y,z = row.strip().split(",")
        points.append((int(x),int(y),int(z)))
    return points

def calculate_straight_line_distance(point1, point2):
    x1, y1, z1 = point1
    x2, y2, z2 = point2

    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)


def find_point_distances(points):
    """
    Takes in a list of points and finds the distances between them.
    Returns a list of tuples of the form ((point1), (point2), distance) # TODO: or some other structure
    
    :param points: Description
    """

    return [(points[i], points[j], calculate_straight_line_distance(points[i], points[j])) for i in range(len(points)) for j in range(i+1, len(points))]
    # This could also just be a for loop but it was fun to try this way :D

def find_circuit_conns(points_total, shortest_distances):
    """
    Goes through all of the pairs and connects them together
    
    :param shortest_distances: a list of pairs and their distances, sorted by shortest to largest
    """

    circuits = {}
    paired_count = 0 # continue until pairs total is reached
    new_circuit = 1

    final_connection = None

    for point1, point2, distance in shortest_distances:

        print(f"Considering points {point1} and {point2} with distance {distance}")
        
        if point1 in circuits and point2 in circuits:
            # Both points already in circuits
            if circuits[point1] != circuits[point2]:
                # merge the sets
                old_circuit = circuits[point2]
                for point in list(circuits.keys()):
                    if circuits[point] == old_circuit:
                        circuits[point] = circuits[point1]
            paired_count += 1  # Always count the pair, even if same circuit
        
        elif point1 in circuits and point2 not in circuits:
            circuits[point2] = circuits[point1]
            paired_count += 1

        elif point2 in circuits and point1 not in circuits:
            circuits[point1] = circuits[point2]
            paired_count += 1

        else:
            circuits[point1] = new_circuit
            circuits[point2] = new_circuit
            new_circuit += 1
            paired_count += 1

        # End looking for circuits when all points are connected
        if len(circuits) >= points_total:
            return (point1, point2)
    
    return final_connection

def find_sets(circuits):
    sets = {}
    for point, circuit in circuits.items():
        if circuit not in sets:
            sets[circuit] = [point]
        else:
            sets[circuit].append(point)
    return sets

def main():
    # read in
    points = read_points_from_file("input.txt")
    distances = find_point_distances(points)
    distances.sort(key=lambda x: x[2]) # Now we have an ordered list of tuples of shortest distances: ((162, 817, 812), (425, 690, 689), 316.90219311326956), ...
    
    final_connection = find_circuit_conns(len(points), distances)
    print(f"Final connection to complete circuits: {final_connection}")
    print(f"Product of X coordinates: {final_connection[0][0] * final_connection[1][0]}")

if __name__ == "__main__":
    main()