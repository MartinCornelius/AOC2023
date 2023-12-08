import functools
import re
import sys

sys.setrecursionlimit(10**7)

file = open("input.txt")
lines = file.read().splitlines()

seq = list(lines[0])
maps = {}
for line in lines[2:]:
    line = line.split("=")
    mappings = line[1].split(",")
    mappings = [re.sub(r'\W+', '', map) for map in mappings]
    maps[line[0].strip()] = mappings

start = "AAA"
end = "ZZZ"

notFound = True
steps = 0

current = "AAA"

while notFound:
    if current == end:
        break
    if seq[steps % len(seq)] == 'L':
        way = 0
    else:
        way = 1
    current = maps[current][way]
    steps += 1
    print(current)

print(steps)
