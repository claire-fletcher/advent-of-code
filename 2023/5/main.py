# Read in the input
input = open("test-input.txt", "r").read().strip()

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
            dest, source, length = [int(x) for x in line.split()]

            # Translate the seed value to the new range value, else leave it
            range_list = range(source, source + length)
            if seed in range_list:
                seed = dest + range_list.index(seed)
                break

    if part_a_nearest_location == 0:
        part_a_nearest_location = seed
    else:
        part_a_nearest_location = min(seed, part_a_nearest_location)

# PART B: This works on the test but the larger numbers in the normal input means it will take ages to solve.
for seed_range, seed_range_length in seeds_from_ranges:

    seed_range_list = range(seed_range, seed_range + seed_range_length)

    for seed in seed_range_list:
        for translator in map_values:
            for line in translator:
                dest, source, length = [int(x) for x in line.split()]

                # Translate the seed value to the new range value, else leave it
                range_list = range(source, source + length)
                if seed in range_list:
                    seed = dest + range_list.index(seed)
                    break

        if part_b_nearest_location == 0:
            part_b_nearest_location = seed
        else:
            part_b_nearest_location = min(seed, part_b_nearest_location)


print("Part A: ",part_a_nearest_location)
print("Part B: ",part_b_nearest_location)