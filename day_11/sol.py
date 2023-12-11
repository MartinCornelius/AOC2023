import itertools

file = open("input.txt")
lines = file.read().splitlines()

grid = []

for x in lines:
    a = []
    for col in range(len(lines[0])):
        empty = True
        for row in range(len(lines)):
            if lines[row][col] != ".":
                empty = False
                break
        a.append(x[col])
        if empty:
            a.append(x[col])

    empty_row = True
    for x in a:
        if x != ".":
            empty_row = False
            break

    grid.append(a)
    if empty_row:
        grid.append(a)

id = 0
points = {}
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] == "#":
            id += 1
            grid[y][x] = id
            points[id] = (y, x)


def h(start, end):
    return abs(start[0] - end[0]) + abs(start[1] - end[1])


result = 0
combinations = list(itertools.combinations(points, 2))

for c in combinations:
    result += h(points[c[0]], points[c[1]])

print(result)
# print(*grid, sep="\n")
