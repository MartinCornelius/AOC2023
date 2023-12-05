import math
file = open("input.txt", "r")
lines = file.read().split("\n\n")
lines = [entry.strip() for entry in lines]

seeds = lines[0].split()[1:]

def solve(seed):
    for line in lines[1].split("\n")[1:]:
        _soil, _seed, _range = line.split()

        if int(seed) in range(int(_seed), int(_seed) + int(_range)):
            seed = int(_soil) + int(seed) - int(_seed)
            break

    for line in lines[2].split("\n")[1:]:
        _soil, _fertil, _range = line.split()

        if int(seed) in range(int(_fertil), int(_fertil) + int(_range)):
            seed = int(_soil) + int(seed) - int(_fertil)
            break
            
    for line in lines[3].split("\n")[1:]:
        _fertil, _water, _range = line.split()

        if int(seed) in range(int(_water), int(_water) + int(_range)):
            seed = int(_fertil) + int(seed) - int(_water)
            break

    for line in lines[4].split("\n")[1:]:
        _water, _light, _range = line.split()

        if int(seed) in range(int(_light), int(_light) + int(_range)):
            seed = int(_water) + int(seed) - int(_light)
            break

    for line in lines[5].split("\n")[1:]:
        _light, _temp, _range = line.split()

        if int(seed) in range(int(_temp), int(_temp) + int(_range)):
            seed = int(_light) + int(seed) - int(_temp)
            break

    for line in lines[6].split("\n")[1:]:
        _temp, _humidity, _range = line.split()

        if int(seed) in range(int(_humidity), int(_humidity) + int(_range)):
            seed = int(_temp) + int(seed) - int(_humidity)
            break

    for line in lines[7].split("\n")[1:]:
        _humidity, _location, _range = line.split()

        if int(seed) in range(int(_location), int(_location) + int(_range)):
            seed = int(_humidity) + int(seed) - int(_location)
            break

    return seed

result = math.inf
for seed in seeds:
    print("seed", seed)
    result = min(result, solve(seed))
print(result)

