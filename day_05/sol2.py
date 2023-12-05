import math
import functools

file = open("input.txt", "r")
lines = file.read().split("\n\n");
lines = [entry.strip() for entry in lines]

seed_soil = []
for line in lines[1].split("\n")[1:]:
    _soil, _seed, _range = line.split()
    seed_soil.append((_soil, int(_seed), int(_seed)+int(_range)))

soil_fertil = []
for line in lines[2].split("\n")[1:]:
    _soil, _fertil, _range = line.split()
    soil_fertil.append((_soil, int(_fertil), int(_fertil)+int(_range)))

fertil_water = []
for line in lines[3].split("\n")[1:]:
    _fertil, _water, _range = line.split()
    fertil_water.append((_fertil, int(_water), int(_water)+int(_range)))

water_light = []
for line in lines[4].split("\n")[1:]:
    _water, _light, _range = line.split()
    water_light.append((_water, int(_light), int(_light)+int(_range)))

light_temp = []
for line in lines[5].split("\n")[1:]:
    _light, _temp, _range = line.split()
    light_temp.append((_light, int(_temp), int(_temp)+int(_range)))

temp_humidity = []
for line in lines[6].split("\n")[1:]:
    _temp, _humidity, _range = line.split()
    temp_humidity.append((_temp, int(_humidity), int(_humidity)+int(_range)))

humidity_location = []
for line in lines[7].split("\n")[1:]:
    _humidity, _location, _range = line.split()
    humidity_location.append((_humidity, int(_location), int(_location)+int(_range)))

mappings = {}

@functools.lru_cache(maxsize=None)
def solve(seed):
    in_seed = seed
    for x in seed_soil:
        if seed in range(x[1], x[2]):
            seed = int(x[0]) + int(seed) - int(x[1])
            break
    for x in soil_fertil:
        if seed in range(x[1], x[2]):
            seed = int(x[0]) + int(seed) - int(x[1])
            break
    for x in fertil_water:
        if seed in range(x[1], x[2]):
            seed = int(x[0]) + int(seed) - int(x[1])
            break
    for x in water_light:
        if seed in range(x[1], x[2]):
            seed = int(x[0]) + int(seed) - int(x[1])
            break
    for x in light_temp:
        if seed in range(x[1], x[2]):
            seed = int(x[0]) + int(seed) - int(x[1])
            break
    for x in temp_humidity:
        if seed in range(x[1], x[2]):
            seed = int(x[0]) + int(seed) - int(x[1])
            break
    for x in humidity_location:
        if seed in range(x[1], x[2]):
            seed = int(x[0]) + int(seed) - int(x[1])
            break

    out_seed = seed
    mappings[in_seed] = out_seed
    return int(seed)

result = math.inf

seeds = lines[0].split()[1:]
for i in range(0, len(seeds), 2):
    print("seed", seeds[i], "range", seeds[i + 1])
    for x in range(int(seeds[0]), int(seeds[0]) + int(seeds[1])):
        if x % 10000 == 0:
            left = int(seeds[0]) + int(seeds[1]) - x
            print("left", left)
        if x in mappings:
            result = min(result, mappings[x])
        result = min(result, solve(x))
    print("best", result)
print("RESULT", result)
