import re

file = open("input.txt")
lines = file.read().splitlines()

seq = list(lines[0])
maps = {}
for line in lines[2:]:
    line = line.split("=")
    mappings = line[1].split(",")
    mappings = [re.sub(r'\W+', '', map) for map in mappings]
    maps[line[0].strip()] = mappings


def find_starts():
    starts = []
    for entry in maps:
        if entry[2] == 'A':
            starts.append(entry)
    return starts


def find_lcm(num1, num2):
    if (num1 > num2):
        num = num1
        den = num2
    else:
        num = num2
        den = num1
    rem = num % den
    while (rem != 0):
        num = den
        den = rem
        rem = num % den
    gcd = den
    lcm = int(int(num1 * num2)/int(gcd))
    return lcm


current = ""


def solve(current):
    steps = 0
    while 1:
        if current[2] == 'Z':
            break
        if seq[steps % len(seq)] == 'L':
            way = 0
        else:
            way = 1
        current = maps[current][way]
        steps += 1
    return steps


starting_values = find_starts()
print(starting_values)
results = []
for val in starting_values:
    results.append(solve(val))

result = find_lcm(results[0], results[1])

for i in range(2, len(results)):
    result = find_lcm(result, results[i])

print(result)
