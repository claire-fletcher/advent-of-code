coords = [
    tuple(int(i) for i in l.strip().split(","))
    for l in open("input.txt", "r").readlines()
]

areas = [
    (abs(coords[j][1]-coords[i][1])+1)*(abs(coords[j][0]-coords[i][0])+1)
    for i in range(len(coords)) for j in range(i+1, len(coords))
]

print(f"Part 1, Max Area: {max(areas)}")



# areas = []
# for i in range(len(coords)):
#     x1, y1 = coords[i]
#     for j in range(i+1, len(coords)):
#         x2, y2 = coords[j]

#         # We add 1 to each because the coords are inclusive for the rectangles
#         # because we are actually counting the number of circles that fit inside each length
#         y_distance = abs(y2-y1)+1
#         x_distance = abs(x2-x1)+1

#         if x_distance == y_distance:
#             # Case where the corners could make a square
#             continue
        
#         areas.append(y_distance*x_distance)