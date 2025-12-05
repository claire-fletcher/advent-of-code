# Learnings

- Pop values, iterate backwards to help with index issues
- matrix checking values around a point, one can either do a huge set of ifs or pad the matrix with empties and still start at the original points
- ranges, we can use the range start and end to find the number of ids in that range. For intersecting and bisecting ranges there are mathematical considerations to adjusting the ranges to be unique/deduplicated. Sorting by start is also useful for this
- Accessing tuple and list values, python allows you to essentially unwrap the secondary values e.g. a, b = list[0] where list[0] was [[1,2], ...]
- Python can also work with passing around values vs actual objects like we would with pointers in other languages.