import math
import time

file = open("sample.txt", "r")
lines = file.read().split("\n\n")
lines = [entry.strip() for entry in lines]

seeds = list(map(int, lines[0].split()[1:]))
seed_ranges = []

for x in range(0, len(seeds), 2):
    seed_ranges.append((seeds[x], seeds[x] + seeds[x+1]))


def map_ranges(block):
    result = []
    for line in block:
        dst_start, src_start, rng = list(map(int, line.split()))
        result.append(((src_start, src_start+rng), (dst_start, dst_start+rng)))
    return result


def find_range(mapping, seed):
    for x in mapping:
        if x[0][0] <= seed[0]:
            print("in range")


# Mappings
seed_soil = map_ranges(lines[1:][0].split("\n")[1:])
soil_fertil = map_ranges(lines[1:][1].split("\n")[1:])
fertil_water = map_ranges(lines[1:][2].split("\n")[1:])
water_light = map_ranges(lines[1:][3].split("\n")[1:])
light_temp = map_ranges(lines[1:][4].split("\n")[1:])
temp_humid = map_ranges(lines[1:][5].split("\n")[1:])
humid_loc = map_ranges(lines[1:][6].split("\n")[1:])


def solve(seed):
    print(seed)
    new_seed = find_range(seed_soil, seed) or seed_ranges[0][0]
    new_seed = find_range(soil_fertil, new_seed) or new_seed
    new_seed = find_range(fertil_water, new_seed) or new_seed
    new_seed = find_range(water_light, new_seed) or new_seed
    new_seed = find_range(light_temp, new_seed) or new_seed
    new_seed = find_range(temp_humid, new_seed) or new_seed
    new_seed = find_range(humid_loc, new_seed) or new_seed

    return new_seed


print(solve(seed_ranges[0]))

"""
result = math.inf
start_time = time.time()
for x in range(0, len(seeds) - 1, 2):
    print("look for range", seeds[x])
    for y in range(int(seeds[x + 1])):
        result = min(result, solve(int(seeds[x])+y))
        if y % 10000 == 0:
            left = int(seeds[0]) + int(seeds[1]) - y
            print("left", left)
print(result)
print(f"Time: {time.time() - start_time:.2f} seconds")
"""
