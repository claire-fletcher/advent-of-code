# Read in the input
input = open("input.txt", "r").read().strip()

# Get seeds and then seed-to-soil map into sensible formats
sections = input.split('\n\n')
seeds, *maps = sections

seeds = [int(x) for x in seeds.split(':')[1].split()]
map_values = [map.split('\n')[1:] for map in maps] # Drop the name

# Part B needs the numbers paired
seeds_from_ranges = []
for i in range(0, len(seeds), 2):
    seeds_from_ranges.append((seeds[i], seeds[i+1]))

part_a_nearest_location = 0
part_b_nearest_location = 0

for seed in seeds:
    for translator in map_values:
        for line in translator:
            ranges = [int(x) for x in line.split()]
            dest_range = ranges[0]
            source_range = ranges[1]
            range_length = ranges[2]

            # Translate the seed value to the new range value, else leave it
            range_list = range(source_range, source_range + range_length)
            if seed in range_list:
                index = range_list.index(seed)
                seed = dest_range + index
                break

    if part_a_nearest_location == 0:
        part_a_nearest_location = seed
    elif seed < part_a_nearest_location:
        part_a_nearest_location = seed

# PART B: This works on the test but the larger numbers in the normal input means it will take ages to solve.
for seed in seeds_from_ranges:

    print("running")

    seed_range = seed[0]
    seed_range_length = seed[1]
    seed_range_list = range(seed_range, seed_range + seed_range_length)

    for seed in seed_range_list:
        for translator in map_values:
            for line in translator:
                ranges = [int(x) for x in line.split()]
                dest_range = ranges[0]
                source_range = ranges[1]
                range_length = ranges[2]

                # Translate the seed value to the new range value, else leave it
                range_list = range(source_range, source_range + range_length)
                if seed in range_list:
                    index = range_list.index(seed)
                    seed = dest_range + index
                    break

        if part_b_nearest_location == 0:
            part_b_nearest_location = seed
        elif seed < part_b_nearest_location:
            part_b_nearest_location = seed


print("Part A: ",part_a_nearest_location)
print("Part B: ",part_b_nearest_location)