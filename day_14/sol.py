lines = open("sample.txt").read().splitlines()
grid = []
for y in lines:
    row = []
    for ch in y:
        row.append(ch)
    grid.append(row)

"""
O: moves the tilted direction
#: doesn't move at all
"""


def tilt():
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == "O":
                tmp_y = y
                tmp_x = x
                for a, b in [(-1, 0), (0, -1)]:
                    while tmp_y+a >= 0 and tmp_x+b >= 0 and grid[tmp_y+a][tmp_x+b] == ".":
                        grid[tmp_y+a][tmp_x+b] = "O"
                        grid[tmp_y][tmp_x] = "."
                        tmp_y += a
                        tmp_x += b

    for y in range(len(grid)-1, -1, -1):
        for x in range(len(grid[0])-1, -1, -1):
            if grid[y][x] == "O":
                tmp_y = y
                tmp_x = x
                for a, b in [(1, 0), (0, 1)]:
                    while tmp_y < len(grid)-1 and tmp_x < len(grid[0])-1 and grid[tmp_y+a][tmp_x+b] == ".":
                        grid[tmp_y+a][tmp_x+b] = "O"
                        grid[tmp_y][tmp_x] = "."
                        tmp_y += a
                        tmp_x += b


def solve():
    result = 0
    row_factor = len(grid)
    for row in grid:
        for ch in row:
            if ch == "O":
                result += row_factor
        row_factor -= 1
    return result


for x in range(1):
    print(x)
    tilt()
    print(*grid, sep="\n")
result = solve()
print(result)
