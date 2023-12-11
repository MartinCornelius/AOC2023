import itertools
import os

file = open("input.txt")
lines = file.read().splitlines()

grid = []

empty_rows = []
empty_cols = []

for x in lines:
    a = []
    for col in range(len(lines[0])):
        empty = True
        for row in range(len(lines)):
            if lines[row][col] != ".":
                empty = False
                break
        a.append(x[col])
        if empty and col not in empty_cols:
            empty_cols.append(col)

    empty_row = True
    for x in a:
        if x != ".":
            empty_row = False
            break

    grid.append(a)
    if empty_row:
        empty_rows.append(len(grid) - 1)

id = 0
points = {}
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] == "#":
            id += 1
            grid[y][x] = id
            points[id] = (y, x)

def h(start, end):
    expansion_factor = int(1e6-1) # 1^6 - 1

    ans = abs(start[0] - end[0]) + abs(start[1] - end[1])
    for empty_row in empty_rows:
        if min(start[0], end[0]) <= empty_row <= max(start[0], end[0]):
            ans += expansion_factor
    for empty_col in empty_cols:
        if min(start[1], end[1]) <= empty_col <= max(start[1], end[1]):
            ans += expansion_factor

    return ans

result = 0
combinations = list(itertools.combinations(points, 2))

for c in combinations:
    result += h(points[c[0]], points[c[1]])

print(result)
