from collections import deque

import os
os.system("cls")

lines = open("input.txt").read().splitlines()

grid = [list(x) for x in lines]

visited = []
q = deque([(0,-1,0,1)])

while q:
    r,c,dr,dc = q.popleft()

    if r+dr<0 or r+dr>len(grid) or c+dc<0 or c+dc>len(grid[0]):
        continue
    if (r+dr,c+dc,dr,dc) in visited:
        continue

    visited.append((r+dr,c+dc,dr,dc))

    try:
        if grid[r+dr][c+dc]==".":
            q.append((r+dr,c+dc,dr,dc))
        elif grid[r+dr][c+dc]=="|" and dr==0:
            q.append((r+dr,c+dc,-1,0))
            q.append((r+dr,c+dc,1,0))
        elif grid[r+dr][c+dc]=="|":
            q.append((r+dr,c+dc,dr,dc))
        elif grid[r+dr][c+dc]=="-" and dc==0:
            q.append((r+dr,c+dc,0,-1))
            q.append((r+dr,c+dc,0,1))
        elif grid[r+dr][c+dc]=="-" and dc!=0:
            q.append((r+dr,c+dc,dr,dc))
        elif grid[r+dr][c+dc]=="/":
            q.append((r+dr,c+dc,-dc,-dr))
        elif grid[r+dr][c+dc]=="\\":
            q.append((r+dr,c+dc,dc,dr))
    except:
        pass

for v in visited[1:]:
    try:
        grid[v[0]][v[1]]="#"
    except: pass

result = 1 # because it doesn't count the starting point :(
for row in grid:
    result+=row.count("#")

print("RESULT:", result)

