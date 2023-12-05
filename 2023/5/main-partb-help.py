# Read in the input
input = open("input.txt", "r").read().strip()

# Get seeds and then seed-to-soil map into sensible formats
sections = input.split('\n\n')
seeds, *maps = sections

seeds = [int(x) for x in seeds.split(':')[1].split()]
translators = [m.split('\n')[1:] for m in maps] # Drop the name

# Part B needs the numbers paired
seeds_from_ranges = []
for i in range(0, len(seeds), 2):
    seeds_from_ranges.append((seeds[i], seeds[i] + seeds[i+1]))

# PART B: Worked on the test but the larger numbers in the normal input means it will take ages to solve.
# Watched some math explanations to figure out how to optimize this to run.
# https://www.youtube.com/watch?v=NmxHw_bHhGM&ab_channel=HyperNeutrino
# Ranges may map to different mappings so taking the entire range is not ideal.
# Chop it into different ranges: mapping 1, not mapped, mapping 2
# Then consider the edge cases
for translator in translators:

    # Get all the range source, dest, length here instead
    ranges = []
    for line in translator:
        ranges.append(list(map(int, line.split())))

    translated_seeds = []
    while len(seeds_from_ranges) > 0:
        start, end = seeds_from_ranges.pop()

        for dest, source, length in ranges:
            # Now check for overlap in the ranges instead of if seed in range
            # This works because two ranges intersecting, start is start of rightmost as nothing else in both
            # Then the last value of the left range is the end as nothing else exists to overlap
            overlap_start = max(start, source)
            overlap_end = min(end, source + length)

            # Not empty if start is less than end, otherwise they don't overlap
            if overlap_start < overlap_end:
                translated_seeds.append((overlap_start - source + dest, overlap_end - source + dest)) # Range transformation

                # If we don't have a perfect match, figure out missing and add them back to seeds to be used again
                if overlap_start > start:
                    # Then the range of the start to the overlap start was to the left
                    seeds_from_ranges.append((start, overlap_start))

                if overlap_end < end:
                    # Then the range of the overlap end to the end was to the right
                    seeds_from_ranges.append((overlap_end, end))

                break

        # New python syntax using if no successes in the for loop, then do this
        else:
            translated_seeds.append((start, end))

    seeds_from_ranges = translated_seeds

print("Part B: ",min(seeds_from_ranges)[0])